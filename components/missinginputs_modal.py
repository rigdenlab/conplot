import dash_html_components as html
import dash_bootstrap_components as dbc


def MissingInput_Modal(*args):
    return dbc.Modal([
        dbc.ModalHeader(
            html.H4("Missing Inputs", className="alert-heading", style={'color': 'red'}),
        ),
        dbc.ModalBody([
            html.P("Please ensure you fill in all required fields before trying to generate a plot. "
                   "We detected problems on the following fields:"
                   ),
            html.Ul([
                html.Li('%s file' % arg) for arg in args
            ], id='missing-fields-div'),
        ]),
    ], id='missing-fields-modal', is_open=True),
