import dash_bootstrap_components as dbc
import dash_html_components as html
from .uploadbutton import UploadButton


def FastaUploadCard():
    return dbc.Card(
        dbc.CardBody(
            [
                html.H5("Fasta", className="card-title"),
                html.P("Upload a FASTA file with the sequence of interest or paste the sequence",
                       className="card-text"),
                dbc.Textarea("fasta-text-area", className="mb-3", placeholder="Paste here your sequence"),
                dbc.Collapse(
                    dbc.Card(dbc.CardBody("Invalid FASTA sequence"), color="danger", outline=True),
                    id="fasta-collapse",
                ),
                html.Br(),
                UploadButton('fasta')
            ]
        )
    )
