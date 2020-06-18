from components import StartNewSessionLink
import dash_bootstrap_components as dbc
import dash_html_components as html


def MismatchModal(*args):
    return dbc.Modal([
        ModalHeader("Mismatch Detected"),
        dbc.ModalBody([
            html.P("""We are having problems to match the uploaded sequence with the following prediction files. Please 
                ensure that these predictions correspond with the protein sequence in the uploaded FASTA file.""",
                   style={'text-align': "justify"}),
            html.Ul([html.Li('%s' % arg) for arg in args], id='mismatched-fnames-div')
        ])
    ], id='mismatch-modal', is_open=True)


def MismatchSequenceModal(*args):
    return dbc.Modal([
        ModalHeader("Sequence Mismatch"),
        dbc.ModalBody([
            html.P("""We are having problems to match the uploaded sequence with contact maps in the following files. 
            Please ensure that the provided the sequence corresponds with the structure in these contact maps.""",
                   style={'text-align': "justify"}),
            html.Ul([html.Li('File: %s' % arg) for arg in args], id='mismatched-maps-div')
        ])
    ], id='mismatch-modal', is_open=True)


def MissingInputModal(*args):
    return dbc.Modal([
        ModalHeader("Missing Inputs"),
        dbc.ModalBody([
            html.P("""Please ensure you fill in all required fields before trying to generate a plot. Following 
            mandatory fields are still missing:""", style={'text-align': "justify"}),
            html.Ul([html.Li('File: %s' % arg) for arg in args], id='missing-fields-div')
        ]),
    ], id='missing-fields-modal', is_open=True)


def SequenceAlreadyUploadedModal():
    return dbc.Modal([
        ModalHeader("Sequence already uploaded"),
        dbc.ModalBody(
            html.P("""Only one sequence file can be uploaded at once. If you wish to upload a new sequence file, remove
            the currently uploaded file before uploading a new sequence file.""", style={'text-align': "justify"})
        ),
    ], id='missing-fields-modal', is_open=True)


def RepeatedInputModal(fname):
    return dbc.Modal([
        ModalHeader("File already uploaded"),
        dbc.ModalBody(
            html.P("""A file with the name - {} - has already been uploaded. You cannot upload two files with identical
             names, please rename one of them and try again.""".format(fname), style={'text-align': "justify"})
        ),
    ], id='missing-fields-modal', is_open=True)


def InvalidInputModal():
    return dbc.Modal([
        ModalHeader("Invalid input"),
        dbc.ModalBody(
            html.P("""Some of the values you have selected on the display control tab are invalid, either because they 
            are out of the permitted range or the input is non-numeric. Check your selection on those selectors 
            highlighted on red and make sure the value you introduce is correct.""", style={'text-align': "justify"})
        ),
    ], id='invalid-input-modal', is_open=True)


def SessionTimedOutModal():
    return dbc.Modal([
        ModalHeader("Session timed-out"),
        dbc.ModalBody([
            html.P("""More than 15 minutes have passed since you last interacted with the website and your session has 
            timed-out.""", style={'text-align': "justify"}),
            StartNewSessionLink()
        ]),
    ], id='missing-fields-modal', is_open=True, backdrop='static', keyboard=False)


def ModalHeader(text):
    return dbc.ModalHeader(html.H4(text, className="alert-heading", style={'color': 'red'}))


def InvalidFormatModal():
    return dbc.Modal([
        ModalHeader("Invalid file format"),
        dbc.ModalBody(
            html.P("""The file you just attempted to upload does not comply with the file format guidelines. Make sure 
            that you are uploading the correct file and you have selected the correct format. If you are not sure about 
            how the file format looks like, you can read about each format on our help page. If you are sure that the 
            format of your file is correct, please report the bug on the 'Contact' tab.""",
                   style={'text-align': "justify"})
        ),
    ], id='invalid-input-modal', is_open=True)


def SessionStoreModal(session_name):
    if session_name is not None:
        return dbc.Modal([
            dbc.ModalHeader(
                html.H4('Session stored successfully', className="alert-heading", style={'color': 'green'})),
            dbc.ModalBody(
                html.P("""You have successfully stored the currently uploaded data as new session with the name %s
                """ % session_name, style={'text-align': "justify"})
            ),
        ], id='invalid-input-modal', is_open=True)
    else:
        return dbc.Modal([
            dbc.ModalHeader(
                html.H4('Error', className="alert-heading", style={'color': 'red'})),
            dbc.ModalBody(
                html.P("You must provide a name for the session before saving it!", style={'text-align': "justify"})
            ),
        ], id='invalid-input-modal', is_open=True)


def InvalidContactFormModal():
    return dbc.Modal([
        ModalHeader(html.H4("Missing input", className="alert-heading", style={'color': 'red'})),
        dbc.ModalBody(
            html.P("""You must fill in all fields before submiting your contact form!""",
                   style={'text-align': "justify"})
        ),
    ], id='invalid-contact-form-modal', is_open=True)


def SuccessContactFormModal():
    return dbc.Modal([
        ModalHeader(html.H4("Success", className="alert-heading", style={'color': 'green'})),
        dbc.ModalBody(
            html.P("""You have successfully submitted the contact form. We will get in touch with the provided email 
            as soon as we can.""", style={'text-align': "justify"})
        ),
    ], id='success-contact-form-modal', is_open=True)


def SlackConnectionErrorModal():
    return dbc.Modal([
        ModalHeader(html.H4('Connnection Error', className="alert-heading", style={'color': 'red'})),
        dbc.ModalBody(
            html.P("""Something went wrong while submitting your contact form. This is most likely a problem on our 
            side, we are working to solve this.""", style={'text-align': "justify"})
        ),
    ], id='slack-contaction-error-modal', is_open=True)
