from dash.dependencies import Input, Output, State
from enum import Enum


class TableCollapseInterfaceIndex(Enum):
    OUTPUT = [
        Output('contact-map-upload-collapse', 'is_open'),
        Output('sequence-upload-collapse', 'is_open'),
        Output('mem-upload-collapse', 'is_open')
    ]
    INPUT = [
        Input('contact-map-upload-head', 'n_clicks'),
        Input('sequence-upload-head', 'n_clicks'),
        Input('mem-upload-head', 'n_clicks')
    ]
    STATE = [
        State('sequence-upload-collapse', 'is_open'),
        State('contact-map-upload-collapse', 'is_open'),
        State('mem-upload-collapse', 'is_open')
    ]


class ContextReference(Enum):
    CONTACT_HEAD_CLICK = 'contact-map-upload-head.n_clicks'
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


class InputReference(Enum):
    UPLOAD_CMAP_FNAME = 0
    CMAP_TEXT_VALUE = 1
    CMAP_FORMAT_SELECT = 2
    UPLOAD_FASTA_FNAME = 3
    FASTA_TEXT_VALUE = 4
    UPLOAD_MEM_FNAME = 5
    MEM_TEXT_VALUE = 6
    PLOT_CLICK = 7
    UPLOAD_CMAP_FCONTENTS = 8
    UPLOAD_FASTA_FCONTENTS = 9
    UPLOAD_MEM_FCONTENTS = 10
    SESSION_ID = 11


class OutputReference(Enum):
    CMAP_TEXT_VALID = 0
    CMAP_TEXT_INVALID = 1
    CMAP_INVALID_COLLAPSE_OPEN = 2
    CMAP_FNAME_ALERT_OPEN = 3
    CMAP_FNAME = 4
    CMAP_FORMAT_SELECT_COLOR = 5
    CMAP_HEAD_COLOR = 6
    FASTA_TEXT_VALID = 7
    FASTA_TEXT_INVALID = 8
    FASTA_INVALID_COLLAPSE_OPEN = 9
    FASTA_FNAME_ALERT_OPEN = 10
    FASTA_FNAME = 11
    SEQ_HEAD_COLOR = 12
    MEM_TEXT_VALID = 13
    MEM_TEXT_INVALID = 14
    MEM_INVALID_COLLAPSE_OPEN = 15
    MEM_FNAME_ALERT_OPEN = 16
    MEM_FNAME = 17
    MEM_HEAD_COLOR = 18
    UPLOAD_CMAP_FCONTENTS = 19
    UPLOAD_FASTA_FCONTENTS = 20
    UPLOAD_MEM_FCONTENTS = 21
    PLOT_DIV = 22
    MODAL_DIV = 23


class UploadInterfaceComponentIndex(Enum):
    OUTPUT = [
        Output("contact-map-text-area", "valid"),
        Output("contact-map-text-area", "invalid"),
        Output("contact-map-invalid-collapse", "is_open"),
        Output("contact-map-filename-alert", "is_open"),
        Output('contact-map-filename-alert', 'children'),
        Output("format-selection-card", "color"),
        Output('contact-map-upload-head', 'color'),
        Output("fasta-text-area", "valid"),
        Output("fasta-text-area", "invalid"),
        Output("fasta-invalid-collapse", "is_open"),
        Output("fasta-filename-alert", "is_open"),
        Output('fasta-filename-alert', 'children'),
        Output('sequence-upload-head', 'color'),
        Output("mem-text-area", "valid"),
        Output("mem-text-area", "invalid"),
        Output("mem-invalid-collapse", "is_open"),
        Output("mem-filename-alert", "is_open"),
        Output('mem-filename-alert', 'children'),
        Output('mem-upload-head', 'color'),
        Output('upload-contact-map', 'contents'),
        Output('upload-fasta', 'contents'),
        Output('upload-mem', 'contents'),
        Output('plot-div', 'children'),
        Output('modal-div', 'children')
    ]
    INPUT = [
        Input('upload-contact-map', 'filename'),
        Input("contact-map-text-area", "value"),
        Input("contact-format-select", "value"),
        Input('upload-fasta', 'filename'),
        Input("fasta-text-area", "value"),
        Input('upload-mem', 'filename'),
        Input("mem-text-area", "value"),
        Input('plot-button', 'n_clicks')
    ]

    STATE = [
        State('upload-contact-map', 'contents'),
        State('upload-fasta', 'contents'),
        State('upload-mem', 'contents'),
        State('session-id', 'children')
    ]
