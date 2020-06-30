from utils import UrlIndex
import dash_html_components as html
from components import NavBar, Header, CustomFormatDescriptionModal
import dash_bootstrap_components as dbc


def Body():
    return html.Div(
        [
            html.Br(),
            html.Br(),
            html.Br(),
            CustomFormatDescriptionModal(),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H2('ConPlot help page', className="card-text", style={'text-align': "center"}),
                            html.Br(),
                            html.Br(),
                            html.P(['Welcome to ConPlot help page, here you can read how to use ConPlot and take full '
                                    'advantage of all its features. This page is divided in a series of sections that '
                                    'will guide you through the process of understanding what data files you need to '
                                    'create a plot, how to adjust the layout of a plot and even store these plots on '
                                    'your user storage area. If you came here looking for an example of the data files '
                                    'used as an input, you can download them right ',
                                    html.A(html.U('here'), href=UrlIndex.STATIC_DATA.value),
                                    '.'
                                    ], style={"font-size": "110%", "text-align": "justify"}),
                            html.Br(),
                            html.H4('1. Required input', className="card-text", style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            html.P("ConPlot requires the following inputs to be able to create a plot.",
                                   style={"font-size": "110%", 'text-align': "justify"}),
                            html.Ul([
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
                            ]),
                            html.P(['After you upload at least one file for each of these datasets you will be able to '
                                    'generate a plain contact map plot by clicking on the ',
                                    html.I('Generate Plot'),
                                    ' button. Note that it is possible to upload as many contact map files as you '
                                    'wish, as it is possible to compare them or dynamically change which contact file '
                                    'is loaded in the plot. More on how to do this will be explain later on.'
                                    ], style={"font-size": "110%", 'text-align': "justify"}),
                            dbc.Alert('TIP: If you wish to remove a file that you have uploaded, simply close the '
                                      'banner with its name and ConPlot will do the rest.',
                                      style={'text-align': "justify"},
                                      color='info'),
                            dbc.Alert('WARNING: It is important that the numbering used in all the uploaded contact '
                                      'map files matches the one used in the sequence of residues present in the '
                                      'provided FASTA file. If this numbering does not match, this could result in '
                                      'misrepresentations of data or even failure to create a plot.',
                                      style={'text-align': "justify"}, color='danger'),
                            html.Br(),
                            html.H4('2. Aditional tracks', className="card-text",
                                    style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            html.P("It is possible to add coloured tracks on the diagonal of the contact maps by "
                                   "uploading  a series of prediction files associated to the sequence of "
                                   "interest. ConPlot is able to parse automatically the information contained in the "
                                   "following formats:"
                                   , style={"font-size": "110%", "text-align": "justify"}),
                            html.Ul([
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
                                         'becomes possible to add as much information as wished. If you wish to read '
                                         'about the format specifications click ',
                                         dbc.Button('here', color='link', size='sm', id='custom-format-specs-button',
                                                    className='ml-0'),
                                         ],
                                        style={"font-size": "110%", 'text-align': "justify"})
                            ]),
                            dbc.Alert('TIP: You will not be able to upload a file until you first select its format in '
                                      'the dropdown selection menu.', style={'text-align': "justify"}, color='info'),
                            html.P(['There is no limit on the number of files you can upload for each dataset, the '
                                    'only requirement is that all the files correspond with the residue sequence that '
                                    'has been uploaded. If these files do not mach, it could be possible that the data '
                                    'on the resulting plot is misrepresented, or ConPlot is unable to create a plot on '
                                    'the first place. Please note that if you upload multiple files for a given '
                                    'format, the default behaviour of ConPlot is to include only the first one to the '
                                    'plot. If you wish to visualise the other files, you will need to select them in '
                                    'the track content selection menus as described in the next section.'],
                                   style={"font-size": "110%", "text-align": "justify"}),
                            dbc.Alert(['TIP: If you would like to upload a sequence prediction that is not included in '
                                       'the list of supported formats, you can always create a custom file and add the '
                                       'information manually. If you think it would be very useful to be able to read '
                                       'this format automatically with ConPlot, you can try to ',
                                       dbc.CardLink(html.U('get in touch'), href=UrlIndex.CONTACT.value),
                                       ' and let us know.'], style={'text-align': "justify"}, color='info'),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.H4('3. Create a plot and adjust the plot', className="card-text",
                                    style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.H4('4. FAQs', className="card-text",
                                    style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.H4('5. Tutorials', className="card-text",
                                    style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                        ])
                    ])
                ], width=10),
            ], align='center', justify='center', className='m-0')
        ]
    )


def Help(session_id, username):
    return html.Div([
        Header(username),
        NavBar(UrlIndex.HELP.value),
        Body(),
    ])
