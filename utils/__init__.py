import urllib.parse
from enum import Enum


class WimleyWhiteHydrophobicityScale(Enum):
    I = -0.81
    L = -0.69
    F = -0.58
    V = -0.53
    M = -0.44
    P = -0.31
    W = -0.24
    H = -0.06
    T = 0.11
    E = 0.12
    Q = 0.19
    C = 0.22
    Y = 0.23
    A = 0.33
    S = 0.33
    N = 0.43
    D = 0.5
    R = 1.0
    G = 1.14
    K = 1.81


class UrlIndex(Enum):
    """An enumerator with an index of all the paths in conplot-web"""
    ROOT = '/'
    HOME = urllib.parse.urljoin(ROOT, 'home')
    PLOT = urllib.parse.urljoin(ROOT, 'plot')
    CONTACT = urllib.parse.urljoin(ROOT, 'contact')
    RIGDEN = urllib.parse.urljoin(ROOT, 'ridgen-group')
    HELP = urllib.parse.urljoin(ROOT, 'help')
    USERS_PORTAL = urllib.parse.urljoin(ROOT, 'users-area')
    CREATE_USER = urllib.parse.urljoin(USERS_PORTAL, 'new-user')
    USER_STORAGE = urllib.parse.urljoin(USERS_PORTAL, 'storage')
    SHARE_SESSIONS = urllib.parse.urljoin(USERS_PORTAL, 'share')
    CHANGE_PASSWORD = urllib.parse.urljoin(USERS_PORTAL, 'change-password')
    SESSION_TIMEOUT = urllib.parse.urljoin(ROOT, 'session-timeout')
    RIGDEN_GITHUB = 'https://github.com/rigdenlab'
    GITHUB = 'https://github.com/rigdenlab/conplot'
    FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
    GITHUB_LOGO = '/assets/github_logo.png'
    CONPLOT_LOGO = '/assets/conplot_logo.png'
    STATIC_DATA = 'https://github.com/rigdenlab/conplot/tree/master/static/data'
    UNIVERSITY_LIVERPOOL = 'https://www.liverpool.ac.uk/'


def create_ConPlot(*args, **kwargs):
    from utils.plot_utils import create_ConPlot

    return create_ConPlot(*args, **kwargs)


def compressStringToBytes(*args, **kwargs):
    from utils.cache_utils import compressStringToBytes

    return compressStringToBytes(*args, **kwargs)


def CacheKeys(*args, **kwargs):
    from utils.cache_utils import CacheKeys

    return CacheKeys(*args, **kwargs)


def decompress_data(*args, **kwargs):
    from utils.cache_utils import decompress_data

    return decompress_data(*args, **kwargs)


def compress_data(*args, **kwargs):
    from utils.cache_utils import compress_data

    return compress_data(*args, **kwargs)


def get_upload_id(*args, **kwargs):
    from utils.callback_utils import get_upload_id

    return get_upload_id(*args, **kwargs)


def get_remove_trigger(*args, **kwargs):
    from utils.callback_utils import get_remove_trigger

    return get_remove_trigger(*args, **kwargs)


def remove_unused_fname_alerts(*args, **kwargs):
    from utils.callback_utils import remove_unused_fname_alerts

    return remove_unused_fname_alerts(*args, **kwargs)


def toggle_selection_alert(*args, **kwargs):
    from utils.callback_utils import toggle_selection_alert

    return toggle_selection_alert(*args, **kwargs)


def decompressBytesToString(*args, **kwargs):
    from utils.cache_utils import decompressBytesToString

    return decompressBytesToString(*args, **kwargs)


def decompress_session(*args, **kwargs):
    from utils.session_utils import decompress_session

    return decompress_session(*args, **kwargs)


def ensure_triggered(*args, **kwargs):
    from utils.callback_utils import ensure_triggered

    return ensure_triggered(*args, **kwargs)


def toggle_alert(*args, **kwargs):
    from utils.callback_utils import toggle_alert

    return toggle_alert(*args, **kwargs)


def get_session_action(*args, **kwargs):
    from utils.callback_utils import get_session_action

    return get_session_action(*args, **kwargs)


def get_hydrophobicity(*args, **kwargs):
    from utils.data_utils import get_hydrophobicity

    return get_hydrophobicity(*args, **kwargs)
