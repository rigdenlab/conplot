import components
from utils import UrlIndex
import dash_html_components as html
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
                            html.H2('ConPlot Website Privacy Policy. Updated: 03/07/2020',
                                    className="card-text", style={'text-align': "center"}),
                            html.Br(),
                            html.Br(),
                            html.H4('1. Introduction', style={'text-align': "center"}),
                            html.Hr(),
                            components.GdprPolicySectionOne(),
                            html.Br(),
                            html.H4('2. Information Automatically Collected', style={'text-align': "center"}),
                            html.Hr(),
                            components.GdprPolicySectionTwo(),
                            html.Br(),
                            html.H4('3. Information You Directly Provide', style={'text-align': "center"}),
                            html.Hr(),
                            components.GdprPolicySectionThree(),
                            html.Br(),
                            html.H4('4. "Get in Touch" Form', style={'text-align': "center"}),
                            html.Hr(),
                            components.GdprPolicySectionFour(),
                            html.Br(),
                            html.H4('5. How ConPlot uses cookies', style={'text-align': "center"}),
                            html.Hr(),
                            components.GdprPolicySectionFive(),
                            html.Br(),
                            html.H4('6. Your Rights based on the General Data Protection Regulation (GDPR)',
                                    style={'text-align': "center"}),
                            html.Hr(),
                            components.GdprPolicySectionSix(),
                            components.GdprRightsList(),
                        ])
                    ])
                ], width=10),
            ], align='center', justify='center', className='m-0')
        ]
    )


def PrivacyPolicy(session_id):
    return html.Div([
        components.Header(),
        components.NavBar(UrlIndex.PRIVACY_POLICY.value),
        Body(),
    ])
