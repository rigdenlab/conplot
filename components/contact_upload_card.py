import dash_bootstrap_components as dbc
import dash_html_components as html
from .uploadbutton import UploadButton
import conkit.io


def ContactUploadCard():
    return dbc.Card(
        dbc.CardBody(
            [
                html.H5("Contact Map", className="card-title"),
                html.P("Upload a file with the contact map of interest or copy paste the map", className="card-text"),
                dbc.Textarea(className="mb-3", placeholder="Paste here your contact map"),
                html.P(["Format  ", dbc.Badge("Required", id='format-badge', color="danger", className="mr-1")],
                       className="card-text"),
                dbc.Select(
                    id="contact-format-select",
                    options=[{"label": map_format, "value": map_format} for map_format in
                             conkit.io.CONTACT_FILE_PARSERS.keys()]
                ),
                html.Br(),
                html.Br(),
                UploadButton('contact-map')
            ]
        )
    )
