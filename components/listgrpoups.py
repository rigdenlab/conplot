import dash_bootstrap_components as dbc
import dash_html_components as html
from utils import sql_utils


def SessionListItem(session_name, session_date, color='secondary'):
    return dbc.ListGroupItem([
        dbc.Row([
            dbc.Col([
                html.P(session_name, style={'text-align': "center", 'vertical-align': 'middle'})
            ]),
            dbc.Col([
                html.P(session_date, style={'text-align': "center", 'vertical-align': 'middle'})
            ]),
            dbc.Col([
                dbc.ButtonGroup([
                    dbc.Button('Load session', outline=True, color='primary',
                               id={'type': 'load-session-button', 'index': session_name}),
                    dbc.Button('Delete session', outline=True, color='danger', className="ml-1",
                               id={'type': 'delete-session-button', 'index': session_name})
                ], className="btn-toolbar")
            ])
        ], align='between')

    ], color=color)


def EmptyListItem():
    return dbc.ListGroupItem('No sessions have been found!')


def StoredSessionsList(username, selected_session_name=None):
    list_items = []
    user_sessions = sql_utils.list_all_sessions(username)
    for session in user_sessions:
        if selected_session_name is not None and session[0] == selected_session_name:
            color = 'success'
        else:
            color = None
        list_items.append(SessionListItem(session[0], session[1], color))

    if not list_items:
        return dbc.ListGroup(EmptyListItem())

    return dbc.ListGroup(list_items)
