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


def SuccessLoginAlert(username):
    return dbc.Alert([
        html.H4('Success', className="alert-heading", style={'text-align': "center"}),
        html.P([
            "You have successfully logged in as '%s'. You can now safely store plots after you create them "
            "on the Plot tab!" % username
        ], style={'text-align': "center"}),
    ],
        dismissable=False,
        color='success',
        fade=True,
        is_open=True,
        id='success-login-alert'
    )


def SuccessLogoutAlert():
    return dbc.Alert([
        html.H4('Success', className="alert-heading", style={'text-align': "center"}),
        html.P([
            "You have successfully logged out"
        ], style={'text-align': "center"}),
    ],
        dismissable=False,
        color='danger',
        fade=True,
        is_open=True,
        id='success-logout-alert'
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
