import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


def UploadButton(dataset, multiple=False, disabled=False):
    return html.Div([
        dcc.Upload(
            id={
                'type': 'upload-button',
                'index': dataset
            },
            children=dbc.Button(
                "Upload {}".format(dataset), id='upload-{}-button'.format(dataset), color="primary", block=True
            ),
            multiple=multiple, disabled=disabled
        ),
    ])


def AddTrackButton(multiple=False, disabled=False):
    return html.Div([
        dcc.Upload(
            id='additionaltrack-upload',
            children=dbc.Button(
                html.I(className="fas fa-plus-circle fa-2x"), id='upload-additionaltrack-button',
                color="primary", block=True
            ),
            multiple=multiple, disabled=disabled
        ),
    ])
