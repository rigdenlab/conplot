from enum import Enum


class DatasetReference(Enum):
    SEQUENCE = 'sequence'
    CONTACT_MAP = 'contact'
    MEMBRANE_TOPOLOGY = 'membranetopology'
    SECONDARY_STRUCTURE = 'secondarystructure'
    CONSERVATION = 'conservation'
    DISORDER = 'disorder'


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
