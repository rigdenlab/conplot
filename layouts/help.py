import components
import dash_html_components as html
import dash_bootstrap_components as dbc
from utils import UrlIndex


def Body(cache):
    return html.Div(
        [
            html.Br(),
            html.Br(),
            html.Br(),
            components.PaletteModal('density', 1),
            components.PaletteModal('conservation', 2),
            components.PaletteModal('custom', 3),
            components.PaletteModal('disorder', 4),
            components.PaletteModal('membranetopology', 5),
            components.PaletteModal('msa', 6),
            components.PaletteModal('secondarystructure', 7),
            components.PaletteModal('hydrophobicity', 8),
            components.PaletteModal('heatmap', 9),
            components.GdprPolicyModal(),
            components.TutorialOneModal(),
            components.TutorialTwoModal(),
            components.TutorialThreeModal(),
            components.TutorialFourModal(),
            # components.TutorialFiveModal(),
            components.CustomFormatDescriptionModal(),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H2('ConPlot help page', className="card-text", style={'text-align': "center"}),
                            html.Br(),
                            html.Br(),
                            html.P(['Welcome to the ConPlot help page: here you can read how to use ConPlot and take '
                                    'full advantage of all its features. This page is divided in a series of sections '
                                    'that will guide you through the process of understanding what data files you need '
                                    'to create a plot, how to adjust the layout of a plot and even store these plots '
                                    'in your user storage area. If you came here looking for an example of the data '
                                    'files used as an input, you can download them ',
                                    html.A(html.U('here'), href=UrlIndex.EXAMPLE_DATA.value),
                                    '.'], style={"font-size": "110%", "text-align": "justify"}),
                            html.Br(),
                            html.H4('1. ConPlot layout', className="card-text", style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            html.P(["To create a plot, you will need to understand first the layout of ConPlot's ",
                                    html.I('Plot'),
                                    ' page. The layout of the application has been divided into four panels that will '
                                    'allow you to interact with ConPlot:'],
                                   style={"font-size": "110%", 'text-align': "justify"}),
                            components.PanelLayoutHelpList(),
                            html.Br(),
                            html.Img(src=UrlIndex.HELP_FIG1.value, height='700vh',
                                     style={'border': '5px solid', 'display': 'block', 'margin-left': 'auto',
                                            'margin-right': 'auto'}),
                            html.Br(),
                            html.Br(),
                            dbc.Alert([
                                'TIPS:',
                                html.Ul([
                                    html.Br(),
                                    html.Li(["Note the difference between the ",
                                             html.I('Generate Plot'), ' and the ', html.I('Adjust Plot'),
                                             " buttons. Use the former to create plots for the first time or after you "
                                             "upload new data files into the current session, and the latter to adjust "
                                             "the way the plot looks after tweaking the settings on the display "
                                             "control panel."]),
                                    html.Li("If you hover to the top right of the plot panel, the plot's mode bar will "
                                            "appear. Use the buttons on this bar to control the behaviour of the "
                                            "hovering tool, zoom in and out, change the scale of the plot or to "
                                            "download the plot image as a png file.")
                                ])
                            ], style={'text-align': "justify"}, color='info'),
                            dbc.Alert("WARNING: Do not click on the refresh button in your browser! Depending on your "
                                      "browser, doing this may cause your session to expire and you will lose any "
                                      "unsaved data and plots. Instead, use ConPlot's navigation bar on the top panel "
                                      "to safely browse through the website.",
                                      style={'text-align': "justify"}, color='danger'),
                            html.Br(),
                            html.H4('2. Required input', className="card-text", style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            html.P("ConPlot requires the following inputs to be able to create a plot.",
                                   style={"font-size": "110%", 'text-align': "justify"}),
                            components.MandatoryInputHelpList(),
                            html.P(['After you upload at least one file for each of these datasets you will be able to '
                                    'generate a plain contact map plot by clicking on the ',
                                    html.I('Generate Plot'),
                                    ' button. Note that it is possible to upload as many contact map files as you '
                                    'wish, as it is possible to compare them or dynamically change which contact file '
                                    'is loaded in the plot. More on how to do this will be explained later on.'
                                    ], style={"font-size": "110%", 'text-align': "justify"}),
                            dbc.Alert([
                                'TIPS:',
                                html.Ul([
                                    html.Li('If you wish to remove a file that you have uploaded, simply close the '
                                            'banner with its name and ConPlot will do the rest.'),
                                    html.Li(['You can repeat the process of uploading a residue contact prediction '
                                             'file using the ', html.I('Upload Contact'),
                                             ' as many times as you wish in order to upload multiple contact maps.'])
                                ])
                            ],
                                style={'text-align': "justify"},
                                color='info'),
                            dbc.Alert('WARNING: It is important that the numbering used in all the uploaded contact '
                                      'map files matches the sequence of residues present in the '
                                      'provided FASTA file. If this numbering does not match, this could result in '
                                      'misrepresentations of data or even failure to create a plot.',
                                      style={'text-align': "justify"}, color='danger'),
                            html.Br(),
                            html.H4('3. Additional tracks', className="card-text",
                                    style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            html.P("It is possible to add coloured tracks on the diagonal of the contact maps by "
                                   "uploading  a series of prediction files associated to the sequence of "
                                   "interest. ConPlot is able to parse automatically the information contained in the "
                                   "following formats:"
                                   , style={"font-size": "110%", "text-align": "justify"}),
                            components.AdditionalFormatsHelpList(),
                            dbc.Alert([
                                'TIPS:',
                                html.Ul([
                                    html.Br(),
                                    html.Li('You will not be able to upload a file until you first select its format '
                                            'in the dropdown selection menu.'),
                                    html.Li(['You can only upload one file at a time when you use the ',
                                             html.I('Add track'),
                                             ' button, but you can do this as many times as you wish in order to add '
                                             'multiple tracks to the plot.']),
                                    html.Li(['If you would like to upload a sequence prediction that is not '
                                             'included in the list of supported formats, you can always create a '
                                             'custom file and add the information manually. If you think it would be '
                                             'very useful to be able to read this format automatically with ConPlot, '
                                             'you can try to ',
                                             dbc.CardLink(html.U('get in touch'), href=UrlIndex.CONTACT.value),
                                             ' and let us know.'])
                                ])
                            ], style={'text-align': "justify"}, color='info'),
                            html.P(['There is no limit on the number of files you can upload, the only requirement is '
                                    'that all the files correspond with the residue sequence that has been uploaded. '
                                    'If these files do not match, this could result in data misrepresentation or '
                                    'Conplot not being able to create a plot. Please note that if you upload multiple '
                                    'files for a given format, the default behaviour of ConPlot is to include only the '
                                    'first one to the plot. If you wish to visualise the other files, you will need to '
                                    'select them in the track content selection menus as described in the next '
                                    'section.'],
                                   style={"font-size": "110%", "text-align": "justify"}),
                            html.Br(),
                            html.H4('4. Adjust the plot layout', className="card-text",
                                    style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            html.P(['Once you have uploaded all the files of interest you can create your first plot '
                                    'by clicking on ',
                                    html.I('Generate Plot'),
                                    '. Then, ConPlot will create a plot with the default layout settings. We tried to '
                                    'make sure that by default ConPlot will generate plots where the provided data is '
                                    'shown clearly, but this is a difficult task as it is something that is highly '
                                    'dependent on your data. Thus, you are likely to need to adjust the settings on '
                                    'the display control panel to get your data shown in the best possible way. To '
                                    'help you do this, this panel has been divided into 4 sections:'],
                                   style={"font-size": "110%", "text-align": "justify"}),
                            components.AdjustPlotHelpList(),
                            html.Br(),
                            dbc.Alert(['TIPS: ',
                                       html.Ul([
                                           html.Br(),
                                           html.Li(['If you have just created a plot with the ',
                                                    html.I('Generate Plot'),
                                                    ' button and you can see individual squared tiles in the diagonal '
                                                    'tracks, try increasing the default value of the additional track '
                                                    'marker size.']),
                                           html.Li(['If you have just uploaded a file, it may be that this file is '
                                                    'not listed on the track selection layout. You may need to '
                                                    'click on the ', html.I('Generate Plot'),
                                                    ' button before being able to choose it in the dropdown menu.']),
                                           html.Li(['You may notice that when you zoom into a contact map, the contact '
                                                    'markers retain their size. There are two ways you can get around '
                                                    'this, we recommend using the ', html.I('Create heatmap'),
                                                    ' to create a heatmap where contact markers increase in size when '
                                                    'you zoom in. Alternatively, you can also change the contact '
                                                    'marker size with the ', html.I("Size selector"),
                                                    ' and click on ', html.I("Adjust Plot"),
                                                    ' and then zoom-in. This can be done repeatedly until the desired '
                                                    'size is chosen.']),
                                           html.Li(['Sometimes it is difficult to map a specific contact with its '
                                                    'annotations at the diagonal. Try turning on the ',
                                                    html.I('Verbose labels'), ' switch.']),
                                           html.Li(['If you have just created a plot with the ',
                                                    html.I('Generate Plot'),
                                                    ' button and the diagonal tracks overlap with each other, try '
                                                    'increasing the default value of the additional track separation.'])
                                       ])],
                                      style={'text-align': "justify"}, color='info'),
                            html.Br(),
                            html.H4('5. Colour Palettes', className="card-text", style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            html.P('Here is a list of the different palettes available for each dataset that you '
                                   'can use in ConPlot'),
                            components.PaletteList(),
                            html.Br(),
                            html.Br(),
                            html.H4('6. User Accounts', className="card-text", style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            html.P(['By creating a user account in ConPlot, you will be able to access a series of '
                                    'additional features that will enable you to store sessions indefinitely and share '
                                    'them with other users. You can access the user account menu with the ',
                                    html.I('LOGIN'),
                                    ' dropdown menu on the top right of the navigation bar -panel 1 in Figure 1.'],
                                   style={"font-size": "110%", "text-align": "justify"}),
                            components.UserAccountHelpList(),
                            html.Br(),
                            dbc.Alert('TIP: Interactive sessions expire after 60 minutes of inactivity. If you '
                                      'wish to permanently save the data and plots, create a user account and store '
                                      'the session before it expires.',
                                      style={'text-align': "justify"}, color='info'),
                            html.Br(),
                            html.H4('7. Tutorials', className="card-text", style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            html.P(["Here is a list of tutorials that will help you understand better how to use "
                                    "ConPlot. We strongly encourage you to complete them before using ConPlot for the "
                                    "first time, as they will guide you through the basic ConPlot features. We also "
                                    "recommend completion of these tutorials in the specified order as each of them "
                                    "will require you to understand concepts learned in the preceding one. To follow "
                                    "them, you will need to download the example data ",
                                    html.A(html.U('here'), href=UrlIndex.EXAMPLE_DATA.value)],
                                   style={"font-size": "110%", "text-align": "justify"}),
                            html.Br(),
                            components.TutorialList(),
                            html.Br(),
                            html.Br(),
                            html.H4('8. Using ConPlot locally', className="card-text", style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            html.P(['ConPlot is a web-based application, and as such we recommend you make use of it '
                                    'through this website. However, it is also possible to use ConPlot locally on your '
                                    'personal machine using the localhost. There are two possible ways to achieve '
                                    'this.', html.Br(), html.Br(),
                                    html.H5('8.1 Using Docker image at DockerHub'),
                                    "ConPlot is distributed as a docker image on the project's ",
                                    html.A(html.U('Docker hub repository'), href=UrlIndex.DOCKER_HUB.value),
                                    '. To use it, you will need to link it with a Redis container:']),
                            dbc.Col([
                                html.Plaintext('$   docker pull filosanrod/conplot:latest\n$   docker run --name '
                                               'redis_db -d redis:latest \n$   docker run --name conplot_app'
                                               '\n    -d filosanrod/conplot:latest gunicorn app:server -p 80:80 -b :80 \ '
                                               '\n    --link redis_db:redis -e KEYDB_URL="redis://redis_db:6379" \ \n'
                                               '    --preload --workers=6 --timeout 120 --graceful-timeout 120 \ \n'
                                               '    --max-requests 5 --log-level=info')
                            ], style={'background-color': '#EAEAEA'}, align='center'),
                            html.P(['After you set up running the docker container, you will be able to access the '
                                    'app on http://0.0.0.0:80/home.',
                                    html.Br(), html.Br(), html.H5('8.2 Locally using Flask development server'),
                                    'It is also possible to use Flask development server to run ConPlot on your '
                                    'localhost. To do this you will first need to install redis, which is the cache '
                                    'memory server used by ConPlot.']),
                            dbc.Col([
                                html.Plaintext('$   sudo apt update\n$   sudo apt install redis-server\n$   sudo '
                                               'service redis start')
                            ], style={'background-color': '#EAEAEA'}, align='center'),
                            html.P('Once you have installed `redis`, you will need to start the service by running:'),
                            dbc.Col([
                                html.Plaintext('$   sudo service redis start')
                            ], style={'background-color': '#EAEAEA'}, align='center'),
                            html.P('Now you will need to clone the repository, install the requirements and '
                                   'setup environment variables. Please note that ConPlot requires at least '
                                   'python 3.6.'),
                            dbc.Col([
                                html.Plaintext('$   git clone https://github.com/rigdenlab/conplot\n'
                                               '$   cd conplot\n$   python3.6 -m pip install -r requirements\n$   '
                                               'echo "KEYDB_URL=0://localhost:6379" > .env\n$   echo "KEYDB_TIME'
                                               'OUT=3600" >> .env')
                            ], style={'background-color': '#EAEAEA'}, align='center'),
                            html.P('With the last two commands you will also have created an .env file with a '
                                   'variable named KEYDB_URL pointing to the redis server and a KEYDB_TIMEOUT '
                                   'variable with the session timeout value. This is the time at which a session '
                                   'expires after inactivity. By default in www.conplot.org this has a value of 3600 '
                                   'minutes, but if running locally you can set this time to any other value. '
                                   'The only thing left to do is to start the Flask development server on your '
                                   'machine:'),
                            dbc.Col([
                                html.Plaintext('$   python3.6 app.py')
                            ], style={'background-color': '#EAEAEA'}, align='center'),
                            html.P(['Now you will be able to access the app on ',
                                    html.A(html.U('http://127.0.0.1:8050/home'),
                                           href='http://127.0.0.1:8050/home'),
                                    '. Please note that when running locally, ConPlot will not be able to establish a '
                                    'connection with our database, so all the user account related features will be '
                                    'disabled. Similarly, you will not be able to get in touch with us using the '
                                    '"Get in touch" tab.']),
                            html.Br(),
                            html.H4('9. Server status', className="card-text", style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            components.ServerStatusList(cache),
                            html.Br(),
                            html.Br(),
                            html.H4('10. Privacy Policy', className="card-text", style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            components.GdprPolicyAlert(False)
                        ])
                    ])
                ], width=10),
            ], align='center', justify='center', className='m-0')
        ]
    )


def Help(session_id, username, cache):
    return html.Div([
        components.Header(username),
        components.NavBar(UrlIndex.HELP.value),
        Body(cache),
        components.Footer()
    ])
