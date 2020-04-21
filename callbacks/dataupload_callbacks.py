from dash.dependencies import Input, Output, State
from app import app, cache


@app.callback([Output("contact-map-text-area", "valid"),
               Output("contact-map-text-area", "invalid"),
               Output("contact-map-invalid-collapse", "is_open"),
               Output("contact-map-filename-alert", "is_open"),
               Output('contact-map-filename-alert', 'children'),
               Output("format-selection-card", "color")],
              [Input('upload-contact-map', 'filename'),
               Input("contact-map-text-area", "value"),
               Input("contact-format-select", "value")],
              [State('upload-contact-map', 'contents'),
               State('session-id', 'children')])
def upload_contact_map(filename, cmap_text, cmap_format, file_contents, session_id):
    session = cache.get('session-{}'.format(session_id))

    if session is None:
        return False, False, False, False, False, 'danger'

    session.contact_loader.register_input(cmap_format, cmap_text, file_contents, filename)
    session.contact_loader.load()
    cache.set('session-{}'.format(session_id), session)
    return session.contact_loader.layout_states


@app.callback(Output('upload-contact-map', 'contents'),
              [Input("contact-map-filename-alert", "is_open")],
              [State('upload-contact-map', 'contents'),
               State('session-id', 'children')])
def remove_cmap_file(is_open, file_contents, session_id):
    session = cache.get('session-{}'.format(session_id))

    if session is not None and not is_open and session.contact_loader.valid and session.contact_loader.valid_file:
        session.contact_loader.clear()
        cache.set('session-{}'.format(session_id), session)
        return None
    else:
        return file_contents


@app.callback([Output("fasta-text-area", "valid"),
               Output("fasta-text-area", "invalid"),
               Output("fasta-invalid-collapse", "is_open"),
               Output("fasta-filename-alert", "is_open"),
               Output('fasta-filename-alert', 'children')],
              [Input('upload-fasta', 'filename'),
               Input("fasta-text-area", "value")],
              [State('upload-fasta', 'contents'),
               State('session-id', 'children')])
def upload_sequence(filename, fasta_text, file_contents, session_id):
    session = cache.get('session-{}'.format(session_id))

    if session is None:
        return False, False, False, False, False

    session.sequence_loader.register_input(fasta_text, file_contents, filename)
    session.sequence_loader.load()
    cache.set('session-{}'.format(session_id), session)
    return session.sequence_loader.layout_states


@app.callback(Output('upload-fasta', 'contents'),
              [Input("fasta-filename-alert", "is_open")],
              [State('upload-fasta', 'contents'),
               State('session-id', 'children')])
def remove_fasta_file(is_open, file_contents, session_id):
    session = cache.get('session-{}'.format(session_id))

    if session is not None and not is_open and session.sequence_loader.valid and session.sequence_loader.valid_file:
        session.sequence_loader.clear()
        cache.set('session-{}'.format(session_id), session)
        return None
    else:
        return file_contents
