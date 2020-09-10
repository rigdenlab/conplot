from utils import UrlIndex, get_display_control_card, load_display_settings, load_figure_json
import dash_core_components as dcc
import dash_html_components as html
from components import NavBar, Header, PlotPlaceHolder, DisplayControlCard, MandatoryUploadCard, \
    AdditionalTracksUploadCard, StoreSessionCard
import dash_bootstrap_components as dbc


def Body(username, figure_json=None, display_settings_json=None):
    if figure_json is None:
        graph = PlotPlaceHolder()
    else:
        graph = dcc.Graph(
            className='square-content', id='plot-graph', figure=load_figure_json(figure_json),
            config={'displaylogo': False, 'modeBarButtonsToRemove': ['select2d', 'lasso2d'],
                    "toImageButtonOptions": {"width": None, "height": None}}
        )

    if display_settings_json is None:
        display_control_card = DisplayControlCard()
        adjust_plot_disabled = True
    else:
        display_settings = load_display_settings(display_settings_json)
        display_control_card = get_display_control_card(display_settings)
        adjust_plot_disabled = False

    return html.Div([
        dbc.Spinner(html.Div(id='contact-upload-modal-div'), fullscreen=True, fullscreenClassName="spinner-with-text"),
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
                    graph
                ], id='plot-div', className='square-box')
            ], id='plot-column', width=5, style={'align-items': 'center', 'text-align': 'center', 'display': 'flex'}),
            dbc.Col([
                html.Div([
                    dbc.Card([
                        dbc.CardBody(
                            display_control_card, id='display-control-cardbody'
                        )
                    ])
                ], className='InputPanel', style={'height': '70vh', 'overflow-y': 'scroll'}),
                html.Br(),
                html.Br(),
                dbc.Button('Adjust Plot', outline=True, color='primary', block=True, id='refresh-button-2',
                           disabled=adjust_plot_disabled)
            ], width=3, style={'height': '100%'}),
        ], justify="between", style={'display': 'flex'}, className='m-0')
    ])


def Plot(session_id, username, figure=None, display_settings=None):
    return html.Div([
        Header(username),
        NavBar(UrlIndex.PLOT.value),
        Body(username, figure, display_settings)
    ])
