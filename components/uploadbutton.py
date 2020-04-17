import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


def UploadButton(id, multiple=False):
    return html.Div([
        dcc.Upload(
            id='upload-{}'.format(id),
            children=dbc.Button("Upload", id='upload-{}-button'.format(id), color="primary", block=True),
            multiple=multiple
        ),
    ])
