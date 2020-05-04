import os
from enum import Enum
import dash
import utils
from dash.dash import no_update
from dash import callback_context
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from flask_caching import Cache
from dash.dependencies import Input, Output, State
from loaders import DatasetReference, SequenceLoader, Loader
from utils import initiate_session, PathIndex, compress_session, decompress_session, ensure_triggered, SessionTimeOut
import gc

# ==============================================================
# Define functions of general use
# ==============================================================


class LoaderReference(Enum):
    CONTACT_MAP = Loader
    SEQUENCE = SequenceLoader
    MEMBRANE_TOPOLOGY = Loader
    SECONDARY_STRUCTURE = Loader
    CONSERVATION = Loader
    DISORDER = Loader


def serve_layout():
    session_id, session = initiate_session()
    cache.set(session_id, session)
    return html.Div([
        html.Div(session_id, id='session-id', style={'display': 'none'}),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content'),
    ])


def upload_dataset(*args):
    args = list(args)
    session_id = args.pop(-1)
    dataset = args.pop(0)
    session_compressed = cache.get(session_id)
    session = decompress_session(session_compressed)
    data, *layout_states = LoaderReference.__dict__[dataset.name](*args)

    if not ensure_triggered(callback_context.triggered) or session is None:
        return [no_update for x in layout_states]

    session[dataset.value] = data
    layout_states = layout_states
    session_compressed = compress_session(session)
    cache.set(session_id, session_compressed)
    del data
    del session
    gc.collect()
    return layout_states


# ==============================================================
# Create dash.app
# ==============================================================


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX, PathIndex.FONT_AWESOME.value])
app.title = 'Conkit-Web'
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
    return utils.toggle_input_cards(*args)


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
    return utils.toggle_extra_cards(*args)


@app.callback([Output("format-selection-card", "color"),
               Output('upload-contact-map', 'disabled')],
              [Input("contact-format-select", "value")])
def toggle_format_alert(format_selection):
    if format_selection is not None:
        return None, False
    else:
        return 'danger', True


@app.callback([Output("contact-map-invalid-collapse", "is_open"),
               Output("contact-map-filename-alert", "is_open"),
               Output('contact-map-filename-alert', 'children'),
               Output('contact-map-upload-head', 'color')],
              [Input('upload-contact-map', 'filename')],
              [State('upload-contact-map', 'contents'),
               State("contact-format-select", "value"),
               State('session-id', 'children')])
def upload_contact_map(*args):
    return upload_dataset(DatasetReference.CONTACT_MAP, *args)


@app.callback([Output("sequence-invalid-collapse", "is_open"),
               Output("sequence-filename-alert", "is_open"),
               Output('sequence-filename-alert', 'children'),
               Output('sequence-upload-head', 'color')],
              [Input('upload-sequence', 'filename')],
              [State('upload-sequence', 'contents'),
               State('session-id', 'children')])
def upload_sequence(*args):
    return upload_dataset(DatasetReference.SEQUENCE, *args)


@app.callback([Output("membranetopology-invalid-collapse", "is_open"),
               Output("membranetopology-filename-alert", "is_open"),
               Output('membranetopology-filename-alert', 'children'),
               Output('membranetopology-upload-head', 'color')],
              [Input('upload-membranetopology', 'filename')],
              [State('upload-membranetopology', 'contents'),
               State('session-id', 'children')])
def upload_membranetopology(*args):
    args = list(args)
    args.insert(2, 'TOPCONS')
    return upload_dataset(DatasetReference.MEMBRANE_TOPOLOGY, *args)


@app.callback([Output("secondarystructure-invalid-collapse", "is_open"),
               Output("secondarystructure-filename-alert", "is_open"),
               Output('secondarystructure-filename-alert', 'children'),
               Output('secondarystructure-upload-head', 'color')],
              [Input('upload-secondarystructure', 'filename')],
              [State('upload-secondarystructure', 'contents'),
               State('session-id', 'children')])
def upload_secondarystructure(*args):
    args = list(args)
    args.insert(2, 'PSIPRED')
    return upload_dataset(DatasetReference.SECONDARY_STRUCTURE, *args)


@app.callback([Output("disorder-invalid-collapse", "is_open"),
               Output("disorder-filename-alert", "is_open"),
               Output('disorder-filename-alert', 'children'),
               Output('disorder-upload-head', 'color')],
              [Input('upload-disorder', 'filename')],
              [State('upload-disorder', 'contents'),
               State('session-id', 'children')])
def upload_disorder(*args):
    args = list(args)
    args.insert(2, 'IUPRED')
    return upload_dataset(DatasetReference.DISORDER, *args)


@app.callback([Output("conservation-invalid-collapse", "is_open"),
               Output("conservation-filename-alert", "is_open"),
               Output('conservation-filename-alert', 'children'),
               Output('conservation-upload-head', 'color')],
              [Input('upload-conservation', 'filename')],
              [State('upload-conservation', 'contents'),
               State('session-id', 'children')])
def upload_conservation(*args):
    args = list(args)
    args.insert(2, 'CONSURF')
    return upload_dataset(DatasetReference.CONSERVATION, *args)


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
    session_id = args.pop(-1)
    compressed_session = cache.get(session_id)
    session = decompress_session(compressed_session)
    prop_id = callback_context.triggered[0]['prop_id']
    value = callback_context.triggered[0]['value']

    if session is None or prop_id == '.' or value is None or value:
        return no_update
    else:
        dataset = prop_id.split('-')[0]
        del session[dataset]

    compressed_session = compress_session(session)
    cache.set(session_id, compressed_session)
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
    session_id = args[-1]
    factor = args[-2]
    active_tracks = args[-3]
    compressed_session = cache.get(session_id)
    session = decompress_session(compressed_session)
    trigger = callback_context.triggered

    return utils.create_plot(session, trigger, factor, active_tracks)


# ==============================================================
# Start server
# ==============================================================


if __name__ == '__main__':
    app.run_server(debug=True)
