import urllib.parse
from enum import Enum


class PathIndex(Enum):
    """An enumerator with an index of all the paths in conplot-web"""
    ROOT = '/'
    HOME = urllib.parse.urljoin(ROOT, 'home')
    PLOT = urllib.parse.urljoin(ROOT, 'plot')
    CONTACT = urllib.parse.urljoin(ROOT, 'contact')
    GITHUB = 'https://github.com/rigdenlab/conplot'
    RIGDEN = urllib.parse.urljoin(ROOT, 'ridgen-group')
    HELP = urllib.parse.urljoin(ROOT, 'help')
    FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
    GITHUB_LOGO = 'https://raw.githubusercontent.com/rigdenlab/conplot/master/assets/github_logo.png'
    CONKIT_LOGO = 'https://raw.githubusercontent.com/rigdenlab/conplot/master/assets/conkit_small_logo.png'


def create_ConPlot(*args, **kwargs):
    from utils.plot_utils import create_ConPlot

    return create_ConPlot(*args, **kwargs)


def compressStringToBytes(*args, **kwargs):
    from utils.cache_utils import compressStringToBytes

    return compressStringToBytes(*args, **kwargs)


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


def initiate_session():
    from utils.session_utils import initiate_session

    return initiate_session()


def compress_session(*args, **kwargs):
    from utils.session_utils import compress_session

    return compress_session(*args, **kwargs)


def decompress_session(*args, **kwargs):
    from utils.session_utils import decompress_session

    return decompress_session(*args, **kwargs)


def ensure_triggered(*args, **kwargs):
    from utils.callback_utils import ensure_triggered

    return ensure_triggered(*args, **kwargs)


def toggle_alert(*args, **kwargs):
    from utils.callback_utils import toggle_alert

    return toggle_alert(*args, **kwargs)


def display_page(*args, **kwargs):
    from utils.callback_utils import display_page

    return display_page(*args, **kwargs)
