import dash_html_components as html
from components import NavBar, Header, PathIndex, FastaUploadCard, ContactUploadCard
import dash_bootstrap_components as dbc
from callbacks import dataupload_callbacks
import dash_core_components as dcc


def DataUpload(session_id):
    return html.Div([
        Header(),
        NavBar(PathIndex.PLOT.value),
        dbc.Row([
            dbc.Col([
                html.Br(),
                html.H1('Data Upload'),
                html.H6(["Please upload the files of interest or paste their contents"]),
                html.Br(),
                html.Div([
                    dbc.ListGroup([
                        dbc.ListGroupItem([
                            dbc.ListGroupItemHeading(dbc.Button('Sequence', block=True, outline=True, color='dark',
                                                                id='sequence-upload-head')),
                            dbc.ListGroupItemText(
                                dbc.Collapse([
                                    FastaUploadCard()
                                ], id='sequence-upload-collapse')
                            )
                        ]),
                        dbc.ListGroupItem([
                            dbc.ListGroupItemHeading(
                                dbc.Button('Contact map', block=True, outline=True, color='dark',
                                           id='contact-map-upload-head')),
                            dbc.ListGroupItemText(
                                dbc.Collapse([
                                    ContactUploadCard()
                                ], id='contact-map-upload-collapse')
                            )
                        ]),
                    ]),
                ], className='InputPanel', style={'height': '60vh', 'overflow-y': 'scroll'}),
                html.Br(),
                html.Br(),
                dbc.Modal([
                    dbc.ModalHeader(
                        html.H4("Missing Inputs", className="alert-heading", style={'color': 'red'}),
                    ),
                    dbc.ModalBody([
                        html.P("Please ensure you fill in all required fields before trying to generate a plot. "
                               "We detected problems on the following fields:"
                               ),
                        html.Hr(),
                        html.Div(id='missing-fields-div'),
                    ]),
                ], id='missing-fields-modal'),
                html.Br(),
                dbc.Button('Plot', id='plot-button', color="primary", block=True),

            ], width=4),
            dbc.Col([
                html.Br(),
                html.Br(),
                html.Div([
                    html.Div([
                        html.Img(
                            src='https://raw.githubusercontent.com/rigdenlab/conkit-web/master/assets/conkit_small_logo.png',
                            style={'margin': 'auto', 'vertical-align': 'middle'}
                        )
                    ], style={'display': 'flex', 'justify-content': 'center'})
                ], id='plot-div', )
            ], id='plot-column', width=7)
        ]),
    ])
