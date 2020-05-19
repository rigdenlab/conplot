import dash_bootstrap_components as dbc


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
