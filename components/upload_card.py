import dash_bootstrap_components as dbc
import dash_html_components as html
from .uploadbutton import UploadButton
from .filename_alert import FilenameAlert


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
