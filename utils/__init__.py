import os
from operator import itemgetter
from enum import Enum
from fast_enum import FastEnum


def conplot_version():
    return 'v0.4'


def get_base_url():
    if 'PRODUCTION_SERVER' in os.environ:
        return '/conplot'
    else:
        return ''


class DistanceLabels(FastEnum):
    BIN_0 = 'd ≤ 4Å'
    BIN_1 = '4Å < d ≤ 6Å'
    BIN_2 = '6Å < d ≤ 8Å'
    BIN_3 = '8Å < d ≤ 10Å'
    BIN_4 = '10Å < d ≤ 12Å'
    BIN_5 = '12Å < d ≤ 14Å'
    BIN_6 = '14Å < d ≤ 16Å'
    BIN_7 = '16Å < d ≤ 18Å'
    BIN_8 = '18Å < d ≤ 20Å'
    BIN_9 = 'd > 20Å'


class HoverTemplates(FastEnum):
    DISTOGRAM = 'Contact: {} - {}<br>Distance {}<br>Confidence: {}'
    DISTOGRAM_VERBOSE = 'Contact: {} - {}<br>Distance {}<br>Confidence: {}<br>{}<br>{}'
    CMAP = 'Contact: {} - {}<br>Confidence: {}'
    CMAP_VERBOSE = 'Contact: {} - {}<br>Confidence: {}<br>{}<br>{}'
    CMAP_SUPERIMPOSE = 'Contact: {} - {}<br>Map A Confidence: {}<br>Map B Confidence: {}'
    CMAP_SUPERIMPOSE_VERBOSE = 'Contact: {} - {}<br>Map A Confidence: {}<br>Map B Confidence: {}<br>{}<br>{}'
    DISTOGRAM_SUPERIMPOSE = 'Contact: {} - {}<br>Map A Distance {}<br>Map B Distance {}<br>Error: {}'
    DISTOGRAM_SUPERIMPOSE_VERBOSE = 'Contact: {} - {}<br>Map A Distance {}<br>Map B Distance {}<br>Error: {}<br>{}<br>{}'


class UrlIndex(Enum):
    """An enumerator with an index of all the paths in conplot-web"""
    ROOT = '/{}'.format(get_base_url())
    HOME = '{}/home'.format(get_base_url())
    PLOT = '{}/plot'.format(get_base_url())
    CONTACT = '{}/contact'.format(get_base_url())
    RIGDEN = '{}/rigden-group'.format(get_base_url())
    HELP = '{}/help'.format(get_base_url())
    USERS_PORTAL = '{}/users-portal'.format(get_base_url())
    CREATE_USER = '{}/new-user'.format(get_base_url())
    USER_STORAGE = '{}/user-storage'.format(get_base_url())
    SHARE_SESSIONS = '{}/user-share'.format(get_base_url())
    CHANGE_PASSWORD = '{}/user-change-password'.format(get_base_url())
    SESSION_TIMEOUT = '{}/session-timeout'.format(get_base_url())
    PRIVACY_POLICY = '{}/privacy-policy-statement'.format(get_base_url())
    ACCOUNT_RECOVERY = '{}/account-recovery'.format(get_base_url())
    GITHUB_LOGO = '{}/assets/github_logo.png'.format(get_base_url())
    HELP_FIG1 = '{}/static/Help_Figure_1.png'.format(get_base_url())
    TUTORIAL1_FIG1 = '{}/static/Tutorial1_Figure1.png'.format(get_base_url())
    TUTORIAL1_FIG2 = '{}/static/Tutorial1_Figure2.png'.format(get_base_url())
    TUTORIAL1_FIG3 = '{}/static/Tutorial1_Figure3.png'.format(get_base_url())
    TUTORIAL1_FIG4 = '{}/static/Tutorial1_Figure4.png'.format(get_base_url())
    TUTORIAL1_FIG5 = '{}/static/Tutorial1_Figure5.png'.format(get_base_url())
    TUTORIAL1_FIG6 = '{}/static/Tutorial1_Figure6.png'.format(get_base_url())
    TUTORIAL1_FIG7 = '{}/static/Tutorial1_Figure7.png'.format(get_base_url())
    TUTORIAL1_FIG8 = '{}/static/Tutorial1_Figure8.png'.format(get_base_url())
    TUTORIAL1_FIG9 = '{}/static/Tutorial1_Figure9.png'.format(get_base_url())
    TUTORIAL1_FIG10 = '{}/static/Tutorial1_Figure10.png'.format(get_base_url())
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
    TUTORIAL4_FIG1 = '{}/static/Tutorial4_Figure1.png'.format(get_base_url())
    TUTORIAL4_FIG2 = '{}/static/Tutorial4_Figure2.png'.format(get_base_url())
    CONPLOT_LOGO = '{}/assets/conplot_logo.png'.format(get_base_url())
    SWAMP_LOGO = '{}/assets/swamp_logo.png'.format(get_base_url())
    SIMBAD_LOGO = '{}/assets/simbad_logo.png'.format(get_base_url())
    AMPLE_LOGO = '{}/assets/ample_logo.png'.format(get_base_url())
    CONKIT_LOGO = '{}/assets/conkit_logo.png'.format(get_base_url())
    RIGDEN_GITHUB = 'https://github.com/rigdenlab'
    GITHUB = 'https://github.com/rigdenlab/conplot'
    GITHUB_ISSUE = 'https://github.com/rigdenlab/conplot/issues/new?assignees=&labels=&template=bug_report.md&title='
    FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
    SWAMP_READDOCS = 'https://swamp.readthedocs.io/en/latest/'
    SIMBAD_READDOCS = 'https://simbad.readthedocs.io/en/latest/'
    AMPLE_READDOCS = 'https://ample.readthedocs.io/en/latest/'
    CONKIT_READDOCS = 'https://conkit.readthedocs.io/en/latest/'
    EXAMPLE_DATA = 'https://github.com/rigdenlab/conplot-examples/archive/master.zip'
    UNIVERSITY_LIVERPOOL = 'https://www.liverpool.ac.uk/'
    CCP4_ONLINE = 'https://www.ccp4.ac.uk/'
    CASP14_RRFORMAT = 'https://predictioncenter.org/casp14/index.cgi?page=format'
    TRROSETTA_SERVER = 'https://yanglab.nankai.edu.cn/trRosetta/'
    MAPPRED_SERVER = 'https://yanglab.nankai.edu.cn/MapPred/'
    TOPCONS_WEB = 'http://topcons.cbr.su.se/'
    TOPCONS_CITATION = 'https://dx.doi.org/10.1093%2Fnar%2Fgkv485'
    PSIPRED_WEB = 'http://bioinf.cs.ucl.ac.uk/psipred/'
    PSIPRED_CITATION = 'https://doi.org/10.1093/nar/gkz297'
    IUPRED_WEB = 'https://iupred2a.elte.hu/'
    IUPRED_CITATION = 'https://doi.org/10.1093/nar/gky384'
    CONSURF_WEB = 'https://consurf.tau.ac.il/'
    CONSURF_CITATION = 'https://doi.org/10.1093/nar/gkw408'
    GDPR_WEBSITE = 'https://gdpr-info.eu'
    DOCKER_HUB = 'https://hub.docker.com/r/filosanrod/conplot'
    CONPLOT_DOCKER = 'https://github.com/rigdenlab/conplot-docker'
    CONPLOT_MAIL = 'conplot.noreply@gmail.com'
    CONPLOT_USERNAME = 'conplot.noreply'
    CITATION = 'https://doi.org/10.1093/bioinformatics/btab049'
    YOUTUBE_EMBED = 'https://www.youtube.com/embed/dQw4w9WgXcQ'
    YOUTUBE_LINK = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'


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


def get_display_control_card(*args, **kwargs):
    from utils.plot_utils import get_display_control_card

    return get_display_control_card(*args, **kwargs)


def is_redis_available(*args, **kwargs):
    from utils.cache_utils import is_redis_available

    return is_redis_available(*args, **kwargs)


def get_active_sessions(*args, **kwargs):
    from utils.cache_utils import get_active_sessions

    return get_active_sessions(*args, **kwargs)


def lookup_data(*args, **kwargs):
    from utils.data_utils import lookup_data

    return lookup_data(*args, **kwargs)


def create_cmap_sets(*args, **kwargs):
    from utils.cmap_utils import create_cmap_sets

    return create_cmap_sets(*args, **kwargs)


def slice_cmap(*args, **kwargs):
    from utils.cmap_utils import slice_cmap

    return slice_cmap(*args, **kwargs)


def load_figure_json(*args, **kwargs):
    from utils.plot_utils import load_figure_json

    return load_figure_json(*args, **kwargs)


def load_display_settings(*args, **kwargs):
    from utils.plot_utils import load_display_settings

    return load_display_settings(*args, **kwargs)


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


def create_cmap_trace(*args, **kwargs):
    from utils.cmap_utils import create_cmap_trace

    return create_cmap_trace(*args, **kwargs)


def get_session_action(*args, **kwargs):
    from utils.callback_utils import get_session_action

    return get_session_action(*args, **kwargs)


def get_unique_contacts(elements):
    # Credits to: https://stackoverflow.com/questions/31499259/making-a-sequence-of-tuples-unique-by-a-specific-element
    key = itemgetter(0)
    unique = list({key(el): el for el in elements}.values())
    output = [(*contact[0], contact[1]) for contact in unique]
    output = sorted(output, key=itemgetter(2), reverse=True)
    return output


def get_unique_distances(elements):
    key = itemgetter(0)
    unique_contacts = list({key(el): el for el in elements}.values())
    output = [(*contact[0], *contact[1:]) for contact in unique_contacts]
    output = sorted(output, key=itemgetter(2), reverse=True)
    output.append('DISTO')
    return output
