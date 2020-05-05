import dash_html_components as html
from utils import PathIndex


def PlotPlaceHolder():
    return html.Div([
        html.Img(
            src=PathIndex.CONKIT_LOGO.value,
            style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}
        )
    ], className='square-content')
