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


def SuccesfulSessionLoadToast(session_name):
    return dbc.Toast(
        "You have loaded session '%s'" % session_name,
        id="positioned-toast",
        header="Session loaded",
        is_open=True,
        dismissable=True,
        icon="success",
        style={"position": "fixed", "top": 66, "right": 10, "width": 350},
    )


def SuccesfulSessionDeleteToast(session_name):
    return dbc.Toast(
        "You have deleted session '%s'" % session_name,
        id="positioned-toast",
        header="Session removed",
        is_open=True,
        dismissable=True,
        icon="danger",
        style={"position": "fixed", "top": 66, "right": 10, "width": 350},
    )


def SuccesfulSessionStopShareToast():
    return dbc.Toast(
        "You have stopped sharing the session",
        id="positioned-toast",
        header="Session no longer shared",
        is_open=True,
        dismissable=True,
        icon="danger",
        style={"position": "fixed", "top": 66, "right": 10, "width": 350},
    )


def SuccesfulSessionShareToast(username):
    return dbc.Toast(
        "You are now sharing the session with %s" % username,
        id="positioned-toast",
        header="Session shared",
        is_open=True,
        dismissable=True,
        icon="success",
        style={"position": "fixed", "top": 66, "right": 10, "width": 350},
    )


def FailedSessionShareToast(username):
    return dbc.Toast(
        "We cannot find a user with the name '%s'. Please make sure you share a session with an existing user"
        "" % username,
        id="positioned-toast",
        header="User not found",
        is_open=True,
        dismissable=True,
        icon="danger",
        style={"position": "fixed", "top": 66, "right": 10, "width": 350},
    )


def SessionAlreadyShared(share_with):
    return dbc.Toast(
        "You are already sharing this session with %s" % share_with,
        id="positioned-toast",
        header="Invalid input",
        is_open=True,
        dismissable=True,
        icon="danger",
        style={"position": "fixed", "top": 66, "right": 10, "width": 350},
    )


def ShareWithOwnerToast():
    return dbc.Toast(
        "You are trying to share this session with yourself! You do not need to do this, you are the owner of the "
        "session and you will always have access to it.",
        id="positioned-toast",
        header="Invalid input",
        is_open=True,
        dismissable=True,
        icon="danger",
        style={"position": "fixed", "top": 66, "right": 10, "width": 350},
    )


def InvalidUsernameToast():
    return dbc.Toast(
        "Please provide a valid username to share the session with",
        id="positioned-toast",
        header="Invalid input",
        is_open=True,
        dismissable=True,
        icon="danger",
        style={"position": "fixed", "top": 66, "right": 10, "width": 350},
    )
