from utils import UrlIndex
import dash_html_components as html
from components import NavBar, Header, PlotPlaceHolder, DisplayControlCard, MandatoryUploadCard, \
    AdditionalTracksUploadCard, StoreSessionCard
import dash_bootstrap_components as dbc


def Body(username):
    return html.Div([
        html.Div(id='_hidden-div', style={'display': 'none'}),
        dbc.Spinner(html.Div(id='contact-upload-modal-div'), fullscreen=True),
        dbc.Spinner(html.Div(id='sequence-upload-modal-div'), fullscreen=True),
        dbc.Spinner(html.Div(id='removefiles-modal-div'), fullscreen=True),
        dbc.Spinner(html.Div(id='plot-modal-div'), fullscreen=True),
        dbc.Spinner(html.Div(id='additional-tracks-upload-modal-div'), fullscreen=True),
        dbc.Spinner(html.Div(id='store-session-modal-div'), fullscreen=True),
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
                        ),
                        dbc.CardBody(
                            StoreSessionCard(username),
                        )
                    ])
                ], className='InputPanel', style={'height': '70vh', 'overflow-y': 'scroll'}),
                html.Br(),
                html.Br(),
                dbc.Button('Generate Plot', id='plot-button', color="primary", block=True),
            ], width=3, style={'height': '100%'}),
            dbc.Col([
                html.Div([
                    PlotPlaceHolder()
                ], id='plot-div', className='square-box')
            ], id='plot-column', width=5, style={'align-items': 'center', 'text-align': 'center', 'display': 'flex'}),
            dbc.Col([
                html.Div([
                    dbc.Card([
                        dbc.CardBody(
                            DisplayControlCard(), id='display-control-cardbody'
                        )
                    ])
                ], className='InputPanel', style={'height': '70vh', 'overflow-y': 'scroll'}),
                html.Br(),
                html.Br(),
                dbc.Button('Adjust Plot', outline=True, color='primary', block=True, id='refresh-button-2',
                           disabled=True)
            ], width=3, style={'height': '100%'}),
        ], justify="between", style={'display': 'flex'}, className='m-0')
    ])


def Plot(session_id, username):
    return html.Div([
        Header(username),
        NavBar(UrlIndex.PLOT.value),
        Body(username)
    ])
