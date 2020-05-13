from utils import PathIndex
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
                        dcc.Markdown(
                            'ConPlot is a web-based application for the visualisation of information derived from '
                            'residue contact predictions in combination with other sources of information, such as'
                            ' secondary structure predictions, transmembrane helical topology, sequence conservation'
                            '...etc. Developed by the [Rigden]({}) group at the [University of Liverpool]'
                            '(https://www.liverpool.ac.uk/), this new tool provides an interactive interface for '
                            'researchers in the field of protein bioinformatics that are interested in analysing data'
                            ' on a given protein at a glance.'
                            ''.format(PathIndex.RIGDEN.value)),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.H4('How does it work', className="card-text", style={'text-align': "center"}),
                        html.Hr(),
                        html.Br()
                    ])
                ])
            ]),
        ]
    )


def Home(session_id):
    return html.Div([
        Header(),
        NavBar(PathIndex.HOME.value),
        Body(session_id),
    ])
