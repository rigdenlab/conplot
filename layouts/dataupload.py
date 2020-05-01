from core import PathIndex
import dash_html_components as html
from components import NavBar, Header, UploadCard, PlotPlaceHolder, DisplayControlCard, ContactUploadCard, WarningsCard, \
    HelpCard
import dash_bootstrap_components as dbc


def DataUpload(session_id):
    return html.Div([
        html.Div(id='_hidden-div', style={'display': 'none'}),
        Header(),
        html.Div(id='modal-div'),
        NavBar(PathIndex.PLOT.value),
        dbc.Row([
            dbc.Col([
                html.Br(),
                html.Br(),
                html.Div([
                    dbc.ListGroup([
                        dbc.ListGroupItem([
                            dbc.ListGroupItemHeading(dbc.Button('Sequence', block=True, outline=True, color='dark',
                                                                id='sequence-upload-head')),
                            dbc.ListGroupItemText(
                                dbc.Collapse([
                                    UploadCard('sequence')
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
                                           id='membranetopology-upload-head')),
                            dbc.ListGroupItemText(
                                dbc.Collapse([
                                    UploadCard('membranetopology')
                                ], id='membranetopology-upload-collapse')
                            )
                        ]),
                        dbc.ListGroupItem([
                            dbc.ListGroupItemHeading(
                                dbc.Button('Secondary structure', block=True, outline=True, color='dark',
                                           id='secondarystructure-upload-head')),
                            dbc.ListGroupItemText(
                                dbc.Collapse([
                                    UploadCard('secondarystructure')
                                ], id='secondarystructure-upload-collapse')
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
                                           id='conservation-upload-head')),
                            dbc.ListGroupItemText(
                                dbc.Collapse([
                                    UploadCard('conservation')
                                ], id='conservation-upload-collapse')
                            )
                        ]),
                    ]),
                ], className='InputPanel', style={'height': '64vh', 'overflow-y': 'scroll'}),
                html.Br(),
                html.Br(),
                dbc.Button('Plot', id='plot-button', color="primary", block=True),
            ], width=3),
            dbc.Col([
                html.Br(),
                html.Br(),
                dbc.Spinner([
                    html.Div([
                        PlotPlaceHolder()
                    ], id='plot-div')
                ])
            ], id='plot-column', width=5),
            dbc.Col([
                html.Br(),
                html.Br(),
                html.Div([
                    dbc.ListGroup([
                        dbc.ListGroupItem([
                            dbc.ListGroupItemHeading(
                                dbc.Button(html.I(className="fas fa-cog fa-2x"), outline=True, color='dark',
                                           id='display-control-head', block=True)),
                            dbc.ListGroupItemText(
                                dbc.Collapse([
                                    DisplayControlCard()
                                ], id='display-control-collapse')
                            )
                        ]),
                        dbc.ListGroupItem([
                            dbc.ListGroupItemHeading(
                                dbc.Button(html.I(className="fas fa-exclamation-circle fa-2x"), outline=True,
                                           color='dark', block=True, id='warning-head')),
                            dbc.ListGroupItemText(
                                dbc.Collapse([
                                    WarningsCard()
                                ], id='warning-collapse')
                            )
                        ]),
                        dbc.ListGroupItem([
                            dbc.ListGroupItemHeading(
                                dbc.Button(html.I(className="fas fa-question-circle fa-2x"), outline=True, color='dark',
                                           block=True, id='help-head')),
                            dbc.ListGroupItemText(
                                dbc.Collapse([
                                    HelpCard()
                                ], id='help-collapse')
                            )
                        ]),
                    ]),
                ], className='InputPanel', style={'height': '73vh', 'overflow-y': 'scroll'}),
            ], width=3),
        ], justify="between"),
    ])
