import dash_bootstrap_components as dbc
import dash_html_components as html
from .uploadbutton import UploadButton


def ContactUploadCard():
    return dbc.Card(
        dbc.CardBody(
            [
                html.H5("Contact Map", className="card-title"),
                html.P("Upload a file with the contact map of interest", className="card-text"),
                UploadButton('contact-map')
            ]
        )
    )
