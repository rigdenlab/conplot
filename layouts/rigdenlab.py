from utils import UrlIndex
import dash_html_components as html
from components import NavBar, Header, AmpleJumbotron, SwampJumbotron, SimbadJumbotron, ConkitJumbotron
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
                            html.H3('Rigden Lab', className="card-text", style={'text-align': "center"}),
                            html.Br(),
                            html.P([
                                """We are a structural bioinformatics group based at the """,
                                html.A(html.U('University of Liverpool'), href=UrlIndex.UNIVERSITY_LIVERPOOL.value),
                                """. Our research focuses on the creation of new software tools aimed at the 
                                applications of residue contact predictions in the fields of molecular replacement 
                                and """,
                                html.I('ab initio'),
                                """ protein modelling. If you work in any of these fields and you enjoyed using 
                                ConPlot, here are some of the tools we have developed that you may also find useful."""
                            ], style={"font-size": "120%", "text-align": "justify"}),
                            html.Br(),
                            html.Br(),
                            AmpleJumbotron(),
                            ConkitJumbotron(),
                            SimbadJumbotron(),
                            SwampJumbotron(),
                            html.Br()
                        ])
                    ])
                ], width=10),
            ], justify='center', align='center', className='m-0')
        ]
    )


def RigdenLab(session_id, username):
    return html.Div([
        Header(username),
        NavBar(UrlIndex.RIGDEN.value),
        Body(),
    ])
