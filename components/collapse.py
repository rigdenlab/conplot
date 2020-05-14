import dash_bootstrap_components as dbc
import dash_html_components as html
from components import InvalidFormatCard


def InvalidFileCollapse(dataset):
    return [
        dbc.Collapse(InvalidFormatCard(), id={'type': "invalid-collapse", 'index': dataset}, is_open=True),
        html.Br()
    ]


def InvalidAddTrackCollapse():
    return dbc.Collapse(InvalidFormatCard(), id='invalid-track-collapse', is_open=True)
