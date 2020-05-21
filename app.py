import components
import dash
from utils.exceptions import UserExists, EmailAlreadyUsed, IntegrityError
import layouts
import loaders
import logging
import redis
from utils import callback_utils, data_utils, session_utils, cache_utils, app_utils, redis_utils, plot_utils, UrlIndex
from dash.dash import no_update
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ALL


# ==============================================================
# Define functions and variables of general use
# ==============================================================
#

def serve_layout():
    cache = redis.Redis(connection_pool=redis_pool)
    session_id = session_utils.initiate_session(cache, app.logger)

    return html.Div([
        html.Div(session_id, id='session-id', style={'display': 'none'}),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content'),
    ])


def update_fname_alerts(session_id, enumerator, cache):
    fname_alerts = []
    for idx, dataset in enumerate(enumerator):
        if cache.hexists(session_id, dataset.value):
            fname = cache_utils.decompress_data(cache.hget(session_id, dataset.value)).pop(-1)
            fname_alerts.append(components.FilenameAlert(fname, dataset.value))
    if enumerator == loaders.MandatoryDatasetReference:
        return fname_alerts + [no_update for x in range(0, 2 - len(fname_alerts))]
    elif not fname_alerts:
        return no_update

    return fname_alerts


# ==============================================================
# Create dash.app
# ==============================================================


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX, UrlIndex.FONT_AWESOME.value])
app.title = 'ConPlot'
server = app.server
app.config.suppress_callback_exceptions = True

redis_pool = redis_utils.create_pool()
app.layout = serve_layout


# ==============================================================
# Define callbacks for the app
# ==============================================================

@app.callback([Output('contact-alert-div', 'children'),
               Output('submit-contact-form-button', 'disabled')],
              [Input('issue-select', 'value')])
def toggle_alert(*args):
    return callback_utils.toggle_alert(*args)


@app.callback(Output('contact-form-modal-div', 'children'),
              [Input('submit-contact-form-button', 'n_clicks')],
              [State('contact-name-input', 'value'),
               State('contact-email-input', 'value'),
               State('issue-select', 'value'),
               State('contact-text-area-input', 'value'),
               State('session-id', 'children')])
def submit_contact_form(n_clicks, name, email, subject, description, session_id):
    trigger = dash.callback_context.triggered[0]
    cache = redis.Redis(connection_pool=redis_pool)

    if session_utils.is_expired_session(session_id, cache, app.logger):
        return components.SessionTimedOutModal()
    elif not callback_utils.ensure_triggered(trigger):
        return no_update

    return callback_utils.submit_form(name, email, subject, description, app.logger)


@app.callback([Output('track-selection-card', "color"),
               Output('additionaltrack-upload', 'disabled')],
              [Input('track-selector', "value")])
def toggle_add_track_format(value):
    return callback_utils.toggle_selection_alert(value)


@app.callback([Output("format-selection-card", "color"),
               Output({'type': "upload-button", 'index': loaders.DatasetReference.CONTACT_MAP.value}, 'disabled')],
              [Input("contact-format-selector", 'value')])
def toggle_format_alert(*args):
    return callback_utils.toggle_selection_alert(*args)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')],
              [State('session-id', 'children')])
def display_page(url, session_id):
    app.logger.info('Session {} requested url {}'.format(session_id, url))
    cache = redis.Redis(connection_pool=redis_pool)

    if url is None:
        return no_update
    elif session_utils.is_expired_session(session_id, cache, app.logger):
        return layouts.SessionTimeout(session_id)

    return app_utils.serve_url(url, session_id, cache, app.logger)


@app.callback([Output('invalid-login-collapse', 'is_open'),
               Output('success-login-alert-div', 'children')],
              [Input("user-login-button", 'n_clicks')],
              [State('username-input', 'value'),
               State('password-input', 'value'),
               State('session-id', 'children')])
def user_login(n_clicks, username, password, session_id):
    trigger = dash.callback_context.triggered[0]
    cache = redis.Redis(connection_pool=redis_pool)

    if session_utils.is_expired_session(session_id, cache, app.logger):
        return no_update, components.SessionTimedOutToast()
    elif not callback_utils.ensure_triggered(trigger):
        return no_update, no_update

    return app_utils.user_login(username, password, session_id, cache, app.logger)


@app.callback(Output('success-logout-alert-div', 'children'),
              [Input("user-logout-button", 'n_clicks')],
              [State('session-id', 'children')])
def user_logout(n_clicks, session_id):
    trigger = dash.callback_context.triggered[0]
    cache = redis.Redis(connection_pool=redis_pool)

    if session_utils.is_expired_session(session_id, cache, app.logger):
        return components.SessionTimedOutToast()
    elif not callback_utils.ensure_triggered(trigger):
        return no_update

    return app_utils.user_logout(session_id, cache, app.logger)


@app.callback([Output('invalid-create-user-collapse', 'is_open'),
               Output('success-create-user-alert-div', 'children')],
              [Input("create-user-button", 'n_clicks')],
              [State('username-input', 'value'),
               State('password-input', 'value'),
               State('email-input', 'value'),
               State('session-id', 'children')])
def create_user(n_clicks, username, password, email, session_id):
    trigger = dash.callback_context.triggered[0]
    cache = redis.Redis(connection_pool=redis_pool)

    if session_utils.is_expired_session(session_id, cache, app.logger):
        return no_update, components.SessionTimedOutToast()
    elif not callback_utils.ensure_triggered(trigger):
        return no_update, no_update

    try:
        app_utils.create_user(username, password, email, session_id, cache, app.logger)
        return False
    except (UserExists, EmailAlreadyUsed, IntegrityError) as e:
        return True


@app.callback(Output('success-change-password-alert-div', 'children'),
              [Input('user-change-password-button', 'n_clicks')],
              [State('old-password-input', 'value'),
               State('new-password-input', 'value'),
               State('session-id', 'children')])
def change_password(n_clicks, old_password, new_password, session_id):
    trigger = dash.callback_context.triggered[0]
    cache = redis.Redis(connection_pool=redis_pool)

    if session_utils.is_expired_session(session_id, cache, app.logger):
        return components.SessionTimedOutToast()
    elif not callback_utils.ensure_triggered(trigger):
        return no_update

    return app_utils.change_password(new_password, old_password, cache, session_id, app.logger)


@app.callback([Output('stored-sessions-toast-div', 'children'),
               Output('stored-sessions-list-spinner', 'children')],
              [Input({'type': 'delete-session-button', 'index': ALL}, 'n_clicks'),
               Input({'type': 'load-session-button', 'index': ALL}, 'n_clicks')],
              [State('session-id', 'children')])
def manage_stored_sessions(delete_clicks, load_click, session_id):
    trigger = dash.callback_context.triggered[0]
    cache = redis.Redis(connection_pool=redis_pool)

    if session_utils.is_expired_session(session_id, cache, app.logger):
        return components.SessionTimedOutToast(), no_update
    elif not callback_utils.ensure_triggered(trigger):
        return no_update, no_update

    session_name, action = callback_utils.get_session_action(trigger)
    username, current_session_name = session_utils.get_current_info(session_id, cache)

    if action == 'delete':
        return session_utils.delete_session(username, session_name, current_session_name, session_id, app.logger)
    else:
        return session_utils.load_session(username, session_name, session_id, cache, app.logger)


@app.callback(Output('store-session-modal-div', 'children'),
              [Input('store-session-button', 'n_clicks')],
              [State('new-session-name-input', 'value'),
               State('session-id', 'children')])
def store_session(n_clicks, session_name, session_id):
    trigger = dash.callback_context.triggered[0]
    cache = redis.Redis(connection_pool=redis_pool)

    if session_utils.is_expired_session(session_id, cache, app.logger):
        return components.SessionTimedOutToast()
    elif not callback_utils.ensure_triggered(trigger):
        return no_update

    return session_utils.store_session(session_name, session_id, cache, app.logger)


@app.callback([Output({'type': "file-div", 'index': ALL}, "children"),
               Output({'type': "upload-button", 'index': ALL}, 'contents'),
               Output('inputs-modal-div', 'children')],
              [Input({'type': "upload-button", 'index': ALL}, 'filename')],
              [State({'type': "upload-button", 'index': ALL}, 'contents'),
               State("contact-format-selector", 'value'),
               State('session-id', 'children')])
def upload_dataset(fnames, fcontents, input_format, session_id):
    trigger = dash.callback_context.triggered[0]
    cleared_fcontents = [None for x in range(0, len(fcontents))]
    cache = redis.Redis(connection_pool=redis_pool)

    if session_utils.is_expired_session(session_id, cache, app.logger):
        return [no_update for x in range(0, len(fcontents))], cleared_fcontents, components.SessionTimedOutModal()
    elif not callback_utils.ensure_triggered(trigger):
        return update_fname_alerts(session_id, loaders.MandatoryDatasetReference, cache), cleared_fcontents, None

    return data_utils.upload_dataset(input_format, trigger, fnames, fcontents, session_id, cache, app.logger)


@app.callback([Output('addtrack-modal-div', 'children'),
               Output('additional-tracks-filenames', 'children')],
              [Input('additionaltrack-upload', 'filename')],
              [State('additionaltrack-upload', 'contents'),
               State('track-selector', 'value'),
               State('additional-tracks-filenames', 'children'),
               State('session-id', 'children')])
def upload_additional_track(fname, fcontent, input_format, fname_alerts, session_id):
    trigger = dash.callback_context.triggered[0]
    cache = redis.Redis(connection_pool=redis_pool)

    if session_utils.is_expired_session(session_id, cache, app.logger):
        return components.SessionTimedOutModal(), no_update
    elif not callback_utils.ensure_triggered(trigger):
        return None, update_fname_alerts(session_id, loaders.AdditionalDatasetReference, cache)

    return data_utils.upload_additional_track(fcontent, input_format, fname, fname_alerts, session_id, cache,
                                              app.logger)


@app.callback(Output('removefiles-modal-div', 'children'),
              [Input({'type': 'filename-alert', 'index': ALL}, 'is_open')],
              [State('session-id', 'children')])
def remove_dataset(alerts_open, session_id):
    trigger = dash.callback_context.triggered[0]
    cache = redis.Redis(connection_pool=redis_pool)

    if not callback_utils.ensure_triggered(trigger):
        return None
    elif session_utils.is_expired_session(session_id, cache, app.logger):
        return components.SessionTimedOutModal()

    data_utils.remove_dataset(trigger, cache, session_id, app.logger)
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
    cache = redis.Redis(connection_pool=redis_pool)

    if not callback_utils.ensure_triggered(trigger):
        return components.PlotPlaceHolder(), None, components.DisplayControlCard(), True
    elif session_utils.is_expired_session(session_id, cache, app.logger):
        return components.PlotPlaceHolder(), components.SessionTimedOutModal(), components.DisplayControlCard(), True

    app.logger.info('Session {} plot requested'.format(session_id))

    if any([True for x in (factor, contact_marker_size, track_marker_size, track_separation) if x is None]):
        app.logger.info('Session {} invalid display control value detected'.format(session_id))
        return no_update, components.InvalidInputModal(), no_update, no_update

    session = cache.hgetall(session_id)

    app.logger.info('Session {} creating conplot'.format(session_id))
    return plot_utils.create_ConPlot(session, trigger, track_selection, factor, contact_marker_size,
                                     track_marker_size,
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
