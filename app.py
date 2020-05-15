import os
import dash
import logging
import redis
import utils
import urllib.parse
import uuid
from dash.dash import no_update
import dash_core_components as dcc
import dash_html_components as html
from loaders import AdditionalTracks
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ALL
from loaders import DatasetReference, SequenceLoader, Loader
from components import RepeatedInputModal, FilenameAlert, SessionTimedOutModal, PlotPlaceHolder, DisplayControlCard, \
    InvalidInputModal, InvalidFormatModal
from utils import UrlIndex, compress_data, ensure_triggered, get_remove_trigger, get_upload_id, \
    remove_unused_fname_alerts


# ==============================================================
# Define functions of general use
# ==============================================================
#

def serve_layout():
    session_id = str(uuid.uuid4())
    app.logger.info('New session initiated {}'.format(session_id))
    cache.hset(session_id, 'id', compress_data(session_id))
    cache.expire(session_id, 900)
    return html.Div([
        html.Div(session_id, id='session-id', style={'display': 'none'}),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content'),
    ])


# ==============================================================
# Create dash.app
# ==============================================================


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX, UrlIndex.FONT_AWESOME.value])
app.title = 'ConPlot'
server = app.server
app.config.suppress_callback_exceptions = True

if 'IS_HEROKU' not in os.environ:
    os.environ['REDISCLOUD_URL'] = "redis://localhost:6379"

redis_url = urllib.parse.urlparse(os.environ.get('REDISCLOUD_URL'))
cache = redis.Redis(host=redis_url.hostname, port=redis_url.port, password=redis_url.password)

app.layout = serve_layout


# ==============================================================
# Define callbacks for the app
# ==============================================================

@app.callback(Output('bug-alert', 'is_open'),
              [Input('issue-select', 'value')])
def toggle_alert(*args):
    return utils.toggle_alert(*args)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')],
              [State('session-id', 'children')])
def display_page(url, session_id):
    app.logger.info('Session {} requested url {}'.format(session_id, url))
    if not cache.exists(session_id):
        app.logger.info('Session {} has expired'.format(session_id))
        url = UrlIndex.SESSION_TIMEOUT.value
    else:
        cache.expire(session_id, 900)
    return utils.display_page(url, session_id)


@app.callback([Output('track-selection-card', "color"),
               Output('additionaltrack-upload', 'disabled')],
              [Input('track-selector', "value")])
def toggle_add_track_format(value):
    return utils.toggle_selection_alert(value)


@app.callback([Output("format-selection-card", "color"),
               Output({'type': "upload-button", 'index': DatasetReference.CONTACT_MAP.value}, 'disabled')],
              [Input("contact-format-selector", 'value')])
def toggle_format_alert(*args):
    return utils.toggle_selection_alert(*args)


@app.callback([Output({'type': "file-div", 'index': ALL}, "children"),
               Output({'type': "upload-button", 'index': ALL}, 'contents'),
               Output('inputs-modal-div', 'children')],
              [Input({'type': "upload-button", 'index': ALL}, 'filename')],
              [State({'type': "upload-button", 'index': ALL}, 'contents'),
               State("contact-format-selector", 'value'),
               State('session-id', 'children')])
def upload_dataset(fnames, fcontents, input_format, session_id):
    trigger = dash.callback_context.triggered[0]
    file_divs = [no_update for x in range(0, len(fcontents))]
    cleared_fcontents = [None for x in range(0, len(fcontents))]

    if not ensure_triggered(trigger):
        return file_divs, cleared_fcontents, None
    elif not cache.exists(session_id):
        app.logger.info('Session {} has expired'.format(session_id))
        return file_divs, cleared_fcontents, SessionTimedOutModal()
    else:
        cache.expire(session_id, 900)

    app.logger.info('Session {} upload triggered'.format(session_id))
    dataset, fname, fcontent, index = get_upload_id(trigger, fnames, fcontents)

    if cache.hexists(session_id, dataset):
        app.logger.info('Session {} dataset {} already exists'.format(session_id, dataset))
        return file_divs, cleared_fcontents, RepeatedInputModal(dataset)
    elif dataset == DatasetReference.SEQUENCE.value:
        data, invalid = SequenceLoader(fcontent)
    else:
        data, invalid = Loader(fcontent, input_format)

    if invalid:
        app.logger.info('Session {} dataset {} invalid'.format(session_id, dataset))
        return file_divs, cleared_fcontents, InvalidFormatModal()
    else:
        app.logger.info('Session {} uploads {} - {}'.format(session_id, dataset, fname))
        file_divs[index] = FilenameAlert(fname, dataset)
        cache.hset(session_id, dataset, data)
        return file_divs, cleared_fcontents, None


@app.callback([Output('addtrack-modal-div', 'children'),
               Output('additional-tracks-filenames', 'children')],
              [Input('additionaltrack-upload', 'filename')],
              [State('additionaltrack-upload', 'contents'),
               State('track-selector', 'value'),
               State('additional-tracks-filenames', 'children'),
               State('session-id', 'children')])
def upload_additional_track(fname, fcontent, input_format, fname_alerts, session_id):
    trigger = dash.callback_context.triggered[0]
    if not ensure_triggered(trigger):
        return None, no_update
    elif not cache.exists(session_id):
        app.logger.info('Session {} has expired'.format(session_id))
        return SessionTimedOutModal(), no_update
    else:
        cache.expire(session_id, 900)

    app.logger.info('Session {} upload triggered'.format(session_id))
    dataset = AdditionalTracks.__getattr__(input_format).value

    if cache.hexists(session_id, dataset):
        app.logger.info('Session {} dataset {} already exists'.format(session_id, dataset))
        return RepeatedInputModal(dataset), no_update

    data, invalid = Loader(fcontent, input_format)

    fname_alerts = remove_unused_fname_alerts(fname_alerts)

    if invalid:
        app.logger.info('Session {} dataset {} invalid'.format(session_id, dataset))
        return InvalidFormatModal(), fname_alerts
    else:
        app.logger.info('Session {} uploads {} - {}'.format(session_id, dataset, fname))
        fname_alerts = [alert for alert in fname_alerts
                        if alert['props']['id'] != 'no-tracks-card'
                        and alert['props']['id'] != 'invalid-track-collapse']
        fname_alerts.append(FilenameAlert(fname, dataset))
        cache.hset(session_id, dataset, data)
        return None, fname_alerts


@app.callback(Output('removefiles-modal-div', 'children'),
              [Input({'type': 'filename-alert', 'index': ALL}, 'is_open')],
              [State('session-id', 'children')])
def remove_dataset(alerts_open, session_id):
    trigger = dash.callback_context.triggered[0]
    if not ensure_triggered(trigger):
        return None
    elif not cache.exists(session_id):
        app.logger.info('Session {} has expired'.format(session_id))
        return SessionTimedOutModal()
    else:
        cache.expire(session_id, 900)

    app.logger.info('Session {} remove file triggered'.format(session_id))
    fname, dataset, is_open = get_remove_trigger(trigger)

    if is_open:
        app.logger.info('Session {} removal of {} aborted'.format(session_id, dataset))
        return None
    else:
        app.logger.info('Session {} removed dataset {}'.format(session_id, dataset))
        cache.hdel(session_id, dataset)

    return None


@app.callback([Output('plot-div', 'children'),
               Output('plot-modal-div', 'children'),
               Output('display-control-cardbody', 'children'),
               Output('refresh-button-2', 'disabled')],
              [Input('plot-button', 'n_clicks'),
               Input('refresh-button-2', 'n_clicks')],
              [State('L-cutoff-input', 'value'),
               State('contact-marker-size-input', 'value'),
               State('track-marker-size-input', 'value'),
               State('track-separation-size-input', 'value'),
               State({'type': "track-select", 'index': ALL}, 'value'),
               State('session-id', 'children')])
def create_ConPlot(plot_click, refresh_click, factor, contact_marker_size, track_marker_size,
                   track_separation, track_selection, session_id):
    trigger = dash.callback_context.triggered[0]
    if not ensure_triggered(trigger):
        return PlotPlaceHolder(), None, DisplayControlCard(), True
    elif not cache.exists(session_id):
        app.logger.info('Session {} has expired'.format(session_id))
        return PlotPlaceHolder(), SessionTimedOutModal(), DisplayControlCard(), True
    else:
        cache.expire(session_id, 900)

    app.logger.info('Session {} plot requested'.format(session_id))

    if any([True for x in (factor, contact_marker_size, track_marker_size, track_separation) if x is None]):
        app.logger.info('Session {} invalid display control value detected'.format(session_id))
        return no_update, InvalidInputModal(), no_update, no_update

    session = cache.hgetall(session_id)

    app.logger.info('Session {} creating conplot'.format(session_id))
    return utils.create_ConPlot(session, trigger, track_selection, factor, contact_marker_size, track_marker_size,
                                track_separation)


# ==============================================================
# Start server
# ==============================================================

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

if __name__ == '__main__':
    app.run_server(debug=True)
