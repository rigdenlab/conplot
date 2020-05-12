from utils import PathIndex
import dash_html_components as html
from components import NavBar, Header


def Body(session_id):
    return html.Div(
        [
            html.Br(),
            html.H1(["Welcome to ConPlot"]),
            html.H6(["Current session id is %s" % session_id]),
        ]
    )


def Home(session_id):
    return html.Div([
        Header(),
        NavBar(PathIndex.HOME.value),
        Body(session_id),
    ])
