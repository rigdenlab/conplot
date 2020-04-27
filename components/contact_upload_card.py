import dash_bootstrap_components as dbc
import dash_html_components as html
from .uploadbutton import UploadButton
import conkit.io
from .filename_alert import FilenameAlert


def ContactUploadCard():
    return dbc.Card(
        dbc.CardBody(
            [
                dbc.Spinner(
                    html.Div([
                        html.P("Upload a file with the contact map of interest or copy paste the map",
                               className="card-text"),
                        dbc.Textarea(id="contact-map-text-area", className="mb-3",
                                     placeholder="Paste here your contact map",
                                     debounce=True),
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
