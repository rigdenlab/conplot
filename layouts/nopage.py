import dash_html_components as html
import dash_bootstrap_components as dbc
from components import NavBar, ErrorAlert, Header


def noPage(url):
    layout = html.Div([
        Header(),
        NavBar(),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Container([
            dbc.Card([
                dbc.CardBody([
                    html.H2('Something went wrong...', className="card-text", style={'text-align': "center"}),
                    html.Hr(),
                    html.Br(),
                    html.P(["404 Page not found: {}".format(url)]),
                    html.Br(),
                    ErrorAlert(True)

                ])
            ])
        ]),
    ],
        className="no-page"
    )
    return layout
