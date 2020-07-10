from components import ShareWithInput, SessionListType
import dash_bootstrap_components as dbc
import dash_html_components as html
from utils import sql_utils, UrlIndex


def SessionListItem(session, list_type, color='secondary'):
    if list_type == SessionListType.SHARED:
        button_group = dbc.ButtonGroup([
            dbc.Button(html.I(className="fas fa-save"), outline=True, color='primary',
                       id={'type': 'load-share-session-button', 'index': session.pkid}),
            dbc.Button(html.I(className="fas fa-ban"), outline=True, color='danger', className="ml-1",
                       id={'type': 'stop-share-session-button', 'index': session.pkid})
        ], className="btn-toolbar")
        session_label = "%s - %s" % (session.owner, session.name)
    elif list_type == SessionListType.TO_SHARE:
        button_group = dbc.ButtonGroup([
            html.Div(id={'type': 'share-session-toast-div', 'index': session.pkid}),
            ShareWithInput(id={'type': 'share-username-input', 'index': session.pkid}),
            dbc.Button(html.I(className="fas fa-share-alt"), outline=True, color='primary', size='sm',
                       id={'type': 'share-session-button', 'index': session.pkid}),
        ], className="btn-toolbar")
        session_label = session.name
    else:
        button_group = dbc.ButtonGroup([
            dbc.Button(html.I(className="fas fa-save"), outline=True, color='primary',
                       id={'type': 'load-session-button', 'index': session.pkid}),
            dbc.Button(html.I(className="fas fa-trash-alt"), outline=True, color='danger', className="ml-1",
                       id={'type': 'delete-session-button', 'index': session.pkid})
        ], className="btn-toolbar")
        session_label = session.name

    return dbc.ListGroupItem([
        dbc.Row([
            dbc.Col([
                html.H5(session_label, style={'vertical-align': 'middle', 'margin': 'auto'})
            ], style={'align-items': 'center', 'justify-content': 'center', 'display': 'flex'}),
            dbc.Col([
                html.H5(session.date, style={'vertical-align': 'middle', 'margin': 'auto'})
            ], style={'align-items': 'center', 'justify-content': 'center', 'display': 'flex'}),
            dbc.Col(button_group, width=5)
        ], align='between')

    ], color=color)


def EmptyListItem():
    return dbc.ListGroupItem(
        dbc.Row(
            dbc.Col(
                html.H5('No sessions have been found!', style={'vertical-align': 'middle', 'margin': 'auto'}),
                style={'align-items': 'center', 'justify-content': 'center', 'display': 'flex'})
        )
    )


def SessionList(username, list_type, selected_session_pkid=None):
    list_items = []
    all_sessions = sql_utils.list_sessions(username, list_type)

    for session in all_sessions:
        if selected_session_pkid is not None and session.pkid == int(selected_session_pkid):
            color = 'success'
        else:
            color = None
        list_items.append(SessionListItem(session, list_type, color))

    if not list_items:
        return dbc.ListGroup(EmptyListItem())

    return dbc.ListGroup(list_items)


def TutorialItem(idx, name):
    style = {'border-bottom': '1px solid', 'border-left': '1px solid', 'border-right': '1px solid'}
    if idx == 1:
        style['border-top'] = '1px solid'

    return dbc.ListGroupItem([
        dbc.Row([
            dbc.Col([
                html.H5('Tutorial {}: {}'.format(idx, name), style={'vertical-align': 'middle', 'margin-top': 8})
            ], style={'align-items': 'center', 'justify-content': 'left', 'display': 'flex'}, width=9),
            dbc.Col(dbc.Button('Read more', id={'type': 'tutorial-button', 'index': idx}, color='primary'),
                    style={'align-items': 'center', 'justify-content': 'right', 'display': 'flex'})
        ], justify='around', align='around')
    ], style=style)


def TutorialList():
    return dbc.Row(
        dbc.ListGroup([
            TutorialItem(idx=1, name='Creating your first plot'),
            TutorialItem(idx=2, name='Compare a contact prediction with a PDB file'),
            TutorialItem(idx=3, name='Storing, loading and sharing a session'),
        ], style={'width': '75%'}
        ), justify='center', align='center')


def UserAccountHelpList():
    return html.Ul([
        html.Li(['Create an user account. First step to get you started with ConPlot accounts '
                 'is to create one. To do this, simply provide your details in the ',
                 html.I('Create a new account'),
                 ' button. We will require you to provide an username that is not already used '
                 'by someone else in our system, a password and an email. Please note that we '
                 'will not share this email address with any third party and that it will only '
                 'be used to contact you if you request assistance to restore your password '
                 'in case you forget it.'],
                style={"font-size": "110%", 'text-align': "justify"}),
        html.Li(['Store sessions. Once you login into your account you will be able to store '
                 'sessions in your personal storage area. To do this, after you create a plot '
                 'of interest, scroll down to the bottom of the input panel -panel 2 in Figure '
                 '1-. Here you will see that you can name your current session and store it '
                 'into your personal storage.'],
                style={"font-size": "110%", 'text-align': "justify"}),
        html.Li(['Load stored sessions. You can access any session that you have stored in '
                 'your personal storage. To do this, access the users area on the dropdown '
                 'menu at the left of the navigation bar and click on ',
                 html.I('Access personal storage'),
                 '. Here you will see a list of all the sessions that you have stored, and '
                 'also those sessions that other users may have shared with you. Use the load '
                 'and delete buttons next to each session to load or delete any of these '
                 'sessions. Please note that you will not be able to delete sessions that were '
                 'shared with you, as only the owner of a session can do this. However, you '
                 'can decide to stop sharing the session by clicking on the stop button.'],
                style={"font-size": "110%", 'text-align': "justify"}),
        html.Li(['Share sessions. You can share any session that you save with other users '
                 'of ConPlot. To do this, access the users area on the dropdown menu at the '
                 'left of the navigation bar and click on ',
                 html.I('Share sessions'),
                 '. Here you will be presented with a list of the sessions that you have '
                 'created. To share a session in particular, fill in the box next to this '
                 'sessions with the user that you want to share it with, and click on the '
                 'share button. Once you do this, the other user will have access to this '
                 'session. Note that you will only be able to do this with sessions that '
                 'you have created yourself: you cannot share sessions that have been shared '
                 'with you previously.'], style={"font-size": "110%", 'text-align': "justify"})
    ])


def AdjustPlotHelpList():
    return html.Ul([
        html.Li(['Section 1: Adjust Contact Map. In this section it is possible to modify '
                 'aspects about how the residue contact information is displayed through a '
                 'series of dropdown menus:',
                 html.Ul([
                     html.Li(['L/N selector: Change the values of ', html.I('N'),
                              ' with this selector to choose how many contacts should be '
                              'included in the plot (L is the number of residues in the '
                              'protein sequence, residues are sorted by their probability '
                              'score). If you set ', html.I('N'),
                              ' to 0, then all contacts in the file will be displayed. Please '
                              'note that only numerical values between 0 and 10 are allowed.']),
                     html.Li('Size selector: Change the size of the contact markers in the '
                             'plot. ConPlot will set a default value depending on the size of '
                             'the protein you are working with, but you can still change this '
                             'if you would like to make the markers smaller or bigger. Please '
                             'note that only numerical values between 1 and 15 are allowed'),
                     html.Li(['Map A and Map B selectors: These two selectors let you choose '
                              'which contact data should be displayed on the plot. By '
                              'default, ', html.I('Map A'),
                              ' refers to the top half triangle of the map, and ',
                              html.I('Map B'), ' to the lower one. If the ',
                              html.I('Superimpose Maps'),
                              ' switch is activated, the the roles of these two dropdown '
                              'menus change: ', html.I('Map A'),
                              ' is now used to select the reference map, which will be '
                              'compared with the secondary map selected with the ',
                              html.I('Map B'), ' selector.']),
                     html.Li(['Superimpose Maps Switch: As explained above, if this switch '
                              'is activated ', html.I('Map A'),
                              ' will be used as a reference map to be compared with ',
                              html.I('Map B'),
                              '. In this mode, contacts will be coloured according to their '
                              'presence in the reference map and the secondary map. Contacts '
                              'that appear on both the reference and the secondary map will be '
                              'colored in black -match-, those that only appear in the '
                              'reference in grey -absent-, and those that only appear in the '
                              'secondary map in red -mismatch-. Please note that you can only '
                              'use this mode if you select two different contact map files in ',
                              html.I('Map A'), ' and ', html.I('Map B'), ' selectors.'])
                 ])],
                style={"font-size": "110%", 'text-align': "justify"}),
        html.Li(['Section 2: Adjust additional tracks. In this section you will find selectors '
                 'that will let you control aspects about how the additional tracks are being '
                 'displayed in the plot:',
                 html.Ul([
                     html.Li('Size selector: Change the size of the tiles used to create the '
                             'tracks on the diagonal of the plot. By increasing this vallue, '
                             'you will be able to create create the effect of a continuous '
                             'uninterrupted line if you wish to.Please note that only '
                             'numerical values between 1 and 20 are allowed'),
                     html.Li('Separation selector: Change the separation between the different '
                             'tracks displayed on the plot. This can result useful if due to '
                             'the default settings of ConPlot some tracks are layed on '
                             'top of others.'),
                     html.Li('Transparent Tracks Switch: When active, the tracks will have '
                             'some level of transparency, allowing you to see any contacts '
                             'present beneath them.')
                 ])],
                style={"font-size": "110%", 'text-align': "justify"}),
        html.Li(["Section 3: Active Tracks. In this section you can select which information "
                 "displayed on actively on each track of the diagonal. In ConPlot, the "
                 "diagonal axis of the contact maps has been divided into 9 tracks, which are "
                 "numbered according to their deviation from the reference diagonal track, "
                 "which is numbered as 0. Each of the selectors in this section controls the "
                 "information displayed on one of these tracks, and will let you choose the "
                 "name of one of the files that you have uploaded previously on the input "
                 "panel -panel 2 on Figure 1-. Once you select a file, the data contained in "
                 "it will be displayed in that particular track. If you leave the selection "
                 "blank, then no data will be shown."],
                style={"font-size": "110%", 'text-align': "justify"}),
        html.Li(['Section 4: Color Palettes. In this section you can alter the color palettes '
                 'used to depict the additional tracks displayed on the plot. ConPlot allows '
                 'you to set different color schemes for each dataset track so that you can '
                 'customise the way your plot looks.'],
                style={"font-size": "110%", 'text-align': "justify"}),
    ])


def AdditionalFormatsHelpList():
    return html.Ul([
        html.Li(['TOPCONS file. TOPCONS is a web based application aimed at the prediction of '
                 'the membrane topology of a given protein sequence. ConPlot parses files '
                 'produced by this server and extracts the information about the topology of '
                 'the protein, indicating the membrane spanning regions and their relative '
                 'orientation. TOPCONS is available ',
                 html.A(html.U('here'), href=UrlIndex.TOPCONS_WEB.value),
                 ', and you may read more about it in the original paper published by its '
                 'authors ',
                 html.A(html.U('here'), href=UrlIndex.TOPCONS_CITATION.value),
                 '.'],
                style={"font-size": "110%", 'text-align': "justify"}),
        html.Li(['PSIPRED file. PSIPRED is a web based application focused at the prediction '
                 'of the secondary structure of a protein sequence. Once uploaded to ConPlot, '
                 'output files obtained with this service are processed to extract the '
                 'predicted presence of secondary structure elements along the protein '
                 'sequence. It is possible to use PSIPRED in order to obtain such predictions ',
                 html.A(html.U('here'), href=UrlIndex.PSIPRED_WEB.value),
                 ', and you can read more about this tool as it is described by its authors on '
                 'the original paper ',
                 html.A(html.U('here'), href=UrlIndex.PSIPRED_CITATION.value),
                 '.'],
                style={"font-size": "110%", 'text-align': "justify"}),
        html.Li(['IUPRED file. IUPred2A is a web server that allows users to generate energy '
                 'estimation based predictions for ordered and disordered residues in a '
                 'sequence. ConPlot parses these output files and extracts the estimate of the '
                 'order / disorder of the residues in the protein of interest. IUPred2A is '
                 'available ',
                 html.A(html.U('here'), href=UrlIndex.IUPRED_WEB.value),
                 '. If you wish to know more about this tool, you may want to read the '
                 'original paper published by its authors ',
                 html.A(html.U('here'), href=UrlIndex.IUPRED_CITATION.value),
                 '.'],
                style={"font-size": "110%", 'text-align': "justify"}),
        html.Li(['CONSURF file. Based on the phylogenetic relations between homologous '
                 'sequences, the Consurf server estimates the evolutionary conservation of '
                 'amino acid positions in a protein sequence. ConPlot will parse the output '
                 'files produced by these server and allow users to add a track indicating the '
                 'level of conservation of each residue in the sequence. Consurf server is '
                 'available ',
                 html.A(html.U('here'), href=UrlIndex.CONSURF_WEB.value),
                 ', and you can read more about it in the original publication ',
                 html.A(html.U('here'), href=UrlIndex.CONSURF_CITATION.value),
                 '.'],
                style={"font-size": "110%", 'text-align': "justify"}),
        html.Li(['CUSTOM file. These files are plain text files that can be created manually '
                 'by users to include additional tracks of information to the plot. These '
                 'files enable limitless personalisation of the contact map plot, as it '
                 'becomes possible to add as much information as desired. If you wish to read '
                 'about the format specifications click ',
                 dbc.Button('here', color='link', size='sm', id='custom-format-specs-button',
                            className='ml-0'),
                 ],
                style={"font-size": "110%", 'text-align': "justify"})
    ])


def PanelLayoutHelpList():
    return html.Ul([
        html.Li(['Panel 1: This panel contains the navigation bar that is displayed throughout '
                 'all ConPlot. The tabs on this bar should be your preferred method to browse '
                 'through ConPlot, as using the arrow keys or the refresh button on your '
                 'browser will cause you to loose your session and loose any unsaved data. '
                 'Also, you may notice that after you create a plot and browse away to a '
                 'different tab, plots will disappear when you come back to the ',
                 html.I('Plot'),
                 ' tab. Nevertheless, ConPlot kept everything for you so if you want to '
                 'see your plot again simply click on ',
                 html.I('Generate Plot'),
                 ' to get it back!'],
                style={"font-size": "110%", 'text-align': "justify"}),
        html.Li(['Panel 2: This is the input panel, here you can upload all the data you want '
                 'to integrate into a plot. The panel is divided into three sections (from top '
                 'to bottom): first, the ',
                 html.I('Required Input'),
                 ' section, where you upload a sequence and a contact map -which is the '
                 'minimal input to create a plot-; second an ',
                 html.I('Additional Tracks'),
                 ' section, where you upload prediction files containing the information to '
                 'be display as coloured tracks in the diagonal of the map; and finally a ',
                 html.I('Store Session'),
                 ' section, where you will be able to store sessions -only after you login '
                 'into your user account-.'],
                style={"font-size": "110%", 'text-align': "justify"}),
        html.Li(["Panel 3: This is the plot panel, and is the panel where the plots that you "
                 "create will be displayed. A grey placeholder with ConPlot's logo will be "
                 "displayed until you generate a plot. Plots are interactive, if you hover "
                 "over the contacts on the map or the tracks on the diagonal ConPlot will show "
                 "information  about that particular data point. If you over on the top left "
                 "of the plot, a mode bar will appear. With the buttons in this bar you can "
                 "control certain aspects of the plot, like the behaviour of the hovering "
                 "tool, the scale of the plot, or you can also download the plot you have "
                 "created as a ",
                 html.I('png'),
                 ' image file -click on the camera button-.'],
                style={"font-size": "110%", 'text-align': "justify"}),
        html.Li(['Panel 4: This is the display control panel, where you will be able to '
                 'control the layout of the plot and the way information is displayed: the '
                 'size of the contact markers, the track colour palettes, the information '
                 'displayed on each track...etc. Once you have tweaked these settings, click '
                 'on ',
                 html.I('Adjust Plot'),
                 ' to refresh the plot with the adjusted parameters.'],
                style={"font-size": "110%", 'text-align': "justify"}),
    ])


def MandatoryInputHelpList():
    return html.Ul([
        html.Li('FASTA file. This file should contain only one sequence, the one corresponding '
                'with the structure of interest. If there are multiple sequences, ConPlot will '
                'only consider the first sequence present in the file. Please note that unlike '
                'other types of input, only one sequence can be uploaded in each session at '
                'any given time. If you want to upload a new sequence, that means you will '
                'need to delete the one you uploaded already first.',
                style={"font-size": "110%", 'text-align': "justify"}),
        html.Li(['Contact map file. This file informs about which residue pairs are in close '
                 'contact in the three-dimensional structure of the protein of interest. There '
                 'are many formats used for such files, of which ConPlot is able to parse the '
                 'most common ones. Nevertheless, it might occur you wish to upload a contact '
                 'map file in a format not supported by ConPlot, in which case we  suggest you '
                 'take a look at ',
                 html.A(html.U('Conkit'), href=UrlIndex.CONKIT_READDOCS.value),
                 ', a python library able to read and convert most contact formats. This tool '
                 'will enable you to convert the file of interest into a format ConPlot is '
                 'able to read.'],
                style={"font-size": "110%", 'text-align': "justify"})
    ])


def GdprRightsList():
    return html.Ul([
        html.Li('The right of transparency and modalities. The privacy policy should be clear and '
                'easy to follow in explaining what data we collect and how we use it.'),
        html.Li('The right to be informed about when data is gathered. This is described in this privacy '
                'policy.'),
        html.Li('The right of access. You can ask for what specific data we have about you and how we '
                'use it.'),
        html.Li('The right to rectification. We will correct any errors in your personal data that you '
                'point out to us.'),
        html.Li('The right to be forgotten. We are happy to delete your account and info when you make '
                'such a request.'),
        html.Li('The right to restrict processing. You have the right to request that we restrict the use '
                'of your data.'),
        html.Li('The right for notification obligation regarding rectification/erasure/restriction.'),
        html.Li('The right to data portability.'),
        html.Li('The right to object to the processing of your personal data at any time.'),
        html.Li('The right in relation to automated decision making and profiling. Basically, you have '
                'the right not to be subject to decisions based solely on automated processing which '
                'significantly affect you.')
    ])


def AutomaticInfoCollectedList():
    return html.Ul([
        html.Li('The IP address of the client making the request. Often the IP address is that of '
                'your personal computer or smart phone; however, it might be that of a firewall or '
                'proxy your internet provider manages.'),
        html.Li('The operating system and information about the browser used when visiting the '
                'site.'),
        html.Li('The date and time of each visit.'),
        html.Li('Pages visited.'),
        html.Li('The address of a referring page. If you click a link on a website that directs '
                'you to ConPlot, the address of that originating web page will be collected. '
                'This “referrer” information is transmitted as part of the browser and server '
                'communications; it is not based on any marketing or partnering agreements with '
                'the referring site.'),
    ])


def CustomFormatFieldsHelpList():
    return html.Ul([
        html.Li('Field 1: corresponds with the first residue number of the record  -inclusive, i.e. '
                'indicates where the record should start-.', style={"text-align": "justify"}),
        html.Li('Field 2: corresponds with the last residue number of the record -inclusive, i.e. '
                'indicates where the record should end-.', style={"text-align": "justify"}),
        html.Li('Field 3: indicates the color that should be used to depict this record. This is indicated '
                'with a number between 1 and 11, that in turn is used by ConPlot to assign a color to this '
                'record. A complete list of the mapping between these numbers and the actual color that '
                'will be used in the plot can be found in the next section "Adjust the plot layout".',
                style={"text-align": "justify"})
    ])
