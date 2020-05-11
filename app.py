import os
import dash
import utils
from flask_caching import Cache
from dash.dash import no_update
from dash import callback_context
import dash_core_components as dcc
import dash_html_components as html
from loaders import AdditionalTracks
import dash_bootstrap_components as dbc
from utils.exceptions import SessionTimeOut
from dash.dependencies import Input, Output, State, ALL
from loaders import DatasetReference, SequenceLoader, Loader
from components import RepeatedInputModal, InvalidFileCollapse, FilenameAlert, SessionTimedOutModal, \
    InvalidAddTrackCollapse
from utils import initiate_session, PathIndex, compress_session, decompress_session, ensure_triggered, \
    get_remove_trigger, get_upload_id, remove_unused_fname_alerts


# ==============================================================
# Define functions of general use
# ==============================================================
#

def serve_layout():
    session_id, session = initiate_session()
    cache.set(session_id, session)
    return html.Div([
        html.Div(session_id, id='session-id', style={'display': 'none'}),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content'),
    ])


# ==============================================================
# Create dash.app
# ==============================================================


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX, PathIndex.FONT_AWESOME.value])
app.title = 'ConPlot'
server = app.server
app.config.suppress_callback_exceptions = True
cache = Cache(app.server, config={
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': os.environ.get('REDIS_URL')

})
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
def display_page(*args):
    return utils.display_page(*args)


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
    trigger = callback_context.triggered[0]
    file_divs = [no_update for x in range(0, len(fcontents))]
    cleared_fcontents = [None for x in range(0, len(fcontents))]

    try:
        session_compressed = cache.get(session_id)
        session = decompress_session(session_compressed)
    except SessionTimeOut:
        return file_divs, cleared_fcontents, SessionTimedOutModal()

    if not ensure_triggered(trigger) or session is None:
        return file_divs, cleared_fcontents, None

    dataset, fname, fcontent, index = get_upload_id(trigger, fnames, fcontents)

    if dataset in session.keys() and session[dataset] is not None:
        return file_divs, cleared_fcontents, RepeatedInputModal(dataset)
    elif dataset == DatasetReference.SEQUENCE.value:
        data, invalid = SequenceLoader(fcontent)
    else:
        data, invalid = Loader(fcontent, input_format)

    if invalid:
        file_divs[index] = InvalidFileCollapse(dataset)
        return file_divs, cleared_fcontents, None
    else:
        file_divs[index] = FilenameAlert(fname, dataset)
        session[dataset] = data
        session_compressed = compress_session(session)
        cache.set(session_id, session_compressed)
        return file_divs, cleared_fcontents, None


@app.callback([Output('addtrack-modal-div', 'children'),
               Output('additional-tracks-filenames', 'children')],
              [Input('additionaltrack-upload', 'filename')],
              [State('additionaltrack-upload', 'contents'),
               State('track-selector', 'value'),
               State('additional-tracks-filenames', 'children'),
               State('session-id', 'children')])
def upload_additional_track(fname, fcontent, input_format, fname_alerts, session_id):
    try:
        session_compressed = cache.get(session_id)
        session = decompress_session(session_compressed)
    except SessionTimeOut:
        return SessionTimedOutModal(), no_update

    trigger = callback_context.triggered[0]
    if not ensure_triggered(trigger) or session is None:
        return None, no_update

    dataset = AdditionalTracks.__getattr__(input_format).value

    if dataset in session.keys() and session[dataset] is not None:
        return RepeatedInputModal(dataset), no_update

    data, invalid = Loader(fcontent, input_format)

    fname_alerts = remove_unused_fname_alerts(fname_alerts)

    if invalid:
        if fname_alerts and fname_alerts[-1]['props']['id'] != 'invalid-track-collapse':
            fname_alerts.append(InvalidAddTrackCollapse())
        return None, fname_alerts
    else:
        fname_alerts = [alert for alert in fname_alerts
                        if alert['props']['id'] != 'no-tracks-card'
                        and alert['props']['id'] != 'invalid-track-collapse']
        fname_alerts.append(FilenameAlert(fname, dataset))
        session[dataset] = data
        session_compressed = compress_session(session)
        cache.set(session_id, session_compressed)
        return None, fname_alerts


@app.callback(Output('removefiles-modal-div', 'children'),
              [Input({'type': 'filename-alert', 'index': ALL}, 'is_open')],
              [State('session-id', 'children')])
def remove_dataset(alerts_open, session_id):
    trigger = callback_context.triggered[0]

    try:
        session_compressed = cache.get(session_id)
        session = decompress_session(session_compressed)
    except SessionTimeOut:
        return SessionTimedOutModal()

    if not ensure_triggered(trigger) or session is None:
        return None

    fname, dataset, is_open = get_remove_trigger(trigger)

    if is_open:
        return None
    else:
        del session[dataset]

    compressed_session = compress_session(session)
    cache.set(session_id, compressed_session)
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
    compressed_session = cache.get(session_id)
    session = decompress_session(compressed_session)
    trigger = callback_context.triggered[0]

    return utils.create_ConPlot(session, trigger, track_selection, factor, contact_marker_size, track_marker_size,
                                track_separation)


# ==============================================================
# Start server
# ==============================================================


if __name__ == '__main__':
    app.run_server(debug=True)
