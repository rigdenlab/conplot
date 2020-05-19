from enum import Enum


class ContextReference(Enum):
    CONTACT_HEAD_CLICK = 'contact-map-upload-head.n_clicks'
    DISPLAY_HEAD_CLICK = 'display-control-head.n_clicks'
    HELP_HEAD_CLICK = 'help-head.n_clicks'
    WARNING_HEAD_CLICK = 'warning-head.n_clicks'
    SS_HEAD_CLICK = 'secondarystructure-upload-head.n_clicks'
    DISORDER_HEAD_CLICK = 'disorder-upload-head.n_clicks'
    CONSERV_HEAD_CLICK = 'conservation-upload-head.n_clicks'
    MEM_HEAD_CLICK = 'membranetopology-upload-head.n_clicks'
    SEQUENCE_HEAD_CLICK = 'sequence-upload-head.n_clicks'
    UPLOAD_CMAP_FNAME = 'upload-contact-map.filename'
    CMAP_TEXT_VALUE = "contact-map-text-area.value"
    CMAP_FORMAT_SELECT = "contact-format-select.value"
    UPLOAD_SEQUENCE_FNAME = 'upload-sequence.filename'
    SEQUENCE_TEXT_VALUE = "sequence-text-area.value"
    UPLOAD_MEM_FNAME = 'upload-membranetopology.filename'
    MEM_TEXT_VALUE = "membranetopology-text-area.value"
    PLOT_CLICK = 'plot-button.n_clicks'
    CMAP_ALERT_OPEN = 'contact-map-filename-alert.is_open'
    SEQUENCE_ALERT_OPEN = 'sequence-filename-alert.is_open'
    MEM_ALERT_OPEN = 'membranetopology-filename-alert.is_open'


def noPage(*args, **kwargs):
    from layouts.nopage import noPage

    return noPage(*args, **kwargs)


def Home(*args, **kwargs):
    from layouts.home import Home

    return Home(*args, **kwargs)


def UsersPortal(*args, **kwargs):
    from layouts.userportal import UsersPortal

    return UsersPortal(*args, **kwargs)


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
