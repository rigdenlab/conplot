import dash_html_components as html
import dash_bootstrap_components as dbc
from loaders import DatasetReference
from app import UrlIndex


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
        ], id='mismatch-modal', is_open=True)


def MissingInputModal(*args):
    return dbc.Modal([
        dbc.ModalHeader(
            html.H4("Missing Inputs", className="alert-heading", style={'color': 'red'}),
        ),
        dbc.ModalBody([
            html.P("Please ensure you fill in all required fields before trying to generate a plot. "
                   "We detected problems on the following fields:"),
            html.Ul([
                html.Li('%s file' % arg) for arg in args
            ], id='missing-fields-div'),
        ]),
    ], id='missing-fields-modal', is_open=True)


def RepeatedInputModal(dataset):
    return dbc.Modal([
        dbc.ModalHeader(
            html.H4("Already uploaded", className="alert-heading", style={'color': 'red'}),
        ),
        dbc.ModalBody([
            html.P("A file for the dataset {} was already provided. To upload a different one you will need to delete"
                   " the current one first.".format(dataset))
        ]),
    ], id='missing-fields-modal', is_open=True)

def InvalidInputModal():
    return dbc.Modal([
        dbc.ModalHeader(
            html.H4("Invalid input", className="alert-heading", style={'color': 'red'}),
        ),
        dbc.ModalBody([
            html.P("Some of the values you have selected on the display control tab are invalid, either because they "
                   "are out of the permitted range or the input is non-numeric. Check your selection on those"
                   " selectors highlighted on red and make sure the value you introduce is correct.")
        ]),
    ], id='invalid-input-modal', is_open=True)

def SessionTimedOutModal():
    return dbc.Modal([
        dbc.ModalHeader(
            html.H4("Session timed-out", className="alert-heading", style={'color': 'red'}),
        ),
        dbc.ModalBody([
            html.P("More than 5 minutes have passed since you last interacted with the website and your session has"
                   "timed-out."),
            html.A(dbc.Button("Start new session", block=True, color='danger'), href=UrlIndex.ROOT.value,
                   style={"text-decoration": "none"})
        ]),
    ], id='missing-fields-modal', is_open=True)
