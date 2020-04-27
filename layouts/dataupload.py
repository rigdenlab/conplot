import dash_html_components as html
from components import NavBar, Header, UploadCard, PlotPlaceHolder, DisplayControlCard, ContactUploadCard
from index import PathIndex
import dash_bootstrap_components as dbc
from callbacks import dataupload_callbacks


def DataUpload(session_id):
    return html.Div([
        html.Div(id='_hidden-div', style={'display': 'none'}),
        Header(),
        html.Div(id='modal-div'),
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
                                    UploadCard('fasta')
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
                        dbc.ListGroupItem([
                            dbc.ListGroupItemHeading(
                                dbc.Button('Membrane topology', block=True, outline=True, color='dark',
                                           id='mem-upload-head')),
                            dbc.ListGroupItemText(
                                dbc.Collapse([
                                    UploadCard('mem')
                                ], id='mem-upload-collapse')
                            )
                        ]),
                        dbc.ListGroupItem([
                            dbc.ListGroupItemHeading(
                                dbc.Button('Secondary structure', block=True, outline=True, color='dark',
                                           id='ss-upload-head')),
                            dbc.ListGroupItemText(
                                dbc.Collapse([
                                    UploadCard('ss')
                                ], id='ss-upload-collapse')
                            )
                        ]),
                        dbc.ListGroupItem([
                            dbc.ListGroupItemHeading(
                                dbc.Button('Disorder', block=True, outline=True, color='dark',
                                           id='disorder-upload-head')),
                            dbc.ListGroupItemText(
                                dbc.Collapse([
                                    UploadCard('disorder')
                                ], id='disorder-upload-collapse')
                            )
                        ]),
                        dbc.ListGroupItem([
                            dbc.ListGroupItemHeading(
                                dbc.Button('Conservation', block=True, outline=True, color='dark',
                                           id='conserv-upload-head')),
                            dbc.ListGroupItemText(
                                dbc.Collapse([
                                    UploadCard('conserv')
                                ], id='conserv-upload-collapse')
                            )
                        ]),
                        dbc.ListGroupItem([
                            dbc.ListGroupItemHeading(
                                dbc.Button(html.I(className="fas fa-cog"), outline=True, color='dark', block=True,
                                           id='display-control-head')),
                            dbc.ListGroupItemText(
                                dbc.Collapse([
                                    DisplayControlCard()
                                ], id='display-control-collapse')
                            )
                        ]),
                    ]),
                ], className='InputPanel', style={'height': '60vh', 'overflow-y': 'scroll'}),
                html.Br(),
                html.Br(),
                dbc.Button('Plot', id='plot-button', color="primary", block=True),
            ], width=4),
            dbc.Col([
                html.Br(),
                html.Br(),
                dbc.Spinner([
                    html.Div([
                        PlotPlaceHolder()
                    ], id='plot-div')
                ])
            ], id='plot-column', width=7),
        ]),
    ])
