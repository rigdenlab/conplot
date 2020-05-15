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
                        html.H1('Rigden Lab', className="card-text", style={'text-align': "center"}),
                        html.Br(),
                        html.H6('About us', className="card-text", style={'text-align': "center"}),
                        html.Hr(),
                        html.Br(),
                        html.P([
                            """We are a structural bioinformatics group based at the """,
                            html.A('University of Liverpool', href=UrlIndex.UNIVERSITY_LIVERPOOL.value),
                            """. Our research focuses in the creation of new software tools to aimed  
                            applications of residue contact predictions both in the 
                            field of molecular replacement and """,
                            html.I('ab initio'),
                            """ protein modelling."""
                        ], style={"font-size": "150%", "text-align": "justify"}),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.H6('Other tools by Rigden Lab', className="card-text", style={'text-align': "center"}),
                        html.Hr(),
                        html.Br(),
                        html.P([
                            """Here we will put the other tools we have a the group with links to their pages"""
                        ]),
                        html.Br()
                    ])
                ])
            ]),
        ]
    )


def RigdenLab(session_id):
    return html.Div([
        Header(),
        NavBar(UrlIndex.RIGDEN.value),
        Body(session_id),
    ])
