from enum import Enum


class PathIndex(Enum):
    """An enumerator with an index of all the paths in conkit-web"""
    ROOT = '/conkit-web/'
    HOME = '/conkit-web/home/'
    PLOT = '/conkit-web/plot/'
    DATAUPLOAD = '/conkit-web/plot/dataupload/'
    PLOTDISPLAY = '/conkit-web/plot/display/'
    CONTACT = '/conkit-web/contact/'
    GITHUB = 'https://github.com/rigdenlab/conkit-web'
    RIGDEN = '/conkit-web/ridgen-group/'
    HELP = '/conkit-web/help/'
    FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
    GITHUB_LOGO = '/conkit-web/home/assets/github_logo.png'
    CONKIT_LOGO = '/conkit-web/home/assets/conkit_small_logo.png'


def Session(*args, **kwargs):
    from core.session import Session

    return Session(*args, **kwargs)


def Plot(*args, **kwargs):
    from core.plot import Plot

    return Plot(*args, **kwargs)
