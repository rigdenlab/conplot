import dash_html_components as html
from components import NavBar, Header, PathIndex
import dash_bootstrap_components as dbc
from components import FastaUploadCard, ContactUploadCard
from callbacks import dataupload_callbacks


def DataUpload(session_id):
    return html.Div([
        Header(),
        NavBar(PathIndex.DATAUPLOAD.value),
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
                dbc.Collapse(
                    dbc.Card(dbc.CardBody("Some required fields are misssing!")),
                    id="collapse-required-fields",
                ),
                dbc.NavLink([dbc.Button("Plot", id='plot-button', color="primary", block=True)], id='plot-navlink',
                            href=PathIndex.PLOTDISPLAY.value, disabled=True),
                html.Div(id='_cmap', style={'display': 'none'}),
                html.Div(id='_fasta', style={'display': 'none'}),
            ]
        )
    ])
