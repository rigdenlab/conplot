import dash_html_components as html
import dash_bootstrap_components as dbc
from components import NavBar, Header, NoPageFoundCard


def noPage(url):
    layout = html.Div([
        Header(),
        NavBar(),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Container(NoPageFoundCard(url)),
    ], className="no-page")
    return layout
