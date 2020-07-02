import dash_html_components as html
import dash_bootstrap_components as dbc
from components import NavBar, Header, UserLoginCard, ShareSessionsCard


def Body(username=None):
    if username is None:
        return html.Div([
            html.Br(),
            html.Br(),
            dbc.Container(UserLoginCard(True))
        ])
    else:
        return html.Div([
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Container(ShareSessionsCard(username), id='share-session-container')
        ])


def ShareSession(username=None):
    return html.Div([
        Header(username),
        NavBar(),
        Body(username)
    ])
