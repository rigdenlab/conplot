from utils import UrlIndex
import dash_html_components as html
from components import NavBar, Header, SessionTimedOutModal
import dash_bootstrap_components as dbc


def Body():
    return html.Div(
        [
            SessionTimedOutModal(),
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Container([
                dbc.Card([
                    dbc.CardBody([
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.H1('Session Timed out!', className="card-text",
                                style={'text-align': "center", 'color': 'red'}),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Div(html.I(className="fas fa-user-clock fa-3x", style={'color': 'red'}),
                                 style={'text-align': "center"}),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br()
                    ])
                ])
            ]),
        ]
    )


def SessionTimeout(session_id):
    return html.Div([
        Header(),
        NavBar(UrlIndex.SESSION_TIMEOUT.value),
        Body(),
    ])
