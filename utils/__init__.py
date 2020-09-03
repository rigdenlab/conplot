import os
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


def get_base_url():
    if 'PRODUCTION_SERVER' in os.environ:
        return '/conplot'
    else:
        return ''


class UrlIndex(Enum):
    """An enumerator with an index of all the paths in conplot-web"""
    ROOT = '/conplot'
    HOME = '{}/home'.format(get_base_url())
    PLOT = '{}/plot'.format(get_base_url())
    CONTACT = '{}/contact'.format(get_base_url())
    RIGDEN = '{}/ridgen-group'.format(get_base_url())
    HELP = '{}/help'.format(get_base_url())
    USERS_PORTAL = '{}/users-portal'.format(get_base_url())
    CREATE_USER = '{}/new-user'.format(get_base_url())
    USER_STORAGE = '{}/user-storage'.format(get_base_url())
    SHARE_SESSIONS = '{}/user-share'.format(get_base_url())
    CHANGE_PASSWORD = '{}/user-change-password'.format(get_base_url())
    SESSION_TIMEOUT = '{}/session-timeout'.format(get_base_url())
    PRIVACY_POLICY = '{}/privacy-policy-statement'.format(get_base_url())
    GITHUB_LOGO = '{}/assets/github_logo.png'.format(get_base_url())
    HELP_FIG1 = '{}/static/Help_Figure_1.png'.format(get_base_url())
    TUTORIAL1_FIG1 = '{}/static/Tutorial1_Figure1.png'.format(get_base_url())
    TUTORIAL1_FIG2 = '{}/static/Tutorial1_Figure2.png'.format(get_base_url())
    TUTORIAL1_FIG3 = '{}/static/Tutorial1_Figure3.png'.format(get_base_url())
    TUTORIAL1_FIG4 = '{}/static/Tutorial1_Figure4.png'.format(get_base_url())
    TUTORIAL1_FIG5 = '{}/static/Tutorial1_Figure5.png'.format(get_base_url())
    TUTORIAL1_FIG6 = '{}/static/Tutorial1_Figure6.png'.format(get_base_url())
    TUTORIAL1_FIG7 = '{}/static/Tutorial1_Figure7.png'.format(get_base_url())
    TUTORIAL2_FIG1 = '{}/static/Tutorial2_Figure1.png'.format(get_base_url())
    TUTORIAL2_FIG2 = '{}/static/Tutorial2_Figure2.png'.format(get_base_url())
    TUTORIAL2_FIG3 = '{}/static/Tutorial2_Figure3.png'.format(get_base_url())
    TUTORIAL3_FIG1 = '{}/static/Tutorial3_Figure1.png'.format(get_base_url())
    TUTORIAL3_FIG2 = '{}/static/Tutorial3_Figure2.png'.format(get_base_url())
    TUTORIAL3_FIG3 = '{}/static/Tutorial3_Figure3.png'.format(get_base_url())
    TUTORIAL3_FIG4 = '{}/static/Tutorial3_Figure4.png'.format(get_base_url())
    TUTORIAL3_FIG5 = '{}/static/Tutorial3_Figure5.png'.format(get_base_url())
    TUTORIAL3_FIG6 = '{}/static/Tutorial3_Figure6.png'.format(get_base_url())
    TUTORIAL3_FIG7 = '{}/static/Tutorial3_Figure7.png'.format(get_base_url())
    CONPLOT_LOGO = '{}/assets/conplot_logo.png'.format(get_base_url())
    SWAMP_LOGO = '{}/assets/swamp_logo.png'.format(get_base_url())
    SIMBAD_LOGO = '{}/assets/simbad_logo.png'.format(get_base_url())
    AMPLE_LOGO = '{}/assets/ample_logo.png'.format(get_base_url())
    CONKIT_LOGO = '{}/assets/conkit_logo.png'.format(get_base_url())
    RIGDEN_GITHUB = 'https://github.com/rigdenlab'
    GITHUB = 'https://github.com/rigdenlab/conplot'
    FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
    SWAMP_READDOCS = 'https://swamp.readthedocs.io/en/latest/'
    SIMBAD_READDOCS = 'https://simbad.readthedocs.io/en/latest/'
    AMPLE_READDOCS = 'https://ample.readthedocs.io/en/latest/'
    CONKIT_READDOCS = 'https://conkit.readthedocs.io/en/latest/'
    EXAMPLE_DATA = 'https://github.com/rigdenlab/conplot-examples/archive/master.zip'
    UNIVERSITY_LIVERPOOL = 'https://www.liverpool.ac.uk/'
    TOPCONS_WEB = 'http://topcons.cbr.su.se/'
    TOPCONS_CITATION = 'https://dx.doi.org/10.1093%2Fnar%2Fgkv485'
    PSIPRED_WEB = 'http://bioinf.cs.ucl.ac.uk/psipred/'
    PSIPRED_CITATION = 'https://doi.org/10.1093/nar/gkz297'
    IUPRED_WEB = 'https://iupred2a.elte.hu/'
    IUPRED_CITATION = 'https://doi.org/10.1093/nar/gky384'
    CONSURF_WEB = 'https://consurf.tau.ac.il/'
    CONSURF_CITATION = 'https://doi.org/10.1093/nar/gkw408'
    GDPR_WEBSITE = 'https://gdpr-info.eu'


def create_ConPlot(*args, **kwargs):
    from utils.plot_utils import create_ConPlot

    return create_ConPlot(*args, **kwargs)


def compressStringToBytes(*args, **kwargs):
    from utils.cache_utils import compressStringToBytes

    return compressStringToBytes(*args, **kwargs)


def retrieve_sequence_fname(*args, **kwargs):
    from utils.callback_utils import retrieve_sequence_fname

    return retrieve_sequence_fname(*args, **kwargs)


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


def is_postgres_available(*args, **kwargs):
    from utils.postgres_utils import is_postgres_available

    return is_postgres_available(*args, **kwargs)


def ensure_triggered(*args, **kwargs):
    from utils.callback_utils import ensure_triggered

    return ensure_triggered(*args, **kwargs)


def toggle_alert(*args, **kwargs):
    from utils.callback_utils import toggle_alert

    return toggle_alert(*args, **kwargs)


def get_session_action(*args, **kwargs):
    from utils.callback_utils import get_session_action

    return get_session_action(*args, **kwargs)


def unique_by_key(elements, key=None):
    # Credits to: https://stackoverflow.com/questions/31499259/making-a-sequence-of-tuples-unique-by-a-specific-element
    if key is None:
        # no key: the whole element must be unique
        key = lambda e: e
    return list({key(el): el for el in elements}.values())
