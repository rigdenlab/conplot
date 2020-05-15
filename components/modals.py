from components import StartNewSessionLink
import dash_bootstrap_components as dbc
import dash_html_components as html
from loaders import DatasetReference


def MismatchModal(*args):
    if DatasetReference.SEQUENCE not in args:

        return dbc.Modal([
            ModalHeader("Mismatch Detected"),
            dbc.ModalBody([
                html.P("""We are having problems to match the uploaded sequence with the following predictions. Please 
                ensure that these predictions correspond with the protein sequence in the uploaded FASTA file."""),
                html.Ul([html.Li('%s' % arg) for arg in args], id='missing-fields-div')
            ])
        ], id='mismatch-modal', is_open=True)

    else:
        return dbc.Modal([
            ModalHeader("Sequence Mismatch"),
            dbc.ModalBody(
                html.P("""We are having problems to match the uploaded sequence with the provided contact map. Please 
                ensure that the provided the sequence corresponds with the protein of the given contact map.""")
            )
        ], id='mismatch-modal', is_open=True)


def MissingInputModal(*args):
    return dbc.Modal([
        ModalHeader("Missing Inputs"),
        dbc.ModalBody([
            html.P("""Please ensure you fill in all required fields before trying to generate a plot. Following 
            mandatory fields are still missing:"""),
            html.Ul([html.Li('%s file' % arg) for arg in args], id='missing-fields-div')
        ]),
    ], id='missing-fields-modal', is_open=True)


def RepeatedInputModal(dataset):
    return dbc.Modal([
        ModalHeader("Already uploaded"),
        dbc.ModalBody(
            html.P("""A file for the dataset {} was already provided. To upload a different one you will need to delete 
            the current one first.""".format(dataset))
        ),
    ], id='missing-fields-modal', is_open=True)


def InvalidInputModal():
    return dbc.Modal([
        ModalHeader("Invalid input"),
        dbc.ModalBody(
            html.P("""Some of the values you have selected on the display control tab are invalid, either because they 
            are out of the permitted range or the input is non-numeric. Check your selection on those selectors 
            highlighted on red and make sure the value you introduce is correct.""")
        ),
    ], id='invalid-input-modal', is_open=True)


def SessionTimedOutModal():
    return dbc.Modal([
        ModalHeader("Session timed-out"),
        dbc.ModalBody([
            html.P("""More than 5 minutes have passed since you last interacted with the website and your session has 
            timed-out."""),
            StartNewSessionLink()
        ]),
    ], id='missing-fields-modal', is_open=True, backdrop='static', keyboard=False)


def ModalHeader(text):
    return dbc.ModalHeader(html.H4(text, className="alert-heading", style={'color': 'red'}))
