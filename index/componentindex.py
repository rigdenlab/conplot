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
        State('contact-map-upload-collapse', 'is_open'),
        State('sequence-upload-collapse', 'is_open'),
        State('mem-upload-collapse', 'is_open')
    ]


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
        Input('upload-fasta', 'filename'),
        Input("fasta-text-area", "value"),
        Input("contact-map-filename-alert", "is_open"),
        Input("fasta-filename-alert", "is_open"),
        Input("mem-filename-alert", "is_open"),
        Input('upload-mem', 'filename'),
        Input("mem-text-area", "value")
    ]

    STATE = [
        State('upload-contact-map', 'contents'),
        State('upload-fasta', 'contents'),
        State('upload-mem', 'contents'),
        State('session-id', 'children')
    ]
