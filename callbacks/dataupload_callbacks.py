from dash.dependencies import Input, Output, State
from app import app, cache
from dash.dash import no_update
from dash import callback_context
from components import PlotPlaceHolder
from core import Plot
import dash_core_components as dcc
from index import DatasetReference, ContextReference
from utils import remove_file, store_dataset, is_valid_trigger


@app.callback([Output('contact-map-upload-collapse', 'is_open'),
               Output('sequence-upload-collapse', 'is_open'),
               Output('mem-upload-collapse', 'is_open'),
               Output('display-control-collapse', 'is_open')],
              [Input('contact-map-upload-head', 'n_clicks'),
               Input('sequence-upload-head', 'n_clicks'),
               Input('mem-upload-head', 'n_clicks'),
               Input('display-control-head', 'n_clicks')],
              [State('sequence-upload-collapse', 'is_open'),
               State('contact-map-upload-collapse', 'is_open'),
               State('mem-upload-collapse', 'is_open'),
               State('display-control-collapse', 'is_open')])
def toggle(contact_click, sequence_click, mem_click, display_click, sequence_open, contact_open, mem_open, display_open):
    context = callback_context.triggered[0]
    prop_id = context['prop_id']

    if prop_id == '.':
        return False, False, False, False
    elif prop_id == ContextReference.CONTACT_HEAD_CLICK.value:
        return not contact_open, False, False, False
    elif prop_id == ContextReference.MEM_HEAD_CLICK.value:
        return False, False, not mem_open, False
    elif prop_id == ContextReference.DISPLAYHEAD_CLICK.value:
        return False, False, False, not display_open
    else:
        return False, not sequence_open, False, False


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
    if not is_valid_trigger(callback_context.triggered):
        return [no_update for x in range(0, 7)]

    session = cache.get('session-{}'.format(session_id))
    if session is None:
        return [no_update for x in range(0, 7)]

    return store_dataset(DatasetReference.CONTACT_MAP.value, session, cmap_text, file_contents, filename, cmap_format)


@app.callback([Output("fasta-text-area", "valid"),
               Output("fasta-text-area", "invalid"),
               Output("fasta-invalid-collapse", "is_open"),
               Output("fasta-filename-alert", "is_open"),
               Output('fasta-filename-alert', 'children'),
               Output('sequence-upload-head', 'color')],
              [Input('upload-fasta', 'filename'),
               Input("fasta-text-area", "value")],
              [State('upload-fasta', 'contents'),
               State('session-id', 'children')])
def upload_sequence(filename, fasta_text, file_contents, session_id):
    if not is_valid_trigger(callback_context.triggered):
        return [no_update for x in range(0, 6)]

    session = cache.get('session-{}'.format(session_id))
    if session is None:
        return [no_update for x in range(0, 6)]

    return store_dataset(DatasetReference.SEQUENCE.value, session, fasta_text, file_contents, filename)


@app.callback([Output("mem-text-area", "valid"),
               Output("mem-text-area", "invalid"),
               Output("mem-invalid-collapse", "is_open"),
               Output("mem-filename-alert", "is_open"),
               Output('mem-filename-alert', 'children'),
               Output('mem-upload-head', 'color')],
              [Input('upload-mem', 'filename'),
               Input("mem-text-area", "value")],
              [State('upload-mem', 'contents'),
               State('session-id', 'children')])
def upload_membranetopology(filename, mem_text, file_contents, session_id):
    if not is_valid_trigger(callback_context.triggered):
        return [no_update for x in range(0, 6)]

    session = cache.get('session-{}'.format(session_id))
    if session is None:
        return [no_update for x in range(0, 6)]

    return store_dataset(DatasetReference.MEMBRANE_TOPOLOGY.value, session, mem_text, file_contents, filename,
                         'TOPCONS')


@app.callback([Output('plot-div', 'children'),
               Output('modal-div', 'children')],
              [Input('plot-button', 'n_clicks')],
              [State('session-id', 'children')])
def create_plot(n_clicks, session_id):
    trigger = callback_context.triggered
    if not is_valid_trigger(trigger):
        return PlotPlaceHolder(), None

    session = cache.get('session-{}'.format(session_id))

    if session is None:
        return PlotPlaceHolder(), None

    error = session.lookup_input_errors()
    if error is not None:
        return PlotPlaceHolder(), error
    else:
        plot = Plot(cmap=session.contact_loader.cmap, mem_pred=session.membrtopo_loader.prediction)
        return dcc.Graph(id='plot-graph', style={'height': '80vh'}, figure=plot.get_figure()), None


@app.callback([Output('_hidden-div', 'children')],
              [Input("contact-map-filename-alert", "is_open"),
               Input("fasta-filename-alert", "is_open"),
               Input("mem-filename-alert", "is_open")],
              [State('session-id', 'children')])
def remove_file(contact_fname_open, fasta_fname_open, mem_fname_open, session_id):
    session = cache.get('session-{}'.format(session_id))
    context = callback_context.triggered[0]
    prop_id = context['prop_id']
    value = context['value']

    if session is None or prop_id == '.' or value is None or value is True:
        return no_update

    if prop_id == ContextReference.CMAP_ALERT_OPEN.value and session.contact_loader.valid_file and not contact_fname_open:
        session.contact_loader.clear()
        cache.set('session-{}'.format(session_id), session)
        return no_update

    elif prop_id == ContextReference.FASTA_ALERT_OPEN.value and session.sequence_loader.valid_file and not fasta_fname_open:
        session.sequence_loader.clear()
        cache.set('session-{}'.format(session_id), session)
        return no_update

    elif prop_id == ContextReference.MEM_ALERT_OPEN.value and session.membrtopo_loader.valid_file and not mem_fname_open:
        session.membrtopo_loader.clear()
        cache.set('session-{}'.format(session_id), session)
        return no_update

    else:
        return no_update
