import dash_html_components as html
import dash_bootstrap_components as dbc
from components import NavBar, Header, UserPortalCard


def UsersPortal(username=None):
    return html.Div([
        Header(username),
        NavBar(),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Container(UserPortalCard(username)),
    ])
