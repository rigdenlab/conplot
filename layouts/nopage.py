import dash_html_components as html
import dash_bootstrap_components as dbc
from components import NavBar, Header, NoPageFoundCard


def noPage(url, username):
    layout = html.Div([
        Header(username),
        NavBar(),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Container(NoPageFoundCard(url)),
    ], className="no-page")
    return layout
