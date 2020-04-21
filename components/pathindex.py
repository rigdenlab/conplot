from enum import Enum


class PathIndex(Enum):
    """An enumerator with an index of all the paths in conkit-web"""
    ROOT = '/conkit-web/'
    HOME = '/conkit-web/home/'
    PLOT = '/conkit-web/plot/'
    DATAUPLOAD = '/conkit-web/plot/dataupload/'
    PLOTDISPLAY = '//conkit-web/plot/display/'
    CONTACT = '/conkit-web/contact/'
    GITHUB = 'https://github.com/rigdenlab/conkit-web'
