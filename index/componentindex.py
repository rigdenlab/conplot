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


class InputReference(Enum):
    UPLOAD_CMAP_FNAME = 0
    CMAP_TEXT_VALUE = 1
    CMAP_FORMAT_SELECT = 2
    CMAP_FILE_ALERT_OPEN = 3
    UPLOAD_FASTA_FNAME = 4
    FASTA_TEXT_VALUE = 5
    FASTA_FILE_ALERT_OPEN = 6
    UPLOAD_MEM_FNAME = 7
    MEM_TEXT_VALUE = 8
    MEM_FILE_ALERT_OPEN = 9
    UPLOAD_CMAP_FCONTENTS = 10
    UPLOAD_FASTA_FCONTENTS = 11
    UPLOAD_MEM_FCONTENTS = 12
    SESSION_ID = 13


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
    UPLOAD_FASTA_FCONTENTS = 19
    UPLOAD_MEM_FCONTENTS = 20
    SESSION_ID = 21


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
        Output('upload-mem', 'contents')
    ]
    INPUT = [
        Input('upload-contact-map', 'filename'),
        Input("contact-map-text-area", "value"),
        Input("contact-format-select", "value"),
        Input("contact-map-filename-alert", "is_open"),
        Input('upload-fasta', 'filename'),
        Input("fasta-text-area", "value"),
        Input("fasta-filename-alert", "is_open"),
        Input('upload-mem', 'filename'),
        Input("mem-text-area", "value"),
        Input("mem-filename-alert", "is_open")
    ]

    STATE = [
        State('upload-contact-map', 'contents'),
        State('upload-fasta', 'contents'),
        State('upload-mem', 'contents'),
        State('session-id', 'children')
    ]
