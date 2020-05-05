import dash_html_components as html
from utils import PathIndex


def PlotPlaceHolder():
    return html.Div([
        html.Img(
            src=PathIndex.CONKIT_LOGO.value,
            style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto', 'vertical-align': 'middle',
                   'position': 'absolute', 'top': '0', 'bottom': '0', 'margin': 'auto', 'left': '0', 'right': '0'}
        )
    ], className='square-content')
