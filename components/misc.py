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


def SuccesfulLoginToast(username):
    return dbc.Toast(
        "Logged in as %s" % username,
        id="positioned-toast",
        header="Successful login",
        is_open=True,
        dismissable=True,
        icon="success",
        style={"position": "fixed", "top": 66, "right": 10, "width": 350},
    )


def SessionTimedOutToast():
    return dbc.Toast(
        "Session has timed-out!",
        id="positioned-toast",
        header="Session timed-out",
        is_open=True,
        dismissable=True,
        icon="danger",
        style={"position": "fixed", "top": 66, "right": 10, "width": 350},
    )


def SuccesfulLogoutToast():
    return dbc.Toast(
        "You have logged out!",
        id="positioned-toast",
        header="User log out",
        is_open=True,
        dismissable=True,
        icon="danger",
        style={"position": "fixed", "top": 66, "right": 10, "width": 350},
    )


def UserAccountDropdownMenu(username=None):
    # TODO: IMPORTANT, WE WONT ALLOW THE USERS TO CREATE A USER WITH USERNAME USER
    if username is None:
        store_disabled = True
        username = 'USER'
    else:
        store_disabled = False

    return dbc.Row([
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem("User identification", header=True),
                dbc.DropdownMenuItem("Login/Logout", href=UrlIndex.USERS_PORTAL.value),
                dbc.DropdownMenuItem("Create a new account", href=UrlIndex.CREATE_USER.value),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Members only area", header=True),
                dbc.DropdownMenuItem("Access stored sessions", disabled=store_disabled),
                dbc.DropdownMenuItem(divider=True),
            ], label=username, right=True, bs_size="md", id='user-account-dropdown'
        )
    ], no_gutters=True, className="ml-auto flex-nowrap mt-3 mt-md-0", align="center")
