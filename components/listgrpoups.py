from components import ShareWithInput, SessionListType
import dash_bootstrap_components as dbc
import dash_html_components as html
from utils import sql_utils


def SessionListItem(session, list_type, color='secondary'):
    if list_type == SessionListType.SHARED:
        button_group = dbc.ButtonGroup([
            dbc.Button(html.I(className="fas fa-save"), outline=True, color='primary',
                       id={'type': 'load-share-session-button', 'index': session.pkid}),
            dbc.Button(html.I(className="fas fa-ban"), outline=True, color='danger', className="ml-1",
                       id={'type': 'stop-share-session-button', 'index': session.pkid})
        ], className="btn-toolbar")
        session_label = "%s - %s" % (session.owner, session.name)
    elif list_type == SessionListType.TO_SHARE:
        button_group = dbc.ButtonGroup([
            html.Div(id={'type': 'share-session-toast-div', 'index': session.pkid}),
            ShareWithInput(id={'type': 'share-username-input', 'index': session.pkid}),
            dbc.Button(html.I(className="fas fa-share-alt"), outline=True, color='primary', size='sm',
                       id={'type': 'share-session-button', 'index': session.pkid}),
        ], className="btn-toolbar")
        session_label = session.name
    else:
        button_group = dbc.ButtonGroup([
            dbc.Button(html.I(className="fas fa-save"), outline=True, color='primary',
                       id={'type': 'load-session-button', 'index': session.pkid}),
            dbc.Button(html.I(className="fas fa-trash-alt"), outline=True, color='danger', className="ml-1",
                       id={'type': 'delete-session-button', 'index': session.pkid})
        ], className="btn-toolbar")
        session_label = session.name

    return dbc.ListGroupItem([
        dbc.Row([
            dbc.Col([
                html.H5(session_label, style={'vertical-align': 'middle', 'margin': 'auto'})
            ], style={'align-items': 'center', 'justify-content': 'center', 'display': 'flex'}),
            dbc.Col([
                html.H5(session.date, style={'vertical-align': 'middle', 'margin': 'auto'})
            ], style={'align-items': 'center', 'justify-content': 'center', 'display': 'flex'}),
            dbc.Col(button_group, width=5)
        ], align='between')

    ], color=color)


def EmptyListItem():
    return dbc.ListGroupItem(
        dbc.Row(
            dbc.Col(
                html.H5('No sessions have been found!', style={'vertical-align': 'middle', 'margin': 'auto'}),
                style={'align-items': 'center', 'justify-content': 'center', 'display': 'flex'})
        )
    )


def SessionList(username, list_type, selected_session_pkid=None):
    list_items = []
    all_sessions = sql_utils.list_sessions(username, list_type)

    for session in all_sessions:
        if selected_session_pkid is not None and session.pkid == int(selected_session_pkid):
            color = 'success'
        else:
            color = None
        list_items.append(SessionListItem(session, list_type, color))

    if not list_items:
        return dbc.ListGroup(EmptyListItem())

    return dbc.ListGroup(list_items)
