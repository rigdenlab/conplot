import dash_html_components as html
import dash_bootstrap_components as dbc
from components import NavBar, Header, UserLoginCard, UserLogoutCard


def UsersPortal(username=None):
    if username is None:
        card = UserLoginCard()
    else:
        card = UserLogoutCard(username)

    return html.Div([
        Header(username),
        NavBar(),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Container(card),
    ])
