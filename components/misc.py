import dash_bootstrap_components as dbc
import dash_html_components as html
from utils import UrlIndex


def PlotPlaceHolder():
    return html.Div([
        html.Img(
            src=UrlIndex.CONPLOT_LOGO.value,
            style={'display': 'block', 'vertical-align': 'middle', 'margin': 'auto', 'position': 'absolute',
                   'top': '0', 'bottom': '0', 'left': '0', 'right': '0'}
        )
    ], className='square-content')


def UserAccountDropdownMenu(username=None):
    if username is None:
        username = 'LOGIN'

    return dbc.Row([
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem("User identification", header=True),
                dbc.DropdownMenuItem("Login/Logout", href=UrlIndex.USERS_PORTAL.value),
                dbc.DropdownMenuItem("Create a new account", href=UrlIndex.CREATE_USER.value),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Members only area", header=True),
                dbc.DropdownMenuItem("Access personal storage", href=UrlIndex.USER_STORAGE.value),
                dbc.DropdownMenuItem("Share sessions", href=UrlIndex.SHARE_SESSIONS.value),
                dbc.DropdownMenuItem("Change your password", href=UrlIndex.CHANGE_PASSWORD.value),
                dbc.DropdownMenuItem(divider=True),
            ], label=username, right=True, bs_size="md", id='user-account-dropdown'
        )
    ], no_gutters=True, className="ml-auto flex-nowrap mt-3 mt-md-0 mr-2", align="center")


def ConPlotBrand():
    return dbc.Row(
        [
            dbc.Col(html.Img(src=UrlIndex.CONPLOT_LOGO.value, height="75vh", className='m-0')),
            dbc.Col(html.H1('ConPlot', style={'font-size': '7vh'}), className="ml-2 mt-2"),
        ],
        align="center",
        no_gutters=True,
        className='m-2'
    )
