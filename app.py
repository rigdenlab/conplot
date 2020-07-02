import components
import dash
import layouts
import loaders
import logging
import redis
from utils import callback_utils, data_utils, session_utils, app_utils, redis_utils, plot_utils, UrlIndex
from dash.dash import no_update
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ALL, MATCH


# ==============================================================
# Define functions and variables of general use
# ==============================================================
#

def serve_layout():
    cache = redis.Redis(connection_pool=redis_pool)
    session_id = session_utils.initiate_session(cache, app.logger)
    return layouts.Base(session_id)


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


@app.callback(Output('custom-format-specs-modal', 'is_open'),
              [Input('custom-format-specs-button', 'n_clicks')])
def toggle_customformatspecs_modal(n_clicks):
    trigger = dash.callback_context.triggered[0]
    if not callback_utils.ensure_triggered(trigger):
        return no_update
    return True


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
               Output('additional-tracks-upload', 'disabled')],
              [Input('additional-track-selector', "value")])
def toggle_add_track_format(value):
    return callback_utils.toggle_selection_alert(value)


@app.callback([Output("format-selection-card", "color"),
               Output('upload-contact-component', 'disabled')],
              [Input("contact-format-selector", 'value')])
def toggle_format_alert(*args):
    return callback_utils.toggle_selection_alert(*args)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')],
              [State('session-id', 'children')])
def display_page(url, session_id):
    trigger = dash.callback_context.triggered[0]
    cache = redis.Redis(connection_pool=redis_pool)

    if url is None:
        return no_update
    elif session_utils.is_expired_session(session_id, cache, app.logger):
        return layouts.SessionTimeout(session_id)
    elif not callback_utils.ensure_triggered(trigger):
        return no_update

    app.logger.info('Session {} requested url {}'.format(session_id, url))
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
        return no_update, components.SessionTimedOutModal()
    elif not callback_utils.ensure_triggered(trigger):
        return no_update, no_update

    return app_utils.create_user(username, password, email, session_id, cache, app.logger)


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


@app.callback(Output({'type': 'share-session-toast-div', 'index': MATCH}, 'children'),
              [Input({'type': 'share-session-button', 'index': MATCH}, 'n_clicks')],
              [State({'type': 'share-username-input', 'index': MATCH}, 'value'),
               State({'type': 'share-username-input', 'index': MATCH}, 'id'),
               State('session-id', 'children')])
def share_session(share_click, share_with, session_pkid, session_id):
    trigger = dash.callback_context.triggered[0]
    cache = redis.Redis(connection_pool=redis_pool)
    session_pkid = session_pkid['index']

    if session_utils.is_expired_session(session_id, cache, app.logger):
        return components.SessionTimedOutToast()
    elif not callback_utils.ensure_triggered(trigger):
        return no_update

    username, current_session_pkid = session_utils.get_current_info(session_id, cache)
    if not share_with:
        return components.InvalidUsernameToast()
    elif username == share_with:
        return components.ShareWithOwnerToast()

    return session_utils.share_session(session_pkid, share_with, app.logger)


@app.callback([Output('session-storage-toast-div', 'children'),
               Output('stored-sessions-list-spinner', 'children'),
               Output('shared-sessions-list-spinner', 'children')],
              [Input({'type': 'delete-session-button', 'index': ALL}, 'n_clicks'),
               Input({'type': 'load-session-button', 'index': ALL}, 'n_clicks'),
               Input({'type': 'stop-share-session-button', 'index': ALL}, 'n_clicks'),
               Input({'type': 'load-share-session-button', 'index': ALL}, 'n_clicks')],
              [State('session-id', 'children')])
def manage_stored_sessions(delete_clicks, load_click, stop_share, load_share, session_id):
    trigger = dash.callback_context.triggered[0]
    cache = redis.Redis(connection_pool=redis_pool)

    if session_utils.is_expired_session(session_id, cache, app.logger):
        return components.SessionTimedOutToast(), no_update, no_update
    elif not callback_utils.ensure_triggered(trigger):
        return no_update, no_update, no_update

    selected_session_pkid, action = callback_utils.get_session_action(trigger)
    username, current_session_pkid = session_utils.get_current_info(session_id, cache)

    if action == callback_utils.ButtonActions.delete:
        return session_utils.delete_session(selected_session_pkid, current_session_pkid, session_id, app.logger)
    elif action == callback_utils.ButtonActions.load:
        return session_utils.load_session(username, selected_session_pkid, session_id, cache, app.logger)
    elif action == callback_utils.ButtonActions.stop:
        return session_utils.stop_share_session(username, selected_session_pkid, current_session_pkid,
                                                session_id, app.logger)


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


@app.callback([Output('sequence-filename-div', "children"),
               Output('upload-sequence-component', 'contents'),
               Output('sequence-upload-modal-div', 'children')],
              [Input('upload-sequence-component', 'filename')],
              [State('upload-sequence-component', 'contents'),
               State('session-id', 'children')])
def upload_sequence(fname, fcontent, session_id):
    trigger = dash.callback_context.triggered[0]
    cache = redis.Redis(connection_pool=redis_pool)

    if session_utils.is_expired_session(session_id, cache, app.logger):
        return no_update, None, components.SessionTimedOutModal()
    elif not callback_utils.ensure_triggered(trigger):
        return callback_utils.retrieve_sequence_fname(session_id, cache), None, None

    return data_utils.upload_sequence(fname, fcontent, session_id, cache, app.logger)


@app.callback([Output('contact-filenames-div', "children"),
               Output('upload-contact-component', 'contents'),
               Output('contact-upload-modal-div', 'children')],
              [Input('upload-contact-component', 'filename')],
              [State('upload-contact-component', 'contents'),
               State("contact-format-selector", 'value'),
               State('contact-filenames-div', "children"),
               State('session-id', 'children')])
def upload_contact(fname, fcontent, input_format, fname_alerts, session_id):
    trigger = dash.callback_context.triggered[0]
    cache = redis.Redis(connection_pool=redis_pool)

    if session_utils.is_expired_session(session_id, cache, app.logger):
        return no_update, None, components.SessionTimedOutModal()
    elif not callback_utils.ensure_triggered(trigger):
        return callback_utils.retrieve_contact_fnames(session_id, cache), None, None

    return data_utils.upload_dataset(fname, fcontent, input_format, fname_alerts, session_id, cache, app.logger,
                                     dataset=loaders.DatasetReference.CONTACT_MAP.value)


@app.callback([Output('additional-tracks-filenames-div', 'children'),
               Output('additional-tracks-upload', 'contents'),
               Output('additional-tracks-upload-modal-div', 'children')],
              [Input('additional-tracks-upload', 'filename')],
              [State('additional-tracks-upload', 'contents'),
               State('additional-track-selector', 'value'),
               State('additional-tracks-filenames-div', 'children'),
               State('session-id', 'children')])
def upload_additional_track(fname, fcontent, input_format, fname_alerts, session_id):
    trigger = dash.callback_context.triggered[0]
    cache = redis.Redis(connection_pool=redis_pool)

    if session_utils.is_expired_session(session_id, cache, app.logger):
        return no_update, None, components.SessionTimedOutModal()
    elif not callback_utils.ensure_triggered(trigger):
        return callback_utils.retrieve_additional_fnames(session_id, cache), None, None

    return data_utils.upload_dataset(fname, fcontent, input_format, fname_alerts, session_id, cache, app.logger)


@app.callback(Output('removefiles-modal-div', 'children'),
              [Input({'type': 'filename-alert', 'index': ALL}, 'is_open')],
              [State('session-id', 'children')])
def remove_dataset(alerts_open, session_id):
    trigger = dash.callback_context.triggered[-1]
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
               State({'type': "halfsquare-select", 'index': ALL}, 'value'),
               State("transparent-tracks-switch", 'value'),
               State('superimpose-maps-switch', 'value'),
               State({'type': 'colorpalette-select', 'index': ALL}, 'value'),
               State('session-id', 'children')])
def create_ConPlot(plot_click, refresh_click, factor, contact_marker_size, track_marker_size, track_separation,
                   track_selection, cmap_selection, transparent, superimpose, selected_palettes, session_id):
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
    elif superimpose and ('---' in cmap_selection or len(set(cmap_selection)) == 1):
        return no_update, components.InvalidMapSelectionModal(), no_update, no_update

    session = cache.hgetall(session_id)

    app.logger.info('Session {} creating conplot'.format(session_id))
    return plot_utils.create_ConPlot(session, trigger, track_selection, cmap_selection, selected_palettes, factor,
                                     contact_marker_size, track_marker_size, track_separation, transparent, superimpose)


# ==============================================================
# Start server
# ==============================================================

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

if __name__ == '__main__':
    app.run_server(debug=True)
