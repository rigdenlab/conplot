from components import NavBar, Header, EmailInput, EmailIssueSelect, ProblemDescriptionInput, NameInput, Footer
import dash_html_components as html
import dash_bootstrap_components as dbc
from utils import UrlIndex


def Body():
    return html.Div(
        [
            dbc.Spinner(html.Div(id='contact-form-modal-div'), fullscreen=True),
            html.Br(),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H3('Contact form', className="card-text", style={'text-align': "center"}),
                            html.Br(),
                            html.H6("Please fill in the form with a description of the problem or the inquiry",
                                    className="card-text", style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            NameInput(),
                            EmailInput(id='contact-email-input'),
                            ProblemDescriptionInput(),
                            EmailIssueSelect(),
                            html.Br(),
                            html.Div(id='contact-alert-div'),
                            dbc.Button("Send", color="primary", block=True, disabled=True,
                                       id='submit-contact-form-button')
                        ])
                    ])
                ], width=10),
            ], justify='center', align='center', className='m-0')
        ]
    )


def Contact(session_id, username):
    return html.Div([
        Header(username),
        NavBar(UrlIndex.CONTACT.value),
        Body(),
        Footer(True)
    ])
