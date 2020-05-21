import dash_bootstrap_components as dbc
import dash_html_components as html
from utils import sql_utils


def SessionListItem(session_name, session_date, color='secondary'):
    return dbc.ListGroupItem([
        dbc.Row([
            dbc.Col([
                html.H5(session_name, style={'vertical-align': 'middle', 'margin': 'auto'})
            ], style={'align-items': 'center', 'justify-content': 'center', 'display': 'flex'}),
            dbc.Col([
                html.H5(session_date, style={'vertical-align': 'middle', 'margin': 'auto'})
            ], style={'align-items': 'center', 'justify-content': 'center', 'display': 'flex'}),
            dbc.Col([
                dbc.ButtonGroup([
                    dbc.Button(html.I(className="fas fa-save"), outline=True, color='primary',
                               id={'type': 'load-session-button', 'index': session_name}),
                    dbc.Button(html.I(className="fas fa-trash-alt"), outline=True, color='danger', className="ml-1",
                               id={'type': 'delete-session-button', 'index': session_name}),
                    dbc.Button(html.I(className="fas fa-share-alt"), outline=True, color='primary', className="ml-1",
                               id={'type': 'share-session-button', 'index': session_name})
                ], className="btn-toolbar")
            ], width=5)
        ], align='between')

    ], color=color)


def SharedSessionListItem(session_owner, session_name, session_date, color='secondary'):
    return dbc.ListGroupItem([
        dbc.Row([
            dbc.Col([
                html.H5("%s - %s" % (session_owner, session_name), style={'vertical-align': 'middle', 'margin': 'auto'})
            ], style={'align-items': 'center', 'justify-content': 'center', 'display': 'flex'}),
            dbc.Col([
                html.H5(session_date, style={'vertical-align': 'middle', 'margin': 'auto'})
            ], style={'align-items': 'center', 'justify-content': 'center', 'display': 'flex'}),
            dbc.Col([
                dbc.ButtonGroup([
                    dbc.Button(html.I(className="fas fa-save"), outline=True, color='primary',
                               id={'type': 'load-share-session-button', 'index': session_name}),
                    dbc.Button(html.I(className="fas fa-ban"), outline=True, color='danger', className="ml-1",
                               id={'type': 'stop-share-session-button', 'index': session_name})
                ], className="btn-toolbar")
            ])
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


def StoredSessionsList(username, selected_session_pkid=None):
    list_items = []
    user_sessions = sql_utils.list_all_sessions(username)
    for session in user_sessions:
        if selected_session_pkid is not None and session[2] == selected_session_pkid:
            color = 'success'
        else:
            color = None
        list_items.append(SessionListItem(session[0], session[1], color))

    if not list_items:
        return dbc.ListGroup(EmptyListItem())

    return dbc.ListGroup(list_items)


def SharedSessionsList(username, selected_session_pkid=None):
    list_items = []
    shared_sessions = sql_utils.get_shared_sessions(username)
    for session in shared_sessions:
        if selected_session_pkid is not None and session[-1] == selected_session_pkid:
            color = 'success'
        else:
            color = None
        list_items.append(SharedSessionListItem(session[0], session[1], session[2], color))

    if not list_items:
        return dbc.ListGroup(EmptyListItem())

    return dbc.ListGroup(list_items)
