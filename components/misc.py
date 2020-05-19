import dash_html_components as html
from utils import UrlIndex


def PlotPlaceHolder():
    return html.Div([
        html.Img(
            src=UrlIndex.CONPLOT_LOGO.value,
            style={'display': 'block', 'vertical-align': 'middle', 'margin': 'auto', 'position': 'absolute',
                   'top': '0', 'bottom': '0', 'left': '0', 'right': '0'}
        )
    ], className='square-content')
