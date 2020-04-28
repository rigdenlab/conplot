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


def DisplayControlCard():
    return dbc.Card(
        dbc.CardBody(
            [
                dbc.Spinner(
                    html.Div([
                        html.P("Change the different data tracks", className="card-text"),
                        html.Br(),
                        dbc.Card([
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("L /", addon_type="prepend"),
                                    dbc.Input(id='L-cutoff-input', type="number", min=1, max=10, step=1,
                                              placeholder='2'),
                                ],
                            ),
                        ], outline=False),
                        html.Br(),
                        dcc.Dropdown(
                            options=[
                                {'label': 'Membrane Topology', 'value': DatasetReference.MEMBRANE_TOPOLOGY.value},
                                {'label': 'Disorder', 'value': DatasetReference.SEQUENCE.value},
                                {'label': 'Consercation', 'value': DatasetReference.CONTACT_MAP.value},
                            ],
                            value=[DatasetReference.MEMBRANE_TOPOLOGY.value],
                            multi=True
                        ),
                        html.Br(),
                        dbc.Button('Refresh', id='refresh-button', outline=True, color='primary', block=True)
                    ])
                )
            ]
        )
    )
