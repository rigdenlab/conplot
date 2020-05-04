from utils import PathIndex
from layouts import noPage, Home, DataUpload, Contact
from dash import callback_context
from layouts import ContextReference


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


def ensure_triggered(trigger):
    context = trigger[0]
    prop_id = context['prop_id']
    value = context['value']
    if prop_id == '.' or value is None:
        return False
    else:
        return True


def toggle_alert(value):
    if value is not None and value == '1':
        return True
    else:
        return False


def display_page(url, session_id):
    if url == PathIndex.HOME.value or url == PathIndex.ROOT.value:
        return Home(session_id)
    elif url == PathIndex.CONTACT.value:
        return Contact(session_id)
    elif url == PathIndex.PLOT.value:
        return DataUpload(session_id)
    else:
        return noPage(url)
