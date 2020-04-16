import dash_bootstrap_components as dbc
import dash_html_components as html
from .pathindex import PathIndex

def ErrorAlert():
    alert = dbc.Alert([html.H4('ERROR', className="alert-heading"),
                       html.P([
                           "If you suspect a bug, please report this to email@me.com or on the project's ",
                           html.A("Github repository", href=PathIndex.GITHUB.value,
                                  className="alert-link")
                       ]),
                       ],
                      dismissable=True,
                      color='danger',
                      fade=True,
                      is_open=True
                      )

    return alert
