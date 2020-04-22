import dash_bootstrap_components as dbc
import dash_html_components as html
from .uploadbutton import UploadButton
from .filename_alert import FilenameAlert


def SequenceUploadCard():
    return dbc.Card(
        dbc.CardBody(
            [
                dbc.Spinner(
                    html.Div([
                        html.P("Upload a FASTA file with the sequence of interest or paste the sequence",
                               className="card-text"),
                        dbc.Textarea("fasta-text-area", className="mb-3", placeholder="Paste here your sequence",
                                     debounce=True),
                        dbc.Collapse(
                            dbc.Card(dbc.CardBody("Invalid FASTA sequence"), color="danger", outline=True),
                            id="fasta-invalid-collapse",
                        ),
                        FilenameAlert('fasta'),
                        html.Br(),
                        UploadButton('fasta')
                    ])
                )
            ]
        )
    )
