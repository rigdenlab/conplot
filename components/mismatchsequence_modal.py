import dash_html_components as html
import dash_bootstrap_components as dbc


def MismatchSequence_Modal():
    return dbc.Modal([
        dbc.ModalHeader(
            html.H4("Sequence Mismatch", className="alert-heading", style={'color': 'red'}),
        ),
        dbc.ModalBody([
            html.P("We are having problems to match the uploaded sequence with the provided contact map. "
                   "Please ensure that the provided the sequence corresponds with the protein of the given contact map."
                   ),
        ]),
    ], id='mismatch-modal', is_open=True),
