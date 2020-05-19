from utils import UrlIndex
import dash_html_components as html
from components import NavBar, Header
import dash_bootstrap_components as dbc


def Body():
    return html.Div(
        [
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Container([
                dbc.Card([
                    dbc.CardBody([
                        html.H1('Conplot help page', className="card-text", style={'text-align': "center"}),
                        html.Br(),
                        html.Br(),
                    ])
                ])
            ]),
        ]
    )


def Help(session_id, username):
    return html.Div([
        Header(username),
        NavBar(UrlIndex.HELP.value),
        Body(),
    ])
