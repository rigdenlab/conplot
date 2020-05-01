import urllib.parse
from enum import Enum


class PathIndex(Enum):
    """An enumerator with an index of all the paths in conkit-web"""
    ROOT = 'https://random-cheesecake.herokuapp.com/'
    # ROOT = '/'
    HOME = urllib.parse.urljoin(ROOT, 'home')
    PLOT = urllib.parse.urljoin(ROOT, 'plot')
    DATAUPLOAD = urllib.parse.urljoin(PLOT, 'dataupload')
    PLOTDISPLAY = urllib.parse.urljoin(PLOT, 'display')
    CONTACT = urllib.parse.urljoin(ROOT, 'contact')
    GITHUB = 'https://github.com/rigdenlab/conkit-web'
    RIGDEN = urllib.parse.urljoin(ROOT, 'ridgen-group')
    HELP = urllib.parse.urljoin(ROOT, 'help')
    FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
    GITHUB_LOGO = 'https://raw.githubusercontent.com/rigdenlab/conkit-web/master/assets/github_logo.png'
    CONKIT_LOGO = 'https://raw.githubusercontent.com/rigdenlab/conkit-web/master/assets/conkit_small_logo.png'


def Session(*args, **kwargs):
    from core.session import Session

    return Session(*args, **kwargs)


def Plot(*args, **kwargs):
    from core.plot import Plot

    return Plot(*args, **kwargs)
