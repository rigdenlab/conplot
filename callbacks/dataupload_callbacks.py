from dash.dash import no_update
from dash import callback_context
from components import PlotPlaceHolder, DisplayControlCard
from core import Plot
import dash_core_components as dcc
from loaders import DatasetReference
from layouts import ContextReference
from callbacks import ensure_triggered


def store_dataset(dataset, session, *args):
    session.__getattribute__('{}_loader'.format(dataset)).register_input(*args)
    session.__getattribute__('{}_loader'.format(dataset)).load()
    return session.__getattribute__('{}_loader'.format(dataset)).layout_states


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


def upload_contact_map(filename, cmap_text, cmap_format, file_contents, session):
    if not ensure_triggered(callback_context.triggered):
        return [no_update for x in range(0, 7)]

    if session is None:
        return [no_update for x in range(0, 7)]

    return store_dataset(DatasetReference.CONTACT_MAP.value, session, cmap_text, file_contents, filename, cmap_format)


def upload_sequence(filename, sequence_text, file_contents, session):
    if not ensure_triggered(callback_context.triggered):
        return [no_update for x in range(0, 6)]

    if session is None:
        return [no_update for x in range(0, 6)]

    return store_dataset(DatasetReference.SEQUENCE.value, session, sequence_text, file_contents, filename)


def upload_membranetopology(filename, mem_text, file_contents, session):
    if not ensure_triggered(callback_context.triggered):
        return [no_update for x in range(0, 6)]

    if session is None:
        return [no_update for x in range(0, 6)]

    return store_dataset(DatasetReference.MEMBRANE_TOPOLOGY.value, session, mem_text, file_contents, filename,
                         'TOPCONS')


def upload_secondarystructure(filename, ss_text, file_contents, session):
    if not ensure_triggered(callback_context.triggered):
        return [no_update for x in range(0, 6)]

    if session is None:
        return [no_update for x in range(0, 6)]

    return store_dataset(DatasetReference.SECONDARY_STRUCTURE.value, session, ss_text, file_contents, filename,
                         'PSIPRED')


def upload_disorder(filename, disorder_text, file_contents, session):
    if not ensure_triggered(callback_context.triggered):
        return [no_update for x in range(0, 6)]

    if session is None:
        return [no_update for x in range(0, 6)]

    return store_dataset(DatasetReference.DISORDER.value, session, disorder_text, file_contents, filename, 'IUPRED')


def upload_conservation(filename, conserv_text, file_contents, session):
    if not ensure_triggered(callback_context.triggered):
        return [no_update for x in range(0, 6)]

    if session is None:
        return [no_update for x in range(0, 6)]

    return store_dataset(DatasetReference.CONSERVATION.value, session, conserv_text, file_contents, filename, 'CONSURF')


def remove_file(*args):
    session = args[-1]
    context = callback_context.triggered[0]
    prop_id = context['prop_id']
    value = context['value']

    if session is None or prop_id == '.' or value is None or value is True:
        pass
    elif not value:
        dataset = prop_id.split('-')[0]
        if session.__getattribute__('{}_loader'.format(dataset)).valid_file:
            session.__getattribute__('{}_loader'.format(dataset)).clear()

    return session


def create_plot(*args):
    trigger = callback_context.triggered
    if not ensure_triggered(trigger):
        return PlotPlaceHolder(), None, DisplayControlCard()

    session = args[-1]
    if session is None:
        return PlotPlaceHolder(), None, DisplayControlCard()

    error = session.lookup_input_errors()
    if error is not None:
        return PlotPlaceHolder(), error, DisplayControlCard()
    elif trigger[0]['prop_id'] == ContextReference.PLOT_CLICK.value:
        plot = Plot(session)
        return dcc.Graph(id='plot-graph', style={'height': '80vh'}, figure=plot.get_figure()), None, DisplayControlCard(
            available_tracks=plot.active_tracks, factor=plot.factor)
    else:
        plot = Plot(session)
        plot.factor = args[-2]
        plot.active_tracks = args[-3]
        return dcc.Graph(id='plot-graph', style={'height': '80vh'}, figure=plot.get_figure()), None, no_update
