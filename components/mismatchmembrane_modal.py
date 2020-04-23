import dash_html_components as html
import dash_bootstrap_components as dbc


def MismatchMembrane_Modal():
    return dbc.Modal([
        dbc.ModalHeader(
            html.H4("Membrane Topology Mismatch", className="alert-heading", style={'color': 'red'}),
        ),
        dbc.ModalBody([
            html.P("We are having problems to match the uploaded sequence with the provided membrane topology "
                   "prediction. Please ensure that the provided the membrane topology prediction corresponds with the"
                   " protein sequence in the uploaded FASTA file."
                   ),
        ]),
    ], id='mismatch-modal', is_open=True),
