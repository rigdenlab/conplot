import dash_html_components as html
import dash_bootstrap_components as dbc
from components import NavBar, Header, UserLoginCard, UserStoredSessions


def UserStorage(username=None, current_session_name=None):
    if username is None:
        card = UserLoginCard()
    else:
        card = UserStoredSessions(username, current_session_name)

    return html.Div([
        Header(username),
        NavBar(),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Container(card),
    ])
