import dash_bootstrap_components as dbc
import dash_html_components as html


def InvalidFileCollapse(dataset):
    return [

        dbc.Collapse(
            dbc.Card(
                dbc.CardBody("Invalid format, unable to load", style={'text-align': "center"}),
                color="danger", outline=True
            ),
            id={'type': "invalid-collapse", 'index': dataset}, is_open=True
        ),
        html.Br()
    ]


def InvalidAddTrackCollapse():
    return dbc.Collapse(
        dbc.Card(
            dbc.CardBody("Invalid format, unable to load", style={'text-align': "center"}),
            color="danger", outline=True
        ), id='invalid-track-collapse', is_open=True)
