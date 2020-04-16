import dash_bootstrap_components as dbc
import dash_html_components as html
from .uploadbutton import UploadButton


def FastaUploadCard():
    return dbc.Card(
        dbc.CardBody(
            [
                html.H5("Fasta", className="card-title"),
                html.P("Upload a FASTA file with the sequence of interest", className="card-text"),
                UploadButton('fasta')
            ]
        )
    )
