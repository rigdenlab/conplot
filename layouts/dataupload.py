import dash_html_components as html
from components import NavBar, Header, PathIndex, FastaUploadCard, ContactUploadCard
import dash_bootstrap_components as dbc
from callbacks import dataupload_callbacks


def DataUpload(session_id):
    return html.Div([
        Header(),
        NavBar(PathIndex.PLOT.value),
        html.Div(
            [
                html.Br(),
                html.H1('Data Upload'),
                html.H6(["Please upload the files of interest or paste their contents"]),
                html.Br(),
                dbc.CardDeck(
                    [
                        FastaUploadCard(),
                        ContactUploadCard()
                    ]
                ),
                html.Br(),
                html.Br(),
                dbc.Collapse([
                    dbc.Alert([
                        html.H4("Missing Inputs", className="alert-heading"),
                        html.P(
                            "Please ensure you fill in all required fields before trying to generate a plot. "
                            "We detected problems on the following fields:"
                        ),
                        html.Hr(),
                        html.Div(id='missing-fields-div'),
                    ], color='danger')
                ], id='missing-fields-collapse'),
                html.Br(),
                dbc.Button('Plot', id='plot-button', color="primary", block=True),
            ]
        )
    ])
