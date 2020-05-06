from utils import PathIndex
import dash_html_components as html
from components import NavBar, Header, PlotPlaceHolder, DisplayControlCard, MandatoryUploadCard, \
    AdditionalTracksUploadCard
import dash_bootstrap_components as dbc


def Plot(session_id):
    return html.Div([
        html.Div(id='_hidden-div', style={'display': 'none'}),
        Header(),
        html.Div(id='inputs-modal-div'),
        html.Div(id='removefiles-modal-div'),
        html.Div(id='plot-modal-div'),
        html.Div(id='addtrack-modal-div'),
        NavBar(PathIndex.PLOT.value),
        html.Br(),
        html.Br(),
        dbc.Row([
            dbc.Col([
                html.Div([
                    dbc.Card([
                        dbc.CardBody(
                            MandatoryUploadCard()
                        ),
                        dbc.CardBody(
                            AdditionalTracksUploadCard(),
                        )
                    ])
                ], className='InputPanel', style={'height': '70vh', 'overflow-y': 'scroll'}),
                html.Br(),
                html.Br(),
                dbc.Button('Plot', id='plot-button', color="primary", block=True),
            ], width=3, style={'height': '100%'}),
            dbc.Col([
                dbc.Spinner([
                    html.Div([
                        PlotPlaceHolder()
                    ], id='plot-div', className='square-box')
                ])
            ], id='plot-column', width=5, style={'align-items': 'center', 'text-align': 'center', 'display': 'flex'}),
            dbc.Col([
                html.Div([
                    dbc.Spinner([
                        dbc.Card([
                            dbc.CardBody(
                                DisplayControlCard(), id='display-control-cardbody'
                            )
                        ])
                    ])
                ], className='InputPanel', style={'height': '73vh', 'overflow-y': 'scroll'}),
            ], width=3, style={'height': '100%'}),
        ], justify="between", style={'display': 'flex'}),
    ])
