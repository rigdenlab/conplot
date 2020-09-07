import dash_html_components as html
import dash_bootstrap_components as dbc
from components import NavBar, Header, UserLoginCard, UserStoredSessionsCard, UserSharedSessionsCard


def Body(username=None, current_session_pkid=None):
    if username is None:
        return html.Div([
            html.Br(),
            html.Br(),
            dbc.Container(UserLoginCard())
        ])
    else:
        return html.Div([
            html.Div(id='session-storage-toast-div'),
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Container(UserStoredSessionsCard(username, current_session_pkid)),
            html.Br(),
            html.Br(),
            dbc.Container(UserSharedSessionsCard(username, current_session_pkid))
        ])


def UserStorage(username=None, current_session_pkid=None):
    return html.Div([
        Header(username),
        NavBar(),
        Body(username, current_session_pkid)
    ])
