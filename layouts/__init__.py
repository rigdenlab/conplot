from enum import Enum


class ContextReference(Enum):
    PLOT_CLICK = 'plot-button.n_clicks'


def noPage(*args, **kwargs):
    from layouts.nopage import noPage

    return noPage(*args, **kwargs)


def RedisConnectionError(*args, **kwargs):
    from layouts.redisconnectionerror import RedisConnectionError

    return RedisConnectionError(*args, **kwargs)


def PrivacyPolicy(*args, **kwargs):
    from layouts.privacypolicy import PrivacyPolicy

    return PrivacyPolicy(*args, **kwargs)


def Home(*args, **kwargs):
    from layouts.home import Home

    return Home(*args, **kwargs)


def UsersPortal(*args, **kwargs):
    from layouts.userportal import UsersPortal

    return UsersPortal(*args, **kwargs)


def Base(*args, **kwargs):
    from layouts.base import Base

    return Base(*args, **kwargs)


def ShareSession(*args, **kwargs):
    from layouts.sharesession import ShareSession

    return ShareSession(*args, **kwargs)


def UserStorage(*args, **kwargs):
    from layouts.userstorage import UserStorage

    return UserStorage(*args, **kwargs)


def ChangeUserPassword(*args, **kwargs):
    from layouts.changeuserpassword import ChangeUserPassword

    return ChangeUserPassword(*args, **kwargs)


def CreateUser(*args, **kwargs):
    from layouts.createuser import CreateUser

    return CreateUser(*args, **kwargs)


def RigdenLab(*args, **kwargs):
    from layouts.rigdenlab import RigdenLab

    return RigdenLab(*args, **kwargs)


def Help(*args, **kwargs):
    from layouts.help import Help

    return Help(*args, **kwargs)


def Contact(*args, **kwargs):
    from layouts.contact import Contact

    return Contact(*args, **kwargs)


def SessionTimeout(*args, **kwargs):
    from layouts.session_timeout import SessionTimeout

    return SessionTimeout(*args, **kwargs)


def Plot(*args, **kwargs):
    from layouts.plot import Plot

    return Plot(*args, **kwargs)
