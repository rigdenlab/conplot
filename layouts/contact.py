import dash_html_components as html
from components import NavBar, Header, PathIndex
import dash_bootstrap_components as dbc


def Body():
    return html.Div(
        [
            html.Br(),
            html.H1('Contact form'),
            html.H6(["Please fill in the form with a description of the problem or the inquiry"]),
            html.Br(),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon("@", addon_type="prepend"),
                    dbc.Input(placeholder="Email address"),
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
                        options=[
                            {"label": "Bug report", "value": 1},
                            {"label": "General inquiry", "value": 2},
                        ]
                    ),
                    dbc.InputGroupAddon("Subject", addon_type="append"),
                ]
            ),
            html.Br(),
            html.Br(),
            dbc.Button("Send", color="primary", block=True)
        ]
    )


def Contact(session_id):
    return html.Div([
        Header(),
        NavBar(PathIndex.CONTACT.value),
        Body(),
    ])
