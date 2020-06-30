from utils import UrlIndex
import dash_html_components as html
from components import NavBar, Header
import dash_bootstrap_components as dbc


def Body():
    return html.Div(
        [
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H2('ConPlot help page', className="card-text", style={'text-align': "center"}),
                            html.Br(),
                            html.Br(),
                            html.P([
                                'Welcome to ConPlot help page, here you can read how to use ConPlot and take full '
                                'advantage of all its features. This page is divided in a series of sections that will '
                                'guide you through the process of understanding what data files you need to create a '
                                'plot, how to adjust the layout of a plot and even store these plots on your user '
                                'storage area. If you came here looking for an example of the data files used as an '
                                'input, you can download them right ',
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
                            html.P([
                                'After you upload at least one file for each of these datasets you will be able to '
                                'generate a plain contact map plot by clicking on the ',
                                html.I('Generate Plot'),
                                ' button. Note that it is possible to upload as many contact map files as you wish, as '
                                'it is possible to compare them or dynamically change which contact file is loaded in '
                                'the plot. More on how to do this will be explain later on.'
                            ], style={"font-size": "110%", 'text-align': "justify"}),
                            dbc.Alert(
                                'TIP: If you wish to remove a file that you have uploaded, simply close the banner '
                                'with its name and ConPlot will do the rest.', style={'text-align': "justify"},
                                color='info'),
                            dbc.Alert('WARNING: it is important that the numbering used in all the uploaded contact '
                                      'map files matches the one used in the sequence of residues present in the provided '
                                      'FASTA file. If this numbering does not match, this could result in '
                                      'misrepresentations of data or even failure to create a plot.',
                                      style={'text-align': "justify"}, color='danger'),
                            html.Br(),
                            html.H4('2. Aditional tracks', className="card-text",
                                    style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            html.P("ConPlot will process the information contained in a series of sequence predictions "
                                   , style={"font-size": "110%", "text-align": "justify"}),
                            dbc.Alert('TIP: You will not be able to upload a file until you first select its format in '
                                      'the dropdown selection menu.', style={'text-align': "justify"}, color='info'),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.H4('3. Create a plot and adjust the plot', className="card-text",
                                    style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            html.P([
                                """Here we explain how to create user accounts, and how to store and share sessions"""
                            ], style={"font-size": "110%", "text-align": "justify"}),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.H4('4. Tutorials', className="card-text",
                                    style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            html.P([
                                """Here is a list of tutorials that will help you understand better how to use 
                                ConPlot."""
                            ], style={"font-size": "110%", "text-align": "justify"}),
                            dbc.Alert([
                                'TIP: If you want to follow these tutorials you will need to download the '
                                'example data that can be found ',
                                html.A(html.U('here'), href=UrlIndex.STATIC_DATA.value),
                                '.'
                            ], style={'text-align': "justify"}, color='info'),
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
