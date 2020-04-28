from enum import Enum


class DatasetReference(Enum):
    SEQUENCE = 'sequence'
    CONTACT_MAP = 'contact'
    MEMBRANE_TOPOLOGY = 'membrtopo'
    SECONDARY_STRUCTURE = 'secondarystructure'
    CONSERVATION = 'conservation'
    DISORDER = 'disorder'


class ContextReference(Enum):
    CONTACT_HEAD_CLICK = 'contact-map-upload-head.n_clicks'
    DISPLAY_HEAD_CLICK = 'display-control-head.n_clicks'
    SS_HEAD_CLICK = 'ss-upload-head.n_clicks'
    DISORDER_HEAD_CLICK = 'disorder-upload-head.n_clicks'
    CONSERV_HEAD_CLICK = 'conserv-upload-head.n_clicks'
    MEM_HEAD_CLICK = 'mem-upload-head.n_clicks'
    SEQUENCE_HEAD_CLICK = 'sequence-upload-head.n_clicks'
    UPLOAD_CMAP_FNAME = 'upload-contact-map.filename'
    CMAP_TEXT_VALUE = "contact-map-text-area.value"
    CMAP_FORMAT_SELECT = "contact-format-select.value"
    UPLOAD_FASTA_FNAME = 'upload-fasta.filename'
    FASTA_TEXT_VALUE = "fasta-text-area.value"
    UPLOAD_MEM_FNAME = 'upload-mem.filename'
    MEM_TEXT_VALUE = "mem-text-area.value"
    PLOT_CLICK = 'plot-button.n_clicks'
    CMAP_ALERT_OPEN = 'contact-map-filename-alert.is_open'
    FASTA_ALERT_OPEN = 'fasta-filename-alert.is_open'
    MEM_ALERT_OPEN = 'mem-filename-alert.is_open'
