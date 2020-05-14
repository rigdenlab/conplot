from utils import UrlIndex
import dash_html_components as html
from components import NavBar, Header
import dash_bootstrap_components as dbc


def Body():
    return html.Div(
        [
            html.Br(),
            html.Br(),
            dbc.Container([
                dbc.Card([
                    dbc.CardBody([
                        html.H1('Contact form', className="card-text", style={'text-align': "center"}),
                        html.Br(),
                        html.H6("Please fill in the form with a description of the problem or the inquiry",
                                className="card-text", style={'text-align': "center"}),
                        html.Hr(),
                        html.Br(),
                        dbc.InputGroup(
                            [
                                dbc.InputGroupAddon("@", addon_type="prepend"),
                                dbc.Input(placeholder="Email address", type="email"),
                            ],
                            className="mb-3",
                        ),
                        dbc.InputGroup(
                            [
                                dbc.Input(placeholder="First Name"),
                            ],
                            className="mb-3",
                        ),
                        dbc.InputGroup(
                            [
                                dbc.InputGroupAddon("Description", addon_type="prepend"),
                                dbc.Textarea(),
                            ],
                            className="mb-3",
                        ),
                        dbc.InputGroup(
                            [
                                dbc.Select(
                                    id='issue-select',
                                    options=[
                                        {"label": "Bug report", "value": 1},
                                        {"label": "General inquiry", "value": 2},
                                    ]
                                ),
                                dbc.InputGroupAddon("Subject", addon_type="append"),
                            ]
                        ),
                        html.Br(),
                        dbc.Alert([
                            html.H4('Info', className="alert-heading"),
                            html.P([
                                "If you suspect a bug, you can also create an issue on the project's ",
                                html.A("Github repository", href=UrlIndex.GITHUB.value, className="alert-link")
                            ]),
                        ],
                            dismissable=True,
                            color='danger',
                            fade=True,
                            is_open=False,
                            id='bug-alert'
                        ),
                        dbc.Button("Send", color="primary", block=True)
                    ])
                ])
            ]),
        ]
    )


def Contact(session_id):
    return html.Div([
        Header(),
        NavBar(UrlIndex.CONTACT.value),
        Body(),
    ])
