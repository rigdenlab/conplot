from dash.dependencies import Input, Output, State
from app import app, cache
from dash.dash import no_update
from dash import callback_context
from components import PlotPlaceHolder
from core import Plot
import dash_core_components as dcc
from index import UploadInterfaceComponentIndex, TableCollapseInterfaceIndex, ContextReference, InputReference, \
    OutputReference


@app.callback(TableCollapseInterfaceIndex.OUTPUT.value,
              TableCollapseInterfaceIndex.INPUT.value,
              TableCollapseInterfaceIndex.STATE.value)
def toggle(contact_click, sequence_click, mem_click, sequence_open, contact_open, mem_open):
    context = callback_context.triggered[0]
    prop_id = context['prop_id']

    if prop_id == '.':
        return False, False, False
    elif prop_id == ContextReference.CONTACT_HEAD_CLICK.value:
        return not contact_open, False, False
    elif prop_id == ContextReference.MEM_HEAD_CLICK.value:
        return False, False, not mem_open
    else:
        return False, not sequence_open, False


@app.callback(UploadInterfaceComponentIndex.OUTPUT.value,
              UploadInterfaceComponentIndex.INPUT.value,
              UploadInterfaceComponentIndex.STATE.value)
def user_input(*args):
    session = cache.get('session-{}'.format(args[InputReference.SESSION_ID.value]))
    context = callback_context.triggered[0]
    prop_id = context['prop_id']
    value = context['value']
    layout_states = [no_update for x in UploadInterfaceComponentIndex.OUTPUT.value]

    if session is None or prop_id == '.' or value is None:
        pass

    elif prop_id == ContextReference.CMAP_FORMAT_SELECT.value or prop_id == ContextReference.CMAP_TEXT_VALUE.value or prop_id == ContextReference.UPLOAD_CMAP_FNAME.value:
        session.contact_loader.register_input(
            args[InputReference.CMAP_TEXT_VALUE.value],
            args[InputReference.UPLOAD_CMAP_FCONTENTS.value],
            args[InputReference.UPLOAD_CMAP_FNAME.value],
            args[InputReference.CMAP_FORMAT_SELECT.value]
        )
        session.contact_loader.load()
        cache.set('session-{}'.format(args[InputReference.SESSION_ID.value]), session)
        layout_states[OutputReference.CMAP_TEXT_VALID.value] = session.contact_loader.valid_text
        layout_states[OutputReference.CMAP_TEXT_INVALID.value] = session.contact_loader.invalid_text
        layout_states[OutputReference.CMAP_INVALID_COLLAPSE_OPEN.value] = session.contact_loader.invalid
        layout_states[OutputReference.CMAP_FNAME_ALERT_OPEN.value] = session.contact_loader.valid_file
        layout_states[OutputReference.CMAP_FNAME.value] = session.contact_loader.filename
        layout_states[OutputReference.CMAP_FORMAT_SELECT_COLOR.value] = session.contact_loader.format_select_color
        layout_states[OutputReference.CMAP_HEAD_COLOR.value] = session.contact_loader.head_color

    elif prop_id == ContextReference.FASTA_TEXT_VALUE.value or prop_id == ContextReference.UPLOAD_FASTA_FNAME.value:
        session.sequence_loader.register_input(
            args[InputReference.FASTA_TEXT_VALUE.value],
            args[InputReference.UPLOAD_FASTA_FCONTENTS.value],
            args[InputReference.UPLOAD_FASTA_FNAME.value]
        )
        session.sequence_loader.load()
        cache.set('session-{}'.format(args[InputReference.SESSION_ID.value]), session)
        layout_states[OutputReference.FASTA_TEXT_VALID.value] = session.sequence_loader.valid_text
        layout_states[OutputReference.FASTA_TEXT_INVALID.value] = session.sequence_loader.invalid_text
        layout_states[OutputReference.FASTA_INVALID_COLLAPSE_OPEN.value] = session.sequence_loader.invalid
        layout_states[OutputReference.FASTA_FNAME_ALERT_OPEN.value] = session.sequence_loader.valid_file
        layout_states[OutputReference.FASTA_FNAME.value] = session.sequence_loader.filename
        layout_states[OutputReference.SEQ_HEAD_COLOR.value] = session.sequence_loader.head_color

    elif prop_id == ContextReference.MEM_TEXT_VALUE.value or prop_id == ContextReference.UPLOAD_MEM_FNAME.value:
        session.membrtopo_loader.register_input(
            args[InputReference.MEM_TEXT_VALUE.value],
            args[InputReference.UPLOAD_MEM_FCONTENTS.value],
            args[InputReference.UPLOAD_MEM_FNAME.value],
            input_format='TOPCONS'
        )
        session.membrtopo_loader.load()
        cache.set('session-{}'.format(args[InputReference.SESSION_ID.value]), session)
        layout_states[OutputReference.MEM_TEXT_VALID.value] = session.membrtopo_loader.valid_text
        layout_states[OutputReference.MEM_TEXT_INVALID.value] = session.membrtopo_loader.invalid_text
        layout_states[OutputReference.MEM_INVALID_COLLAPSE_OPEN.value] = session.membrtopo_loader.invalid
        layout_states[OutputReference.MEM_FNAME_ALERT_OPEN.value] = session.membrtopo_loader.valid_file
        layout_states[OutputReference.MEM_FNAME.value] = session.membrtopo_loader.filename
        layout_states[OutputReference.MEM_HEAD_COLOR.value] = session.membrtopo_loader.head_color

    elif prop_id == ContextReference.PLOT_CLICK.value:
        error = session.lookup_input_errors()
        if error is not None:
            layout_states[OutputReference.PLOT_DIV.value] = PlotPlaceHolder()
            layout_states[OutputReference.MODAL_DIV.value] = error
        else:
            plot = Plot(cmap=session.contact_loader.cmap, mem_pred=session.membrtopo_loader.prediction)
            layout_states[OutputReference.PLOT_DIV.value] = dcc.Graph(id='plot-graph', style={'height': '80vh'},
                                                                      figure=plot.get_figure())
            layout_states[OutputReference.MODAL_DIV.value] = None

    return layout_states


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
