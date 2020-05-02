import os
import dash
import uuid
from dash.dash import no_update
from core import Session, PathIndex
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from flask_caching import Cache
from dash.dependencies import Input, Output, State
from callbacks import contact_callbacks, dataupload_callbacks, main_callbacks


# ==============================================================
# Define functions of general use
# ==============================================================


def store_dataset(dataset, session, *args):
    session.__getattribute__('{}_loader'.format(dataset)).register_input(*args)
    session.__getattribute__('{}_loader'.format(dataset)).load()
    cache.set('session-{}'.format(session.id), session)
    return session.__getattribute__('{}_loader'.format(dataset)).layout_states


def serve_layout():
    session_id = initiate_session()
    return html.Div([
        html.Div(session_id, id='session-id', style={'display': 'none'}),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content'),
    ])


def initiate_session():
    session_id = str(uuid.uuid4())
    session = Session(session_id)
    cache.set('session-{}'.format(session_id), session)
    return session_id


# ==============================================================
# Create dash.app
# ==============================================================


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX, PathIndex.FONT_AWESOME.value])
app.title = 'Conkit-Web'
server = app.server
app.config.suppress_callback_exceptions = True
cache = Cache(app.server, config={
    'CACHE_TYPE': 'redis',
    'REDIS_URL' : os.environ.get('REDISCLOUD_URL')

})
app.layout = serve_layout


# ==============================================================
# Define callbacks for the app
# ==============================================================


@app.callback(Output('bug-alert', 'is_open'),
              [Input('issue-select', 'value')])
def toggle_alert(*args):
    return contact_callbacks.toggle_alert(*args)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')],
              [State('session-id', 'children')])
def display_page(*args):
    return main_callbacks.display_page(*args)


@app.callback([Output('contact-map-upload-collapse', 'is_open'),
               Output('sequence-upload-collapse', 'is_open'),
               Output('membranetopology-upload-collapse', 'is_open'),
               Output('secondarystructure-upload-collapse', 'is_open'),
               Output('disorder-upload-collapse', 'is_open'),
               Output('conservation-upload-collapse', 'is_open')],
              [Input('contact-map-upload-head', 'n_clicks'),
               Input('sequence-upload-head', 'n_clicks'),
               Input('membranetopology-upload-head', 'n_clicks'),
               Input('secondarystructure-upload-head', 'n_clicks'),
               Input('disorder-upload-head', 'n_clicks'),
               Input('conservation-upload-head', 'n_clicks')],
              [State('sequence-upload-collapse', 'is_open'),
               State('contact-map-upload-collapse', 'is_open'),
               State('membranetopology-upload-collapse', 'is_open'),
               State('secondarystructure-upload-collapse', 'is_open'),
               State('disorder-upload-collapse', 'is_open'),
               State('conservation-upload-collapse', 'is_open')])
def toggle_input_cards(*args):
    return dataupload_callbacks.toggle_input_cards(*args)


@app.callback([Output('display-control-collapse', 'is_open'),
               Output('warning-collapse', 'is_open'),
               Output('help-collapse', 'is_open')],
              [Input('display-control-head', 'n_clicks'),
               Input('warning-head', 'n_clicks'),
               Input('help-head', 'n_clicks')],
              [State('display-control-collapse', 'is_open'),
               State('warning-collapse', 'is_open'),
               State('help-collapse', 'is_open')])
def toggle_extra_cards(*args):
    return dataupload_callbacks.toggle_extra_cards(*args)


@app.callback([Output("contact-map-text-area", "valid"),
               Output("contact-map-text-area", "invalid"),
               Output("contact-map-invalid-collapse", "is_open"),
               Output("contact-map-filename-alert", "is_open"),
               Output('contact-map-filename-alert', 'children'),
               Output("format-selection-card", "color"),
               Output('contact-map-upload-head', 'color')],
              [Input('upload-contact-map', 'filename'),
               Input("contact-map-text-area", "value"),
               Input("contact-format-select", "value")],
              [State('upload-contact-map', 'contents'),
               State('session-id', 'children')])
def upload_contact_map(*args):
    args = list(args)
    session = cache.get('session-{}'.format(args.pop(-1)))
    layout = dataupload_callbacks.upload_contact_map(*args, session)
    cache.set('session-{}'.format(session.id), session)
    return layout


@app.callback([Output("sequence-text-area", "valid"),
               Output("sequence-text-area", "invalid"),
               Output("sequence-invalid-collapse", "is_open"),
               Output("sequence-filename-alert", "is_open"),
               Output('sequence-filename-alert', 'children'),
               Output('sequence-upload-head', 'color')],
              [Input('upload-sequence', 'filename'),
               Input("sequence-text-area", "value")],
              [State('upload-sequence', 'contents'),
               State('session-id', 'children')])
def upload_sequence(*args):
    args = list(args)
    session = cache.get('session-{}'.format(args.pop(-1)))
    layout = dataupload_callbacks.upload_sequence(*args, session)
    cache.set('session-{}'.format(session.id), session)
    return layout


@app.callback([Output("membranetopology-text-area", "valid"),
               Output("membranetopology-text-area", "invalid"),
               Output("membranetopology-invalid-collapse", "is_open"),
               Output("membranetopology-filename-alert", "is_open"),
               Output('membranetopology-filename-alert', 'children'),
               Output('membranetopology-upload-head', 'color')],
              [Input('upload-membranetopology', 'filename'),
               Input("membranetopology-text-area", "value")],
              [State('upload-membranetopology', 'contents'),
               State('session-id', 'children')])
def upload_membranetopology(*args):
    args = list(args)
    session = cache.get('session-{}'.format(args.pop(-1)))
    layout = dataupload_callbacks.upload_membranetopology(*args, session)
    cache.set('session-{}'.format(session.id), session)
    return layout


@app.callback([Output("secondarystructure-text-area", "valid"),
               Output("secondarystructure-text-area", "invalid"),
               Output("secondarystructure-invalid-collapse", "is_open"),
               Output("secondarystructure-filename-alert", "is_open"),
               Output('secondarystructure-filename-alert', 'children'),
               Output('secondarystructure-upload-head', 'color')],
              [Input('upload-secondarystructure', 'filename'),
               Input("secondarystructure-text-area", "value")],
              [State('upload-secondarystructure', 'contents'),
               State('session-id', 'children')])
def upload_secondarystructure(*args):
    args = list(args)
    session = cache.get('session-{}'.format(args.pop(-1)))
    if session is None:
        return no_update
    layout = dataupload_callbacks.upload_secondarystructure(*args, session)
    cache.set('session-{}'.format(session.id), session)
    return layout


@app.callback([Output("disorder-text-area", "valid"),
               Output("disorder-text-area", "invalid"),
               Output("disorder-invalid-collapse", "is_open"),
               Output("disorder-filename-alert", "is_open"),
               Output('disorder-filename-alert', 'children'),
               Output('disorder-upload-head', 'color')],
              [Input('upload-disorder', 'filename'),
               Input("disorder-text-area", "value")],
              [State('upload-disorder', 'contents'),
               State('session-id', 'children')])
def upload_disorder(*args):
    args = list(args)
    session = cache.get('session-{}'.format(args.pop(-1)))
    if session is None:
        return no_update
    layout = dataupload_callbacks.upload_disorder(*args, session)
    cache.set('session-{}'.format(session.id), session)
    return layout


@app.callback([Output("conservation-text-area", "valid"),
               Output("conservation-text-area", "invalid"),
               Output("conservation-invalid-collapse", "is_open"),
               Output("conservation-filename-alert", "is_open"),
               Output('conservation-filename-alert', 'children'),
               Output('conservation-upload-head', 'color')],
              [Input('upload-conservation', 'filename'),
               Input("conservation-text-area", "value")],
              [State('upload-conservation', 'contents'),
               State('session-id', 'children')])
def upload_conservation(*args):
    args = list(args)
    session = cache.get('session-{}'.format(args.pop(-1)))
    if session is None:
        return no_update
    layout = dataupload_callbacks.upload_conservation(*args, session)
    cache.set('session-{}'.format(session.id), session)
    return layout


@app.callback([Output('_hidden-div', 'children')],
              [Input("contact-map-filename-alert", "is_open"),
               Input("sequence-filename-alert", "is_open"),
               Input("membranetopology-filename-alert", "is_open"),
               Input("secondarystructure-filename-alert", "is_open"),
               Input("disorder-filename-alert", "is_open"),
               Input("conservation-filename-alert", "is_open")],
              [State('session-id', 'children')])
def remove_file(*args):
    args = list(args)
    session = cache.get('session-{}'.format(args.pop(-1)))
    if session is None:
        return no_update
    dataupload_callbacks.remove_file(*args, session)
    cache.set('session-{}'.format(session.id), session)
    return no_update


@app.callback([Output('plot-div', 'children'),
               Output('modal-div', 'children'),
               Output('display-control-collapse', 'children')],
              [Input('plot-button', 'n_clicks'),
               Input('refresh-button', 'n_clicks')],
              [State('track-selection-dropdown', 'value'),
               State('L-cutoff-input', 'value'),
               State('session-id', 'children')])
def create_plot(*args):
    args = list(args)
    session = cache.get('session-{}'.format(args.pop(-1)))
    if session is None:
        return no_update
    layout = dataupload_callbacks.create_plot(*args, session)
    return layout


# ==============================================================
# Start server
# ==============================================================


if __name__ == '__main__':
    app.run_server(debug=True)
