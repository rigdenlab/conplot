import components
import dash_bootstrap_components as dbc
import dash_html_components as html
from utils import UrlIndex, color_palettes


def MismatchModal(*args):
    return dbc.Modal([
        ModalHeader("Mismatch Detected"),
        dbc.ModalBody([
            html.P("""We were unable to match the uploaded sequence with the following prediction files. Please 
                ensure that these predictions correspond with the protein sequence in the uploaded FASTA file.""",
                   style={'text-align': "justify"}),
            html.Ul([html.Li('%s' % arg) for arg in args], id='mismatched-fnames-div')
        ])
    ], id='mismatch-modal', is_open=True)


def MismatchDatasetModal(fname, seq_fname):
    return dbc.Modal([
        ModalHeader("Mismatch Detected"),
        dbc.ModalBody([
            html.P("""We were unable to match the sequence at {} with the data at the file {}. Please 
                ensure that the file you attempt to upload corresponds with the protein sequence 
                in the provided FASTA file.""".format(seq_fname, fname), style={'text-align': "justify"}),
        ])
    ], id='mismatch-dataset-modal', is_open=True)


def MismatchSequenceModal(*args):
    return dbc.Modal([
        ModalHeader("Sequence Mismatch"),
        dbc.ModalBody([
            html.P("""We were unable to match the uploaded sequence with datasets in the following files. 
            Please ensure that the provided sequence corresponds with the structure described in these datasets.""",
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


def InvalidSuperposeDistanceMatrixModal():
    return dbc.Modal([
        ModalHeader("Invalid Input"),
        dbc.ModalBody([
            html.P("""Superposition of heatmaps is not supported yet!""",
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
            html.P("""More than 60 minutes have passed since you last interacted with the website and your session has 
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
            format of your file is correct, please report the bug on the 'Get in touch with us' tab.""",
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


def SuccessCreateUserModal(username):
    return dbc.Modal([
        ModalHeader(html.H4("Success", className="alert-heading", style={'color': 'green'})),
        dbc.ModalBody(
            html.P("""You have successfully created a new user. You are now logged in as {}.""".format(username),
                   style={'text-align': "justify"})
        ),
    ], id='success-contact-form-modal', is_open=True)


def CustomFormatDescriptionModal():
    return dbc.Modal([
        dbc.ModalHeader('Custom Format Specifications'),
        dbc.ModalBody([
            dbc.Row([
                html.P('Custom files can be used to add personalised tracks to your plots. These files are plain text '
                       'files, and can be created manually in Notepad++ or similar text editors. The first line of '
                       'this file should start with the flag "LEN", followed by the length of the protein sequence '
                       'that this file is intended to be used with. Subsequent lines indicate records to be added in '
                       'the track, each defined using three fields, which are separated by white spaces:',
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
            'This tutorial serves as a walk-through of how to create a plot using ConPlot. We will be using data '
            'corresponding with the Uniprot entry ', html.I('W9DY28'),
            ', a putative membrane protein. This data can be downloaded ',
            html.A(html.U('here'), href=UrlIndex.EXAMPLE_DATA.value),
            '. First, use the navigation bar on top of the website to access the ',
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
                         'in this case that will be ', html.I('W9DY28.FASTA')]),
                html.Li(['Click on the ', html.I('Format'),
                         ' dropdown menu  highlighted in red to select the format of the contact map that '
                         'you will be uploading. In this case, that will be ', html.I('PSICOV'),
                         ' format. You will see dropdown menus colored in red like this one all over '
                         'ConPlot everytime this input is required before moving to the stage of uploading '
                         'a file.']),
                html.Li(['Click on ', html.I('UPLOAD CONTACT'),
                         ' to upload a contact map file, in this case that will be the file ',
                         html.I('W9DY28.PSICOV'),
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
            'memory -but do not do this now. As you have already uploaded the input required to create a minimal '
            'contact map plot, if you click on ', html.I('Generate Plot'),
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
            'predictions using the designated area in the input panel. If you scroll down the input panel, you will '
            'see the ', html.I('Additional Tracks'),
            ' input area. Again, here you will be presented with a format selection menu highlighted in red, '
            'indicating that we will need to select a format before uploading the first file. You have been provided '
            'with five files in the example data that you can upload in this section, the order at which you do this '
            'will not affect the output:',
            html.Ul([
                html.Li(['TOPCONS (membrane topology prediction): W9DY28.TOPCONS']),
                html.Li(['PSIPRED (secondary structure prediction): W9DY28.SS2']),
                html.Li(['CONSURF (sequence conservation): W9DY28.CONSURF']),
                html.Li(['IUPRED (sequence disorder prediction): W9DY28.IUPRED']),
                html.Li(['CUSTOM (custom track data file): W9DY28.CUSTOM'])
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
            'tweak the exact way the plot looks, you can read all about these on section ',
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
            'You have now created a contact map that integrates several sources of information on the diagonal, '
            'allowing easy visual cross-referencing of multiple sources. However, you may have noticed that sometimes '
            'it can result difficult to map a specific contact with its corresponding annotations on the diagonal. '
            'To get around this, you can try activating the ', html.I("Toggle spike lines"),
            ' on the mode bar at the top right corner of the plot:',
            html.Img(src=UrlIndex.TUTORIAL1_FIG8.value, height='100vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            html.Br(),
            'When this button is active, horizontal and vertical spike lines appear when hovering on top of a contact, '
            'allowing you to map it to its position in the diagonal. Alternatively, the tooltip text that appears when '
            'hovering on top of a contact can be changed to display all the additional information available for the '
            'specific residues involved on each contact by activating the ', html.I("Verbose labels"),
            ' switch at the ', html.I('Display Control Panel'), ' on the right of the plot.',
            html.Img(src=UrlIndex.TUTORIAL1_FIG9.value, height='400vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            html.Br(),
            'You may have also noticed the ', html.I('Create heatmap'), ' switch right on top of the ',
            html.I("Verbose labels"),
            ' one. By activating this switch, users can choose to display their contact information as a heatmap where '
            'all the contacts present in the uploaded file are displayed coloured according to the confidence assigned '
            'to each specific contact. This mode becomes specially relevant when visualising residue-residue distance '
            'predictions, as you will see in ', html.I('Tutorial 4. Residue-Residue distance predictions'), '.',
            html.Img(src=UrlIndex.TUTORIAL1_FIG10.value, height='500vh', className='mt-3',
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
        dbc.ModalHeader('Tutorial 2: Compare a contact prediction with a PDB file'),
        dbc.ModalBody([
            'With ConPlot, it is possible to superimpose a reference contact map and a secondary contact map '
            'into the same plot. ConPlot well then highlight in red the mismatches, in black the matching contacts and '
            'in grey the contacts only present in the reference map. This can be used if you wish to compare two '
            'different prediction methods, but it has also wider applications since ConPlot can also extract the '
            'contacts present in a structure described on a PDB file. Thus, if you provide a PDB file for the role of '
            'reference map and a predicted map for the secondary map, ConPlot can be used to evaluate the precision '
            'of the prediction method of interest, or for the validation of models obtained through ',
            html.I('ab initio'),
            " modelling and predicted residue contacts. To showcase this functionality, we will be using data from "
            "protein TOXD, an alpha-dendrotoxin. You can download this data ",
            html.A(html.U('here'), href=UrlIndex.EXAMPLE_DATA.value),
            ". The data includes the crystal structure of this toxin -a PDB file-, its sequence -a FASTA file- "
            "and a contact prediction map in ccmpred format -a MAT file-. First, access the ", html.I('Plot'),
            " tab and upload the sequence fasta file as you have done on the previous tutorial. Then, proceed to "
            "select the ", html.I('CCMPRED'), " contact map format and upload the file ", html.I('toxd.mat'),
            ' in the contact map upload section. Do the same with the file ', html.I('toxd.pdb'),
            ' but remember to change the contact format to ', html.I('PDB'),
            ' first. Once you have done this, simply click on ', html.I('Generate Plot'),
            ' to create a plot as described on previous tutorial. By default, ConPlot will display the first contact '
            'map you uploaded. For example, in this case we first uploaded ', html.I('toxd.mat'),
            ' so ConPlot created a plot using the contacts found in this file:',
            html.Img(src=UrlIndex.TUTORIAL2_FIG1.value, height='500vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            html.Br(),
            'However, for the purpose of comparing both maps, we would like to change that: we need '
            'ConPlot to compare the predicted contacts in the ', html.I('todx.mat'),
            ' file using the residue contacts derived on the crystal structure at the ', html.I('toxd.pdb'),
            ' file as a reference. To do this, you will need to use the ', html.I('Map A'), ' and ', html.I('Map B'),
            ' selectors on the ', html.I('Display Control'),
            ' panel. By default, these selectors control which map is displayed on each half of the map -you can try '
            'to change these values now and click on ', html.I('Adjust Plot'),
            ' button to experiment with this. However, the role of these selectors changes when you turn on the ',
            html.I('Superimpose Maps'), ' switch. Then, ConPlot will use the selection on the ', html.I('Map A'),
            ' as the reference map, and the selection on ', html.I('Map B'),
            ' as the secondary map. Thus, if we want to compare the ', html.I('todx.mat'),
            ' prediction with the ground truth at the ', html.I('toxd.pdb'),
            ' crystal structure, you will need to select ', html.I('toxd.pdb'), ' as ', html.I('Map A'), ' and ',
            html.I('todx.mat'), ' as ', html.I('Map B'),
            '. Then, turn on the ', html.I('Superimpose Maps'),
            ' switch. Before creating the new plot, you may also want to increase the size of the contact markers '
            'to 7 and set the L/N selector to 1 for better clarity of the plot:',
            html.Img(src=UrlIndex.TUTORIAL2_FIG2.value, height='350vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            html.Br(),
            'Now click on ', html.I('Adjust Plot'),
            '. ConPlot will then create a superimposed map, with matching contacts coloured in solid black, mismatches '
            'in red and contacts only present in the reference map in grey.',
            html.Img(src=UrlIndex.TUTORIAL2_FIG3.value, height='500vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            html.Br(),
        ])
    ], id={'type': 'tutorial-modal', 'index': 2}, is_open=False, size='xl', scrollable=True, centered=True,
        autoFocus=True)


def TutorialThreeModal():
    return dbc.Modal([
        dbc.ModalHeader('Tutorial 3: Storing, loading and sharing a session'),
        dbc.ModalBody([
            'In this tutorial you will learn about how to create an user account in ConPlot, that then can be used '
            'to store data, and share it among your collaborators. First thing is to create an user account in '
            'ConPlot. To do this, first click on the ', html.I('LOGIN'),
            ' dropdown menu on the top right of the website. This menu will let you access the user portal and the '
            'members only area -only available once you login.',
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
            html.I('LOGIN'), ' dropdown menu and select the ', html.I('Access Personal Storage'),
            ' option. This will take you to a list of all the sessions that you have saved with your user account, plus '
            'those that have been shared with you:',
            html.Img(src=UrlIndex.TUTORIAL3_FIG5.value, height='500vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            'As you can see, in this case we can see the EXAMPLE session that we just stored. To load any of the '
            'sessions listed here, simply click on the load button. Alternatively, if you wish to delete '
            'a session, click on the delete button. Notice how there is another section for those '
            'sessions that have been shared with your user. This section is likely to be empty as you just created '
            'your user, but as your collaborators start to use ConPlot as well, this functionality can become an easy '
            'way to share data across other lab members. To share a session with another user, click again on the ',
            html.I('LOGIN'), ' dropdown menu and select the ', html.I('Share Sessions'),
            ' option. This will take you to a list of all the sessions that you have saved with your user account. '
            'Next to each item, there is a text box that you can use to write the name of the user that you want to '
            'share that particular session with, and a share button.',
            html.Img(src=UrlIndex.TUTORIAL3_FIG6.value, height='500vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            'Once you share a session with another user, they will be able to see this session listed in their '
            'personal storage. For example, in the following image, ', html.I('user_2'),
            ' has access to the example session as it has been shared by ', html.I('user_1'), '.',
            html.Img(src=UrlIndex.TUTORIAL3_FIG7.value, height='500vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            'In the same way as you can do with your own stored sessions, if you want to load a shared session simply '
            'click on the load button. However, please note that you will not be able to delete shared '
            'sessions -this can only be done by the owner of the session. Instead, you may click on the stop button '
            'to stop sharing that session -this way it will not appear on your personal storage '
            'anymore-. Also please note that session sharing is dynamic, which means that as the owner of the session '
            'adds/removes files from the session, those users with shared access will be able to see these changes '
            '-but only the session owner can make changes on the session.', html.Br(), html.Br()
        ])
    ], id={'type': 'tutorial-modal', 'index': 3}, is_open=False, size='xl', scrollable=True, centered=True,
        autoFocus=True)


def TutorialFourModal():
    return dbc.Modal([
        dbc.ModalHeader('Tutorial 4: Residue-Residue Distance Predictions'),
        dbc.ModalBody([
            "In this tutorial, you will learn how to use ConPlot's heatmap mode, which allows you to visualise data "
            "derived from residue-residue distance predictions. These files contain information about real value "
            "distances predicted between residue pairs, and are becoming increasingly popular in the field of "
            "structural bioinformatics. We will be using the same data used in ",
            html.I("Tutorial 1. Creating your first plot"),
            ", which corresponds with Uniprot entry ", html.I("W9DY28"),
            ", a putative membrane domain. Remember that tutorial data can be downloaded ",
            html.A(html.U('here'), href=UrlIndex.EXAMPLE_DATA.value),
            ". First, let's start by uploading the following data:",
            html.Ul([
                html.Li(['Click on ', html.I('UPLOAD SEQUENCE'),
                         ' to upload a FASTA file with the sequence of the protein of interest, '
                         'in this case that will be ', html.I('W9DY28.FASTA')]),
                html.Li(['Click on the ', html.I('Format'),
                         ' dropdown menu highlighted in red to select the format of the contact information file that '
                         'you will be uploading. In this case, that will be ', html.I('CASPRR_MODE2'),
                         ' format. This is the format used by ConPlot to upload residue-residue distance prediction '
                         'files, a description of this format can be found ',
                         html.A(html.U('here'), href=UrlIndex.CASP14_RRFORMAT.value), '.']),
                html.Li(['Click on ', html.I('UPLOAD CONTACT'),
                         ' to upload a contact prediction file, in this case that will be the file ',
                         html.I('W9DY28.CASPRR_2')])
            ]),
            'You can now optionally upload the same prediction files that wre used on ',
            html.I('Tutorial 1.Creating your first plot'),
            ' if you wish to have the same data displayed on the diagonal this time, and then and click on ',
            html.I('Generate Plot'),
            ' to create a plot. As you can see, by default ConPlot will generate a contact map based on the '
            'information present on the uploaded file. However, we are only looking at a small fraction of the data '
            'contained in the ', html.I('CASPRR MODE2'),
            ' which also informs about predicted real-value residue-residue distances. To display this information, we '
            'can turn on the ', html.I('Create heatmap'), ' switch on the ', html.I('Display Control'),
            ' panel and then click on the ', html.I('Adjust plot'), ' button.',
            html.Img(src=UrlIndex.TUTORIAL4_FIG1.value, height='400vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            html.Br(),
            'As you can see, a distogram with the residue-residue distance prediction is displayed in place of the '
            'default contact map. In these representations, contacts are coloured according to the predicted distance '
            'of each specific pair of residues. You may also notice that the predicted distance between residue pairs '
            'has been added to the tooltip text that appears when you hover on top of a given contact.',
            html.Img(src=UrlIndex.TUTORIAL4_FIG2.value, height='500vh', className='mt-3',
                     style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
            html.Br(),
        ])
    ], id={'type': 'tutorial-modal', 'index': 4}, is_open=False, size='xl', scrollable=True, centered=True,
        autoFocus=True)


def TutorialFiveModal():
    return dbc.Modal([
        dbc.ModalHeader('Tutorial 5: Video Tutorial'),
        dbc.ModalBody([
            'Below there is a short video tutorial with an overview of the main ConPlot features. ',
            html.Br(),
            html.Br(),
            html.Iframe(width=1100, height=630, src=UrlIndex.YOUTUBE_EMBED.value,
                        style={'frameborder': 0, 'allow': "accelerometer; autoplay; clipboard-write; "
                                                          "encrypted-media; gyroscope; picture-in-picture"}),
            html.Br(),
            'If you cannot see the video click ', html.A(html.U('here'), href=UrlIndex.YOUTUBE_LINK.value), '.'
        ])
    ], id={'type': 'tutorial-modal', 'index': 5}, is_open=False, size='xl', scrollable=True, centered=True,
        autoFocus=True)


def RedisConnectionErrorModal():
    return dbc.Modal([
        ModalHeader("Redis connection error"),
        dbc.ModalBody([
            html.P(["It was impossible to connect with Redis database. If you are using ConPlot web services on ",
                    html.I('www.conplot.org'),
                    " we are probably taking a look at this already. If the problem  persists after a few hours, "
                    "please report this issue on our ", html.A(html.U('Github repository'), href=UrlIndex.GITHUB.value),
                    ". Alternatively, if you are running ConPlot on localhost please ensure that redis server "
                    "is running and that the URL for the connection is available as an environment variable "
                    "called KEYDB_URL as explained on our ",
                    html.A(html.U('Github repository'), href=UrlIndex.GITHUB_ISSUE.value), "."],
                   style={'text-align': "justify"}),
            components.StartNewSessionLink()
        ]),
    ], id='redis-connection-error-modal', is_open=True, backdrop='static', keyboard=False)


def PostgresConnectionErrorModal():
    return dbc.Modal([
        ModalHeader("PostgreSQL connection error"),
        dbc.ModalBody([
            html.P(["It was impossible to connect with PostgreSQL database. If you are using ConPlot web services on ",
                    html.I('www.conplot.org'), " please report this issue ",
                    dbc.CardLink(html.U('here'), href=UrlIndex.CONTACT.value),
                    ". Alternatively, if you are running ConPlot on localhost please remember that it is not "
                    "possible to use user account related features when running ConPlot on this mode."],
                   style={'text-align': "justify"}),
            components.StartNewSessionLink()
        ]),
    ], id='postgres-connection-error-modal', is_open=True, backdrop='static', keyboard=False)


def ExampleSessionConnectionErrorModal():
    return dbc.Modal([
        ModalHeader("PostgreSQL connection error"),
        dbc.ModalBody([
            html.P(['It was impossible to connect with PostgreSQL database in order to get the example session. If '
                    'you are using ConPlot web services on ', html.I('www.conplot.org'),
                    ' please report this issue in the "Get in touch" tab. While we fix this, you can download the '
                    'example data ', dbc.CardLink(html.U('here'), href=UrlIndex.EXAMPLE_DATA.value), "."],
                   style={'text-align': "justify"}),
        ]),
    ], id='example-session-error-modal', is_open=True)


def SlackConnectionErrorModal():
    return dbc.Modal([
        ModalHeader("Helpdesk connection error"),
        dbc.ModalBody([
            html.P(["It was impossible to connect with ConPlot helpdesk. If you are using ConPlot web services on ",
                    html.I('www.conplot.org'), " please report this issue on our ",
                    html.A(html.U('Github repository'), href=UrlIndex.GITHUB.value),
                    ". Alternatively, if you are running ConPlot on localhost please remember that it is not "
                    "possible to get in touch with us when running ConPlot on this mode."],
                   style={'text-align': "justify"}),
        ]),
    ], id='slack-connection-error-modal', is_open=True)


def ContactWrongAccountModal():
    return dbc.Modal([
        dbc.ModalHeader(
            html.H4('Wrong account details', className="alert-heading", style={'color': 'red'})),
        dbc.ModalBody(
            html.P("""We cannot match the information you provided with any account on our database. If you wish to 
            recover your password please make sure to provide the same email address and username you have registered 
            when creating the account.""", style={'text-align': "justify"})
        ),
    ], id='slack-fail-recovery-modal', is_open=True)


def ContactRecoverAccountModal():
    return dbc.Modal([
        dbc.ModalHeader(
            html.H4('Account recovery', className="alert-heading", style={'color': 'green'})),
        dbc.ModalBody(
            html.P("""We have sent a message to your email address with further instructions to reset your password. 
            PLEASE MAKE SURE TO CHECK YOUR SPAM FOLDER.""", style={'text-align': "justify"})
        ),
    ], id='slack-success-recovery-modal', is_open=True)


def PaletteModal(dataset, idx):
    palette_dict = {}
    palette_list = []
    for palette in color_palettes.DatasetColorPalettes.__getitem__(dataset).value:
        palette_list.append(palette.name)
        palette_dict[palette.name] = []
        for color in palette.value:
            palette_dict[palette.name].append((color.name, color.value.format(0.5)))

    modal_body = []
    for palette in palette_list:
        modal_body.append(dbc.Row(html.H4(palette, style={'font-weight': 'bold'}), align='center', justify='center'))
        modal_body.append(html.Br())
        row = dbc.Row([
            dbc.ListGroup([
                dbc.ListGroupItem(
                    dbc.Row([
                        color[0]
                    ], justify='center', align='center'), style={'background-color': color[1], 'font-weight': 'bold'}
                ) for color in palette_dict[palette]
            ], style={'width': '55%'})
        ], justify='center', align='center')
        modal_body.append(row)
        modal_body.append(html.Br())
        modal_body.append(html.Br())

    return dbc.Modal([
        dbc.ModalHeader('{} colour palettes'.format(components.UserReadableTrackNames.__getitem__(dataset).value)),
        dbc.ModalBody(modal_body)
    ], is_open=False, size='xl', scrollable=True, centered=True, autoFocus=True,
        id={'type': 'palette-modal', 'index': idx})


def SuccessRecoverAccount():
    return dbc.Modal([
        dbc.ModalHeader(
            html.H4('Successful password reset', className="alert-heading", style={'color': 'green'})),
        dbc.ModalBody(
            html.P("""You have successfully changed your password. Please head back to the login page and try to
            login with your new details.""", style={'text-align': "justify"})
        ),
    ], id='success-recovery-modal', is_open=True)


def FailureRecoverAccount():
    return dbc.Modal([
        dbc.ModalHeader(
            html.H4('Password reset failed', className="alert-heading", style={'color': 'red'})),
        dbc.ModalBody(
            html.P("""Your attempt to reset your password has failed. Please check the spelling of your username, 
            email address and the verification code. You can find the verification code in the message that was sent 
            to your registered email address.""", style={'text-align': "justify"})
        ),
    ], id='fail-recovery-modal', is_open=True)


def InvalidPasswordRecoverAccount():
    return dbc.Modal([
        dbc.ModalHeader(
            html.H4('Passwords do not match', className="alert-heading", style={'color': 'red'})),
        dbc.ModalBody(
            html.P("""Please make sure to type the same password when in the 'Confirm Password' input box.""",
                   style={'text-align': "justify"})
        ),
    ], id='fail-recovery-modal', is_open=True)
