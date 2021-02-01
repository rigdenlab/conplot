import dash_html_components as html
import dash_bootstrap_components as dbc
from components import RecoveryPortalCard, Footer


def AccountRecoveryPortal():
    return html.Div([
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Container(RecoveryPortalCard()),
        Footer(True)
    ])
