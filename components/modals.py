import dash_html_components as html
import dash_bootstrap_components as dbc
from index import DatasetReference


def MismatchModal(*args):
    if DatasetReference.SEQUENCE.name not in args:

        return dbc.Modal([
            dbc.ModalHeader(
                html.H4("Mismatch Detected", className="alert-heading", style={'color': 'red'}),
            ),
            dbc.ModalBody([
                html.P("We are having problems to match the uploaded sequence with the following predictions. "
                       "Please ensure that these predictions correspond with the protein sequence in the uploaded "
                       "FASTA file."
                       ),
                html.Ul([
                    html.Li('%s' % arg) for arg in args
                ], id='missing-fields-div'),
            ]),
        ], id='mismatch-modal', is_open=True)

    else:
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
