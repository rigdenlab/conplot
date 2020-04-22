import dash_bootstrap_components as dbc
import dash_html_components as html
from .uploadbutton import UploadButton
from .filename_alert import FilenameAlert


def MembraneTopologyUploadCard():
    return dbc.Card(
        dbc.CardBody(
            [
                dbc.Spinner(
                    html.Div([
                        html.P("Upload a file with the membrane topology predictions of your protein.",
                               className="card-text"),
                        dbc.Textarea("mem-text-area", className="mb-3", placeholder="Paste here your prediction",
                                     debounce=True),
                        dbc.Collapse(
                            dbc.Card(dbc.CardBody("Invalid prediction format"), color="danger", outline=True),
                            id="mem-invalid-collapse",
                        ),
                        FilenameAlert('mem-filename-alert'),
                        html.Br(),
                        UploadButton('mem')
                    ])
                )
            ]
        )
    )
