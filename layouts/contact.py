from components import NavBar, Header, ContactBugAlert, EmailInput, EmailIssueSelect, ProblemDescriptionInput, NameInput
import dash_html_components as html
import dash_bootstrap_components as dbc
from utils import UrlIndex


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
                        EmailInput(),
                        NameInput(),
                        ProblemDescriptionInput(),
                        EmailIssueSelect(),
                        html.Br(),
                        ContactBugAlert(),
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
