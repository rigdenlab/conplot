from components import StartNewSessionLink, GdprRightsList, AutomaticInfoCollectedList
import dash_bootstrap_components as dbc
import dash_html_components as html
from utils import UrlIndex


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


def InvalidMapSelectionModal():
    return dbc.Modal([
        ModalHeader("Invalid Input"),
        dbc.ModalBody([
            html.P("""Two different contacts maps must be selected to create a superimposed map!""",
                   style={'text-align': "justify"})
        ]),
    ], id='invalid-map-selection-modal', is_open=True)


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


def CustomFormatDescriptionModal():
    return dbc.Modal([
        dbc.ModalHeader('Custom Format Specifications'),
        dbc.ModalBody([
            dbc.Row([
                html.P('Custom files can be used to add personalised tracks to your plots. These files are plain text '
                       'files, and can be created manually in Notepad or similar text editors. The first line of this '
                       'file should start with the flag "LEN", followed by the length of the protein sequence that '
                       'this file is intended to be used with. Subsequent lines indicate records to be added in the '
                       'track, each defined using three fields, which are separated by white spaces:',
                       style={"text-align": "justify"}),
                html.Ul([
                    html.Li('Field 1: corresponds with the first residue number of the record  -inclusive, i.e. '
                            'indicates where the record should start-.', style={"text-align": "justify"}),
                    html.Li('Field 2: corresponds with the last residue number of the record -inclusive, i.e. '
                            'indicates where the record should end-.', style={"text-align": "justify"}),
                    html.Li('Field 3: indicates the color that should be used to depict this record. This is indicated '
                            'with a number between 1 and 11, that in turn is used by ConPlot to assign a color to this '
                            'record. A complete list of the mapping between these numbers and the actual color that '
                            'will be used in the plot can be found in the next section "Adjust the plot layout".',
                            style={"text-align": "justify"})
                ]),
                html.P('Bellow there is a sample of the first four lines of an example custom file. As you can see, '
                       'this sample corresponds with a file created for a protein containing 168 residues. In this '
                       'case, three records have been created, a record with color "3" that spans between residues 1 '
                       'and 10; a second record with color "6" that spans residues from 11 to 25; and a third record '
                       'with color "9" between residues 30 and 45. Note how a gap has been left between residues '
                       '25 and 30. When a range of residues has no record, this will be left as a blank gap in the '
                       'track by ConPlot.', style={"text-align": "justify"}),
                html.Br(),
                dbc.Col([
                    html.Plaintext('LEN 168\n1 10 3\n11 25 6\n30 45 9')
                ], width=5, style={'background-color': '#EAEAEA'}, align='center'),
            ], justify='center', align='center', className='m-0')
        ]),
    ], id='custom-format-specs-modal', is_open=False, size='lg', scrollable=True)


def GdprPolicyModal():
    return dbc.Modal([
        dbc.ModalHeader('ConPlot Website Privacy Policy. Updated: 03/07/2020'),
        dbc.ModalBody([
            dbc.Row([
                html.H4('1. Introduction'),
                html.P('ConPlot (also referred to as ‘we’ throughout this text) is committed to protect user data and '
                       'privacy. The purpose of this text is to provide you with information about how the data we '
                       'collect from users of ConPlot is used or shared. We may update this Privacy Notice from time '
                       'to time. We encourage you re-visit this text frequently and take note of the date of the last '
                       'update on the field above. We do not use or share any of your personal information for any '
                       'purpose unrelated to the functionality of the website; however, we do collect some '
                       'information to help us understand how our site is being used in order to improve community '
                       'support and to enhance the ConPlot user’s experience when visiting our site.'
                       , style={"text-align": "justify"}),
                html.Br(),
                html.H4('2. Information Automatically Collected'),
                html.P(['When you browse ConPlot, certain information about your visit will be collected. We '
                        'automatically collect and store the following type of information about your visit:',
                        AutomaticInfoCollectedList(),
                        'This automatically collected information does not identify you personally unless you include '
                        'personally identifying information in a support form request; see the “Get in Touch” policy '
                        'below for details. We use this information to measure the number of visitors to our site. '
                        'The aggregate data may be included in prospectuses and reports to funding agencies.'
                        ], style={"text-align": "justify"}),
                html.Br(),
                html.H4('3. Information You Directly Provide'),
                html.P('Storing, sharing sessions and any other user account related features of the ConPlot requires '
                       'that you register for an account. You will be required to provide an email address so we can '
                       'send you your temporary account password in case you forget this password. An anonymous email '
                       'service can be used if you do not want to provide personally identifying information. Your '
                       'email address will not be used to send you alerts or notifications. Any email address '
                       'provided in this site will only be used to get in touch with you in case your forget your '
                       'password or you request assistance from us. We do not sell or distribute email addresses to '
                       'third parties. We also ask for an user name when creating an account. If you share a session '
                       'with another user, this user name will be displayed with the shared session. We will not sell '
                       'or distribute your user name or institution to third parties. When you log in, the client IP '
                       'address is recorded. This IP address can be correlated with the address automatically '
                       'collected as noted above. If your user profile personally identifies you, then it may be '
                       'possible to associate you with your detailed activity on the ConPlot website.',
                       style={"text-align": "justify"}),
                html.Br(),
                html.H4('4. "Get in Touch" Form'),
                html.P('The header on each ConPlot site includes a “Get in Touch” link to a form where users can '
                       'submit general inquiries, bug reports or request assistance if they forget their passwords. '
                       'Submissions through this form are emailed to members of the Rigden Lab at the University of '
                       'Liverpool. The form includes a field for an email address. If the email address identifies you '
                       'personally, say if you use your institutional email, then your correspondence with us will '
                       'likewise be linked to you. A valid email is not strictly required, although we cannot reply to '
                       'you without one. When you submit the form, your IP address and browser version will be '
                       'recorded for internal use. In the case of reported bugs or other site errors, this '
                       'information may be used by technical staff to help locate your session in the server logs to '
                       'aid in troubleshooting the issue. This does have the side effect of making it possible to '
                       'associate an IP address with an email address which may, in turn, personally identify you. '
                       'However, ConPlot does not publicly release this information.', style={"text-align": "justify"}),
                html.Br(),
                html.H4('5. How ConPlot uses cookies'),
                html.P('ConPlot uses cookies to associate multiple requests by your web browser into a stateful '
                       'session. Cookies are essential to track the state of session. Some cookies persist only for a '
                       'single session. The information is recorded temporarily and is erased when the user quits the '
                       'session or closes the browser. Others may be persistently stored on the hard drive of your '
                       'computer until you manually delete them from a browser folder or until they expire, which can '
                       'be months after they were last used. Cookies can be disabled in your browser (refer to your '
                       'browser’s documentation for instructions); however, the majority of the website functionality '
                       'will be unavailable if cookies are disabled.', style={"text-align": "justify"}),
                html.Br(),
                html.H4('6. Your Rights based on the General Data Protection Regulation (GDPR)'),
                html.P(['If you wish to know more about your rights under the General Data Protection Regulation '
                        '(GDPR), you can do this ', html.A(html.U('here'), href=UrlIndex.GDPR_WEBSITE.value),
                        '. Here is a summary of what this includes:'],
                       style={"text-align": "left"}),
                GdprRightsList(),
            ], justify='center', align='center', className='m-0'),
        ]),
    ], id='gdpr-policy-modal', is_open=False, size='xl', scrollable=True, centered=True, autoFocus=True)


def TutorialOneModal():
    return dbc.Modal([
        dbc.ModalHeader('Tutorial 1: Creating your first plot'),
        dbc.ModalBody(['Tutorial goes here'])
    ], id={'type': 'tutorial-modal', 'index': 1}, is_open=False, size='xl', scrollable=True, centered=True,
        autoFocus=True)


def TutorialTwoModal():
    return dbc.Modal([
        dbc.ModalHeader('Tutorial 2: Storing and loading a session'),
        dbc.ModalBody(['Tutorial goes here'])
    ], id={'type': 'tutorial-modal', 'index': 2}, is_open=False, size='xl', scrollable=True, centered=True,
        autoFocus=True)


def TutorialThreeModal():
    return dbc.Modal([
        dbc.ModalHeader('Tutorial 3: Sharing a session'),
        dbc.ModalBody(['Tutorial goes here'])
    ], id={'type': 'tutorial-modal', 'index': 3}, is_open=False, size='xl', scrollable=True, centered=True,
        autoFocus=True)


def TutorialFourModal():
    return dbc.Modal([
        dbc.ModalHeader('Tutorial 4: Getting in touch with us'),
        dbc.ModalBody(['Tutorial goes here'])
    ], id={'type': 'tutorial-modal', 'index': 4}, is_open=False, size='xl', scrollable=True, centered=True,
        autoFocus=True)
