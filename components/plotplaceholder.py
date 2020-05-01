import dash_html_components as html
import dash_bootstrap_components as dbc
from core import PathIndex

def PlotPlaceHolder():
    return dbc.Jumbotron(
        [
            dbc.Container(
                [
                    html.Img(
                        src=PathIndex.CONKIT_LOGO.value,
                        style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}
                    )
                ],
                fluid=True,
            )
        ],
        fluid=True,
    )
