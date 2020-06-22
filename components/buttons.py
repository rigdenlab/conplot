import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


def Button(id, children, color='primary'):
    return dbc.Button(id=id, children=children, color=color, block=True)


def UploadButton(dataset, multiple=False, disabled=False):
    return html.Div([
        dcc.Upload(
            id='upload-{}-component'.format(dataset),
            children=Button(children="Upload {}".format(dataset), id='upload-{}-button'.format(dataset)),
            multiple=multiple, disabled=disabled
        ),
    ])


def AddTrackButton(multiple=False, disabled=False):
    return html.Div([
        dcc.Upload(
            id='additional-tracks-upload',
            children=Button(children=html.I(className="fas fa-plus-circle fa-2x"), id='upload-additionaltrack-button'),
            multiple=multiple, disabled=disabled
        ),
    ])
