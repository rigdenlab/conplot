import components
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
            components.StartNewSessionLink()
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
                components.CustomFormatFieldsHelpList(),
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
                components.GdprPolicySectionOne(),
                html.Br(),
                html.H4('2. Information Automatically Collected'),
                components.GdprPolicySectionTwo(),
                html.Br(),
                html.H4('3. Information You Directly Provide'),
                components.GdprPolicySectionThree(),
                html.Br(),
                html.H4('4. "Get in Touch" Form'),
                components.GdprPolicySectionFour(),
                html.Br(),
                html.H4('5. How ConPlot uses cookies'),
                components.GdprPolicySectionFive(),
                html.Br(),
                html.H4('6. Your Rights based on the General Data Protection Regulation (GDPR)'),
                components.GdprPolicySectionSix(),
                components.GdprRightsList(),
            ], justify='center', align='center', className='m-0'),
        ]),
    ], id='gdpr-policy-modal', is_open=False, size='xl', scrollable=True, centered=True, autoFocus=True)


def TutorialOneModal():
    return dbc.Modal([
        dbc.ModalHeader('Tutorial 1: Creating your first plot'),
        dbc.ModalBody([
            'First, use the navigation bar on top of the website to access the ',
            html.I('Plot'), ' tab. Then, you will be presented with the following website:',
            html.Img(src=UrlIndex.TUTORIAL1_FIG1.value, height='500vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            html.Br(),
            'From here, you will be able to upload your data and integrate it into a plot. The minimal input that '
            'ConPlot requires to be able to generate a plot is a protein sequence -in a FASTA file- and a residue '
            "contact prediction file -a contact map in one of the supported formats-. Let's start by uploading these "
            'files using the input panel on the left of the page as follows:',
            html.Ul([
                html.Li(['Click on ', html.I('UPLOAD SEQUENCE'),
                         ' to upload a FASTA file with the sequence of the protein of interest, '
                         'in this case that will be ', html.I('EXAMPLE.FASTA')]),
                html.Li(['Click on the ', html.I('Format'),
                         ' dropdown menu  highlighted in red to select the format of the contact map that '
                         'you will be uploading. In this case, that will be ', html.I('PSICOV'),
                         ' format. You will see dropdown menus colored in red like this one all over '
                         'ConPlot everytime this input is required before moving to the stage of uploading '
                         'a file.']),
                html.Li(['Click on ', html.I('UPLOAD CONTACT'),
                         ' to upload a contact map file, in this case that will be the file ',
                         html.I('EXAMPLE.PSICOV'),
                         '. Please note that this file is follows the PSICOV format, just as we indicated '
                         'previously with the dropdown menu.'])
            ]),
            'You will notice that as you upload files, green file banners have appeared in the input panel as shown '
            'below: ',
            html.Img(src=UrlIndex.TUTORIAL1_FIG2.value, height='500vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            html.Br(),
            "This banners represent the space allocated for the uploaded file in ConPlot's memory, if you wish to "
            'remove any of them simply click on the cross on the right side of the banner to remove them from the '
            'memory. As you have already uploaded the input required to create a minimal contact map plot, if you '
            'click on ', html.I('Generate Plot'),
            ', you will generate a contact map plot without any additional information, as shown in this figure:',
            html.Img(src=UrlIndex.TUTORIAL1_FIG3.value, height='500vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            html.Br(),
            'If you wish to download the figure as a ', html.I('png'),
            ' file, simply click on the camera icon on the mode bar at the top right of the plot -this mode bar will '
            'only appear when you hover around the top right area of the plot-. You will be able to do this anytime '
            'as you add information to the plot or you adjust its layout.',
            html.Img(src=UrlIndex.TUTORIAL1_FIG4.value, height='300vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            html.Br(),
            'Next, in order to add more tracks of information to the plot, we will upload the example sequence '
            'predictions using the designated are in the input panel. If you scroll down the input panel, you will '
            'see the ', html.I('Additional Trakcs'),
            ' input area. Again, here you will be presented with a format selection menu highlighted in red, '
            'indicating that we will need to select a format before uploading the first file. You have been provided '
            'with five files in the example data that you can upload in this section, the order at which you do this '
            'will not affect the output:',
            html.Ul([
                html.Li(['TOPCONS (membrane topology prediction): EXAMPLE.TOPCONS']),
                html.Li(['PSIPRED (secondary structure prediction): EXAMPLE.SS2']),
                html.Li(['CONSURF (sequence conservation): EXAMPLE.CONSURF']),
                html.Li(['IUPRED (sequence disorder prediction): EXAMPLE.IUPRED']),
                html.Li(['CUSTOM (custom track data file): EXAMPLE.CUSTOM'])
            ]),
            'Again, as you upload files green banners will appear depicting the storage allocated to each file.',
            html.Img(src=UrlIndex.TUTORIAL1_FIG5.value, height='500vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            html.Br(),
            'Once you upload all these files, click again on ', html.I('GENERATE PLOT'),
            ' to generate a plot that includes all the information you just uploaded:',
            html.Img(src=UrlIndex.TUTORIAL1_FIG6.value, height='500vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            html.Br(),
            'As you can see, due to the characteristics of this particular protein, the size of the tiles '
            'is not big enough so that they will overlay to form a continuous line. This might be the '
            'desired effect for some users, but if you are looking after solid lines in the diagonal of the '
            'plot you are likely to need to use some of the controls on the right of the plot. You may have '
            'noticed that since you generated the first bare contact map a display control panel appeared '
            'on the right of the plot. This panel contains numerous switches and menus that will let you '
            'tweak the exact way the plot looks, you can read all about these on section',
            html.I('4. Adjust the plot layout'),
            '. In this particular case, since we are interested in making the tiles big enough that they will overlay '
            'into a continuous solid line, you will need to adjust the size of the additional tracks: increase its '
            'value from the default 5 to 7. After doing this, click on the ', html.I('Adjust Plot'),
            ' button down below the display control panel. Please note that you did not click on the ',
            html.I('Generate Plot'),
            ' button beneath the input panel, that button is only used if you would like to generate a new '
            'plot after uploading more data to ConPlot. Since we did not upload more data, we are just adjusting the '
            'way the plot looks, we click on ', html.I('Adjust Plot'), '.',
            html.Img(src=UrlIndex.TUTORIAL1_FIG7.value, height='500vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            html.Br(),
            'That will be all for this tutorial, now you are able to create a plot that integrates several '
            'sources of information with you residue contact predictions. This representations are an '
            'effective way of visualising your data at a glance, but notice how you will loose this '
            'information unless you download the picture as a ', html.I('png'),
            ' file. Nevertheless, ConPlot provides you a way to store the uploaded information permanently '
            'within our data stores. For this, you will need to follow with the next tutorial to learn '
            'how to create an user account and store sessions!', html.Br(), html.Br()
        ])
    ], id={'type': 'tutorial-modal', 'index': 1}, is_open=False, size='xl', scrollable=True, centered=True,
        autoFocus=True)


def TutorialTwoModal():
    return dbc.Modal([
        dbc.ModalHeader('Tutorial 2: Contact prediction evaluation'),
        dbc.ModalBody([
            'It is possible to evaluate the precision of your contact prediction using ConPlot. This might result '
            'useful in different situations.'


        ])
    ], id={'type': 'tutorial-modal', 'index': 2}, is_open=False, size='xl', scrollable=True, centered=True,
        autoFocus=True)


def TutorialThreeModal():
    return dbc.Modal([
        dbc.ModalHeader('Tutorial 3: Storing, loading and sharing a session'),
        dbc.ModalBody([
            'First thing is to create an user account in ConPlot. To do this, first click on the ', html.I('LOGIN'),
            ' dropdown menu on the top right of the website. This menu will let you access the user portal and the '
            'members only area -only available once you login-.',
            html.Img(src=UrlIndex.TUTORIAL3_FIG1.value, height='300vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            html.Br(),
            'By clicking on ', html.I('Create a new account'), ' you will be redirected to the new users area:',
            html.Img(src=UrlIndex.TUTORIAL3_FIG2.value, height='500vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            'Here you can create a new user by providing an user name, a password and an email. We will only use this '
            'email address to get in touch with you in case your forget your or you request assistance from us. Also '
            'please note that both the user name and the email need to be unique, i.e. they cannot be already in use '
            'in our system. A valid email is not strictly required as we do not validate the email address you '
            'provide, but please note that you will need access to this email in case you forget your password. Once '
            'you provide all the required information a green banner will appear informing you that you have now '
            'created an user account. As an user of ConPlot you can now store sessions on your personal storage and '
            'retrieve the data whenever you want. You will also be able to share this data among your collaborators '
            "registered in ConPlot if you wish to. Let's start by storing a session. If you just completed tutorial 1, "
            'you will now have uploaded to ConPlot the example files and created a plot to visualise this data. '
            'Thus, if you head back to the ', html.I('Plot'),
            ' area you will be able to see the files you just uploaded. Since you have created an user account and you '
            'are logged in, if you scroll down to the bottom of the input panel you will see that the input panel to '
            'store the current session has been unlocked: ',
            html.Img(src=UrlIndex.TUTORIAL3_FIG3.value, height='500vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            html.Br(),
            'Fill in the text box with the name you want to use to identify the saved session and click on the button '
            'with the save icon. A green alert will appear letting you now that the operation was a success. Now you '
            'have stored the data you uploaded in this session, it will be stored for you permanently so that you can '
            'come back and re-visit it whenever you want.',
            html.Img(src=UrlIndex.TUTORIAL3_FIG4.value, height='500vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            html.Br(),
            'If you want to check out any session that you have saved following this method, click again on the ',
            html.I('LOGIN'), 'dropdown menu and select the ', html.I('Access Personal Storage'),
            'option. This will take you to a list of all the sessions that you have saved with your user account, plus '
            'those that have been shared with you:',
            html.Img(src=UrlIndex.TUTORIAL3_FIG5.value, height='500vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            'As you can see, in this case we can see the EXAMPLE session that we just stored. To load any of the '
            'sessions listed here, simply click on the button with the disk icon. Alternatively, if you wish to delete '
            'a session, click on the button with the trash icon. Notice how there is another section for those '
            'sessions that have been shared with your user. This section is likely to be empty as you just created '
            'your user, but as your collaborators start to use ConPlot as well, this functionality can become an easy '
            'way to share data across other lab members. To share a session with another user, click again on the ',
            html.I('LOGIN'), 'dropdown menu and select the ', html.I('Share Sessions'),
            'option. This will take you to a list of all the sessions that you have saved with your user account. Next '
            'to each item, there is a text box that you can use to write the name of the user that you want to share '
            'that particular session with, and a share button.',
            html.Img(src=UrlIndex.TUTORIAL3_FIG6.value, height='500vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            'Once you share a session with another user, they will be able to see this session listed in their '
            'personal storage. For example, in the following image, ', html.I('user_2'),
            ' has access to the example session as it has been shared by ', html.I('user_1'), '.',
            html.Img(src=UrlIndex.TUTORIAL3_FIG7.value, height='500vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            'In the same way as you can do with your own stored sessions, if you want to load a shared session simply '
            'click on the button with the disk icon. However, please note that you will not be able to delete shared '
            'sessions -this can only be done by the owner of the session-. Instead, you may click on the button with '
            'the stop icon to stop sharing that session -this way it will not appear on your personal storage '
            'anymore-. Also please note that session sharing is dynamic, which means that as the owner of the session '
            'adds/removes files from the session, those users with shared access will be able to see these changes '
            '-but only the session owner can make changes on the session-.', html.Br(), html.Br()
        ])
    ], id={'type': 'tutorial-modal', 'index': 3}, is_open=False, size='xl', scrollable=True, centered=True,
        autoFocus=True)
