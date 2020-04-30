import dash_bootstrap_components as dbc
import dash_html_components as html
from .uploadbutton import UploadButton
import conkit.io
from .alerts import FilenameAlert
import dash_core_components as dcc
from index import DatasetReference


def ContactUploadCard():
    return dbc.Card(
        dbc.CardBody(
            [
                dbc.Spinner(
                    html.Div([
                        html.P("Upload a file with the contact map of interest or copy paste the map",
                               className="card-text"),
                        dbc.Textarea(id="contact-map-text-area", className="mb-3",
                                     placeholder="Paste here your contact map", debounce=True),
                        html.Br(),
                        dbc.Card([
                            dbc.InputGroup(
                                [
                                    dbc.Select(
                                        id="contact-format-select",
                                        options=[{"label": map_format, "value": map_format} for map_format in
                                                 conkit.io.CONTACT_FILE_PARSERS.keys()]
                                    ),
                                    dbc.InputGroupAddon("Format", addon_type="append"),
                                ]
                            ),
                        ], id='format-selection-card', color="danger", outline=True),
                        html.Br(),
                        dbc.Collapse(
                            dbc.Card(dbc.CardBody("Invalid Contact Map! Make sure the format is correct"),
                                     color="danger",
                                     outline=True),
                            id="contact-map-invalid-collapse",
                        ),
                        FilenameAlert('contact-map'),
                        html.Br(),
                        UploadButton('contact-map')
                    ])
                )
            ]
        )
    )


def UploadCard(dataset):
    return dbc.Card(
        dbc.CardBody(
            [
                dbc.Spinner(
                    html.Div([
                        html.P("Choose a file to upload or paste its contents.",
                               className="card-text"),
                        dbc.Textarea("{}-text-area".format(dataset), className="mb-3",
                                     placeholder="Paste here your prediction", debounce=True),
                        dbc.Collapse(
                            dbc.Card(dbc.CardBody("Invalid format, unable to load"), color="danger", outline=True),
                            id="{}-invalid-collapse".format(dataset),
                        ),
                        FilenameAlert(dataset),
                        html.Br(),
                        UploadButton(dataset)
                    ])
                )
            ]
        )
    )


def DisplayControlCard(available_tracks=None, factor=2):
    if available_tracks is None:
        return dbc.Card([
            dbc.CardBody("Need to create a plot first!"),
            html.Div([
                dbc.Button('Refresh', id='refresh-button', outline=True, color='primary', block=True),
                dcc.Dropdown(id='track-selection-dropdown'),
                dbc.Input(id='L-cutoff-input'),
            ], style={'display': 'none'})
        ],
            color="danger",
            outline=True
        )
    else:
        return dbc.Card(
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
                            html.Br(),
                            dbc.Button('Refresh', id='refresh-button', outline=True, color='primary', block=True)
                        ])
                    )
                ]
            )
        )


def HelpCard():
    return dbc.Card([
        dbc.CardBody("Some hints will go here..."),
    ], color="dark", outline=True)


def WarningsCard(warnings=None):
    return dbc.Card([
        dbc.CardBody("There are no warnigns registered"),
    ], color="success", outline=True)
