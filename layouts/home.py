from components import GdprPolicyModal, GdprPolicyAlert
from utils import UrlIndex
import dash_html_components as html
from components import NavBar, Header
import dash_bootstrap_components as dbc


def Body():
    return html.Div(
        [
            GdprPolicyModal(),
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader(
                            GdprPolicyAlert()
                        ),
                        dbc.CardBody([
                            html.H2('Welcome to Conplot', className="card-text", style={'text-align': "center"}),
                            html.Br(),
                            html.Br(),
                            html.H4('About ConPlot', className="card-text", style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            html.P([
                                """ConPlot is a web-based application for the visualisation of information derived from 
                                residue contact predictions in combination with other sources of information, such as 
                                secondary structure predictions, transmembrane helical topology, sequence conservation. 
                                The plot allows the visual cross-referencing of sequence-based prediction data from 
                                multiple sources. The exploitation of this novel cross-referencing method can be useful 
                                to potentially expose structural features that would otherwise go undetected. Developed 
                                by the """,
                                dbc.CardLink(html.U("Rigden Lab"), href=UrlIndex.RIGDEN.value),
                                """ group at the """,
                                html.A(html.U("University of Liverpool"), href=UrlIndex.UNIVERSITY_LIVERPOOL.value),
                                """ this new tool provides an interactive interface for researchers in the field of 
                                protein bioinformatics that are interested in analysing data on a given protein at a 
                                glance."""
                            ], style={"font-size": "120%", "text-align": "justify"}),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.H4('How does it work', className="card-text", style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            html.P([
                                """A protein contact map is a two-dimensional representation of the (predicted) 
                                contacting pairs of residues in the three-dimensional structure. Common depictions of 
                                these maps tend to  omit those contacts near the diagonal of the plot, as they 
                                correspond to pairs of sequentially nearby residues and typically do not add any 
                                valuable information to the plot. ConPlot takes advantage of this, and allows users 
                                to use this space otherwise left empty to integrate different sources of information 
                                into a contact map  as coloured tracks in the diagonal. Additionally, ConPlot is 
                                packed with features that allow the user to fully customise their plots:                           
                                """
                            ], style={"font-size": "120%", "text-align": "justify"}),
                            html.Ul([
                                html.Li(
                                    'Upload multiple contact maps to compare them, either by plotting each of them in '
                                    'a half of the map or by superimposing one of top of the other.'),
                                html.Li(
                                    'Full control over plot features such as contact marker size, track size or track '
                                    'arrangement.'),
                                html.Li('Multiple custom tracks can be added to the plot, enabling limitless '
                                        'personalisation of the information displayed on the plot.'),
                                html.Li(
                                    'User accounts are available in order to store sessions and re-visit them without '
                                    'having to upload the data again. It is also possible to share these sessions with '
                                    'other users.'),
                            ], style={"font-size": "120%", "text-align": "justify"}),
                            html.P([
                                'Visit our ',
                                dbc.CardLink(html.U('help page'), href=UrlIndex.HELP.value),
                                ' to read about how to use ConPlot and take advantage of its full potential!'
                            ], style={"font-size": "120%", "text-align": "justify"}),
                        ]),
                    ]),
                ], width=10)
            ], justify='center', align='center', className='m-0'),

        ]
    )


def Home(session_id, username):
    return html.Div([
        Header(username),
        NavBar(UrlIndex.HOME.value),
        Body(),
    ])
