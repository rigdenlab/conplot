from utils import UrlIndex
import dash_html_components as html
from components import NavBar, Header
import dash_core_components as dcc
import dash_bootstrap_components as dbc


def Body(session_id):
    return html.Div(
        [
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Container([
                dbc.Card([
                    dbc.CardBody([
                        html.H1('Welcome to Conplot', className="card-text", style={'text-align': "center"}),
                        html.Br(),
                        html.Br(),
                        html.H4('About ConPlot', className="card-text", style={'text-align': "center"}),
                        html.Hr(),
                        html.Br(),
                        html.P([
                            """ConPlot is a web-based application for the visualisation of information derived from 
                            residue contact predictions in combination with other sources of information, such as 
                            secondary structure predictions, transmembrane helical topology, sequence conservation. 
                            The plot allows the visual cross-referencing of sequence-based prediction data from multiple 
                            sources. The exploitation of this novel cross-referencing method can be useful to 
                            potentially expose structural features that would otherwise go undetected. Developed by 
                            the """,
                            html.A("Rigden", href=UrlIndex.RIGDEN_GITHUB.value),
                            """ group at the """,
                            html.A("University of Liverpool", href=UrlIndex.UNIVERSITY_LIVERPOOL.value),
                            """ this new tool provides an interactive interface for researchers in the field of protein
                             bioinformatics that are interested in analysing data on a given protein at a glance."""
                        ], style={"font-size": "150%", "text-align": "justify"}),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.H4('How does it work', className="card-text", style={'text-align': "center"}),
                        html.Hr(),
                        html.Br(),
                        dcc.Markdown("""Here we explain about the different types of formats you can upload with links 
                        to help page"""),
                        html.Br()
                    ])
                ])
            ]),
        ]
    )


def Home(session_id):
    return html.Div([
        Header(),
        NavBar(UrlIndex.HOME.value),
        Body(session_id),
    ])
