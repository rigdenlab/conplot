from dash.dependencies import Input, Output, State
from app import app, cache
from dash.dash import no_update
from dash import callback_context
from components import PlotPlaceHolder, DisplayControlCard
from core.plot import Plot
import dash_core_components as dcc
from index import DatasetReference, ContextReference
from utils import store_dataset, ensure_triggered


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
def toggle_input_cards(contact_click, sequence_click, mem_click, ss_click, disorder_click, conserv_click, sequence_open,
                       contact_open, mem_open, ss_open, disorder_open, conserv_open):
    context = callback_context.triggered[0]
    prop_id = context['prop_id']
    layout = [False for x in range(0, 6)]

    if prop_id == '.':
        pass
    elif prop_id == ContextReference.CONTACT_HEAD_CLICK.value:
        layout[0] = not contact_open
    elif prop_id == ContextReference.SEQUENCE_HEAD_CLICK.value:
        layout[1] = not sequence_open
    elif prop_id == ContextReference.MEM_HEAD_CLICK.value:
        layout[2] = not mem_open
    elif prop_id == ContextReference.SS_HEAD_CLICK.value:
        layout[3] = not ss_open
    elif prop_id == ContextReference.DISORDER_HEAD_CLICK.value:
        layout[4] = not disorder_open
    else:
        layout[5] = not conserv_open

    return layout


@app.callback([Output('display-control-collapse', 'is_open'),
               Output('warning-collapse', 'is_open'),
               Output('help-collapse', 'is_open')],
              [Input('display-control-head', 'n_clicks'),
               Input('warning-head', 'n_clicks'),
               Input('help-head', 'n_clicks')],
              [State('display-control-collapse', 'is_open'),
               State('warning-collapse', 'is_open'),
               State('help-collapse', 'is_open')])
def toggle_extra_cards(display_click, warning_click, help_click, display_open, warning_open, help_open):
    context = callback_context.triggered[0]
    prop_id = context['prop_id']
    layout = [False for x in range(0, 3)]

    if prop_id == '.':
        pass
    elif prop_id == ContextReference.DISPLAY_HEAD_CLICK.value:
        layout[0] = not display_open
    elif prop_id == ContextReference.WARNING_HEAD_CLICK.value:
        layout[1] = not warning_open
    elif prop_id == ContextReference.HELP_HEAD_CLICK.value:
        layout[2] = not help_open

    return layout


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
def upload_contact_map(filename, cmap_text, cmap_format, file_contents, session_id):
    if not ensure_triggered(callback_context.triggered):
        return [no_update for x in range(0, 7)]

    session = cache.get('session-{}'.format(session_id))
    if session is None:
        return [no_update for x in range(0, 7)]

    return store_dataset(DatasetReference.CONTACT_MAP.value, session, cmap_text, file_contents, filename, cmap_format)


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
def upload_sequence(filename, sequence_text, file_contents, session_id):
    if not ensure_triggered(callback_context.triggered):
        return [no_update for x in range(0, 6)]

    session = cache.get('session-{}'.format(session_id))
    if session is None:
        return [no_update for x in range(0, 6)]

    return store_dataset(DatasetReference.SEQUENCE.value, session, sequence_text, file_contents, filename)


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
def upload_membranetopology(filename, mem_text, file_contents, session_id):
    if not ensure_triggered(callback_context.triggered):
        return [no_update for x in range(0, 6)]

    session = cache.get('session-{}'.format(session_id))
    if session is None:
        return [no_update for x in range(0, 6)]

    return store_dataset(DatasetReference.MEMBRANE_TOPOLOGY.value, session, mem_text, file_contents, filename,
                         'TOPCONS')


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
def upload_secondarystructure(filename, ss_text, file_contents, session_id):
    if not ensure_triggered(callback_context.triggered):
        return [no_update for x in range(0, 6)]

    session = cache.get('session-{}'.format(session_id))
    if session is None:
        return [no_update for x in range(0, 6)]

    return store_dataset(DatasetReference.SECONDARY_STRUCTURE.value, session, ss_text, file_contents, filename,
                         'PSIPRED')


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
def upload_disorder(filename, disorder_text, file_contents, session_id):
    if not ensure_triggered(callback_context.triggered):
        return [no_update for x in range(0, 6)]

    session = cache.get('session-{}'.format(session_id))
    if session is None:
        return [no_update for x in range(0, 6)]

    return store_dataset(DatasetReference.DISORDER.value, session, disorder_text, file_contents, filename, 'IUPRED')


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
def upload_conservation(filename, conserv_text, file_contents, session_id):
    if not ensure_triggered(callback_context.triggered):
        return [no_update for x in range(0, 6)]

    session = cache.get('session-{}'.format(session_id))
    if session is None:
        return [no_update for x in range(0, 6)]

    return store_dataset(DatasetReference.CONSERVATION.value, session, conserv_text, file_contents, filename, 'CONSURF')


@app.callback([Output('_hidden-div', 'children')],
              [Input("contact-map-filename-alert", "is_open"),
               Input("sequence-filename-alert", "is_open"),
               Input("membranetopology-filename-alert", "is_open"),
               Input("secondarystructure-filename-alert", "is_open"),
               Input("disorder-filename-alert", "is_open"),
               Input("conservation-filename-alert", "is_open")],
              [State('session-id', 'children')])
def remove_file(*args):
    session = cache.get('session-{}'.format(args[-1]))
    context = callback_context.triggered[0]
    prop_id = context['prop_id']
    value = context['value']

    if session is None or prop_id == '.' or value is None or value is True:
        pass
    elif not value:
        dataset = prop_id.split('-')[0]
        if session.__getattribute__('{}_loader'.format(dataset)).valid_file:
            session.__getattribute__('{}_loader'.format(dataset)).clear()
        cache.set('session-{}'.format(args[-1]), session)

    return no_update


@app.callback([Output('plot-div', 'children'),
               Output('modal-div', 'children'),
               Output('display-control-collapse', 'children')],
              [Input('plot-button', 'n_clicks'),
               Input('refresh-button', 'n_clicks')],
              [State('track-selection-dropdown', 'value'),
               State('session-id', 'children')])
def create_plot(*args):
    trigger = callback_context.triggered
    if not ensure_triggered(trigger):
        return PlotPlaceHolder(), None, DisplayControlCard()

    session = cache.get('session-{}'.format(args[-1]))
    if session is None:
        return PlotPlaceHolder(), None, DisplayControlCard()

    error = session.lookup_input_errors()
    if error is not None:
        return PlotPlaceHolder(), error, DisplayControlCard()
    elif trigger[0]['prop_id'] == ContextReference.PLOT_CLICK.value:
        plot = Plot(session)
        return dcc.Graph(id='plot-graph', style={'height': '80vh'}, figure=plot.get_figure()), None, DisplayControlCard(
            available_tracks=plot.active_tracks)
    else:
        selected_tracks = args[-2]
        plot = Plot(session)
        plot.active_tracks = selected_tracks
        return dcc.Graph(id='plot-graph', style={'height': '80vh'}, figure=plot.get_figure()), None, no_update
