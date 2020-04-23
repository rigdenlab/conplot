import dash_html_components as html
from components import NavBar, ErrorAlert, Header


def noPage():
    layout = html.Div([
        Header(),
        NavBar(),
        html.Br(),
        html.H2('Something went wrong...'),
        html.Hr(),
        html.P(["404 Page not found"]),
        html.Br(),
        html.Br(),
        ErrorAlert(True)
    ],
        className="no-page"
    )
    return layout
