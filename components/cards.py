import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from parsers import ContactFormats
from components import UploadButton, AddTrackButton
from loaders import DatasetReference, AdditionalTracks


def MandatoryUploadCard():
    return dbc.Spinner(
        dbc.Card(
            dbc.CardBody(
                [
                    html.H4("Required input", className="card-text", style={'text-align': "center"}),
                    html.Br(),
                    dbc.Card([
                        dbc.CardBody([
                            html.H5('Sequence', style={'text-align': "center"}),
                            html.Br(),
                            html.Div(id={'type': 'file-div', 'index': DatasetReference.SEQUENCE.value}),
                            UploadButton(DatasetReference.SEQUENCE.value),
                        ], id='format-selection-card'),
                    ]),
                    html.Br(),
                    dbc.Card([
                        dbc.CardBody([
                            html.H5('Contact Map', style={'text-align': "center"}),
                            html.Br(),
                            dbc.Card([
                                dbc.InputGroup(
                                    [
                                        dbc.Select(
                                            id='contact-format-selector',
                                            options=[{"label": map_format, "value": map_format} for map_format in
                                                     ContactFormats.__dict__.keys() if '_' not in map_format]
                                        ),
                                        dbc.InputGroupAddon("Format", addon_type="append"),
                                    ]
                                ),
                            ], id='format-selection-card', color="danger", outline=True),
                            html.Br(),
                            html.Div(id={'type': 'file-div', 'index': DatasetReference.CONTACT_MAP.value}),
                            UploadButton(DatasetReference.CONTACT_MAP.value, disabled=True)
                        ], id='format-selection-card'),
                    ]),
                ]
            )
        )
    )


def AdditionalTracksUploadCard():
    return dbc.Spinner(
        dbc.Card([
            dbc.CardBody([
                html.H4("Additional tracks", className="card-text", style={'text-align': "center"}),
                html.Br(),
                html.Div([
                    NoAdditionalTracksCard()
                ], id='additional-tracks-filenames'),
                html.Br(),
                dbc.Card([
                    dbc.InputGroup(
                        [
                            dbc.Select(
                                id='track-selector',
                                options=[{"label": '{} ({})'.format(track.name, track.value), "value": track.name}
                                         for track in AdditionalTracks]
                            ),
                            dbc.InputGroupAddon("Track", addon_type="append"),
                        ]
                    ),
                ], id='track-selection-card', color="danger", outline=True),
                html.Br(),
                AddTrackButton(disabled=True)
            ]),
        ])
    )


def NoAdditionalTracksCard():
    return dbc.Card(dbc.CardBody("No additional tracks"), color="danger", outline=True, id='no-tracks-card')


def DisplayControlCard(available_tracks=None, factor=2, contact_marker_size=5, track_marker_size=7, track_separation=2):
    if available_tracks is None:
        return dbc.Card(
            dbc.CardBody(
                [
                    html.H4('Display control', className="card-text", style={'text-align': "center"}),
                    html.Br(),
                    dbc.Card([
                        dbc.CardBody("Need to create a plot first!"),
                        html.Div([
                            dbc.Button('Refresh', id='refresh-button', outline=True, color='primary', block=True),
                            dcc.Dropdown(id='track-selection-dropdown'),
                            dbc.Input(id='L-cutoff-input'),
                            dbc.Input(id='contact-marker-size-input'),
                            dbc.Input(id='track-marker-size-input'),
                            dbc.Input(id='track-separation-size-input'),
                        ], style={'display': 'none'})
                    ],
                        color="danger",
                        outline=True
                    )
                ]
            )
        )
    else:
        return html.Div([
            html.H4('Display control', className="card-text", style={'text-align': "center"}),
            html.Br(),
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Spinner(
                            html.Div([
                                html.P("Adjust contact map", className="card-text"),
                                dbc.Card([
                                    dbc.InputGroup(
                                        [
                                            dbc.InputGroupAddon("L /", addon_type="prepend"),
                                            dbc.Input(id='L-cutoff-input', type="number", min=1, max=10, step=1,
                                                      value=factor),
                                        ],
                                    ),
                                ], outline=False),
                                html.Br(),
                                dbc.Card([
                                    dbc.InputGroup(
                                        [
                                            dbc.InputGroupAddon("Size", addon_type="prepend"),
                                            dbc.Input(id='contact-marker-size-input', type="number", min=1, max=10,
                                                      step=1, value=contact_marker_size),
                                        ],
                                    ),
                                ], outline=False),
                                html.Br(),
                                html.Hr(),
                                html.P('Adjust additional tracks'),
                                dbc.Card([
                                    dbc.InputGroup(
                                        [
                                            dbc.InputGroupAddon("Size", addon_type="prepend"),
                                            dbc.Input(id='track-marker-size-input', type="number", min=1, max=10,
                                                      step=1, value=track_marker_size),
                                        ],
                                    ),
                                ], outline=False),
                                html.Br(),
                                dbc.Card([
                                    dbc.InputGroup(
                                        [
                                            dbc.InputGroupAddon("Separation", addon_type="prepend"),
                                            dbc.Input(id='track-separation-size-input', type="number", min=1, max=10,
                                                      step=1, value=track_separation),
                                        ],
                                    ),
                                ], outline=False),
                                html.Br(),
                                html.Hr(),
                                html.P("Active tracks", className="card-text"),
                                dcc.Dropdown(
                                    id='track-selection-dropdown',
                                    options=[
                                        {'label': dataset, 'value': dataset} for dataset in available_tracks
                                    ],
                                    value=[dataset for dataset in available_tracks],
                                    multi=True
                                ),
                            ])
                        )
                    ]
                )
            )
        ])
