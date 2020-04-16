import dash_html_components as html
from components import NavBar, Header, PathIndex


def Body():
    return html.Div(
        [
            html.Br(),
            html.H1(["Welcome to Conkit-Web"]),
            html.H6(["This is a place holder"]),
        ]
    )


def Home():
    return html.Div([
        Header(),
        NavBar(PathIndex.HOME.value),
        Body(),
    ])
