import dash_bootstrap_components as dbc
import dash_html_components as html
from .uploadbutton import UploadButton
import conkit.io


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
                        html.P("Additional options", className="card-text"),
                        dbc.Row([
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
                        ]),
                        html.Br(),
                        dbc.Row([
                            dbc.Card([
                                dbc.InputGroup(
                                    [
                                        dbc.InputGroupAddon("L /", addon_type="prepend"),
                                        dbc.Input(id='L-cutoff-input', type="number", min=1, max=10, step=1,
                                                  placeholder='1'),
                                    ],
                                ),
                            ]),
                            dbc.Card([
                                dbc.Input(id='score-threshold-input', type="number", min=0.000, max=1.000, step=0.01,
                                          placeholder='Score threshold'),
                            ]),
                        ]),
                        html.Br(),
                        dbc.Row([
                            dbc.Col([
                                dbc.Checklist(
                                    options=[{"label": "Remove neighbours", "value": 1}, ],
                                    value=[],
                                    id="switches-inline-input",
                                    inline=True,
                                    switch=True,
                                ),

                            ])
                        ]),
                        html.Br(),
                        dbc.Collapse(
                            dbc.Card(dbc.CardBody("Invalid Contact Map! Make sure the format is correct"),
                                     color="danger",
                                     outline=True),
                            id="contact-map-invalid-collapse",
                        ),
                        dbc.Alert(
                            id='contact-map-filename-alert',
                            dismissable=True,
                            color="success"
                        ),
                        html.Br(),
                        UploadButton('contact-map')
                    ])
                )
            ]
        )
    )
