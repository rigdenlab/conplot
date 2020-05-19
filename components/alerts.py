import dash_bootstrap_components as dbc
import dash_html_components as html
from utils import UrlIndex


def ErrorAlert(is_open=False):
    return dbc.Alert([
        html.H4('ERROR', className="alert-heading"),
        html.P([
            "If you suspect a bug, please report this to email@me.com or on the project's ",
            html.A("Github repository", href=UrlIndex.GITHUB.value, className="alert-link")
        ]),
    ], dismissable=True, color='danger', fade=True, is_open=is_open, id='error-alert')


def FilenameAlert(filename, dataset):
    return dbc.Alert(
        '{}: {}'.format(dataset, filename),
        dismissable=True, color="success", is_open=True,
        id={'type': 'filename-alert', 'index': '["{}", "{}"]'.format(filename, dataset)}
    )


def ContactBugAlert():
    return dbc.Alert([
        html.H4('Info', className="alert-heading"),
        html.P([
            "If you suspect a bug, you can also create an issue on the project's ",
            html.A("Github repository", href=UrlIndex.GITHUB.value, className="alert-link")
        ]),
    ],
        dismissable=True,
        color='danger',
        fade=True,
        is_open=False,
        id='bug-alert'
    )
