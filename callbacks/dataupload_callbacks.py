from dash.dependencies import Input, Output, State
from app import app, cache
from dash.dash import no_update
from dash import callback_context
from components import PlotPlaceHolder
from core import Plot
import dash_core_components as dcc


@app.callback([Output('contact-map-upload-collapse', 'is_open'),
               Output('sequence-upload-collapse', 'is_open'),
               Output('mem-upload-collapse', 'is_open')],
              [Input('contact-map-upload-head', 'n_clicks'),
               Input('sequence-upload-head', 'n_clicks'),
               Input('mem-upload-head', 'n_clicks')],
              [State('contact-map-upload-collapse', 'is_open'),
               State('sequence-upload-collapse', 'is_open'),
               State('mem-upload-collapse', 'is_open')])
def toggle(contact_click, sequence_click, mem_click, contact_open, sequence_open, mem_open):
    ctx = callback_context.triggered[0]

    if ctx['prop_id'] == '.':
        return False, False, False
    elif ctx['prop_id'] == 'contact-map-upload-head.n_clicks':
        return not contact_open, False, False
    elif ctx['prop_id'] == 'mem-upload-head.n_clicks':
        return False, False, not mem_open
    else:
        return False, not sequence_open, False


@app.callback([Output("contact-map-text-area", "valid"),
               Output("contact-map-text-area", "invalid"),
               Output("contact-map-invalid-collapse", "is_open"),
               Output("contact-map-filename-alert", "is_open"),
               Output('contact-map-filename-alert', 'children'),
               Output("format-selection-card", "color"),
               Output('contact-map-upload-head', 'color')],
              [Input('upload-contact-map', 'filename'),
               Input("contact-map-text-area", "value"),
               Input("contact-format-select", "value")],
              [State('upload-contact-map', 'contents'),
               State('session-id', 'children')])
def upload_contact_map(filename, cmap_text, cmap_format, file_contents, session_id):
    session = cache.get('session-{}'.format(session_id))

    if session is None:
        return False, False, False, False, False, 'danger', 'dark'

    session.contact_loader.register_input(cmap_text, file_contents, filename, cmap_format)
    session.contact_loader.load()
    cache.set('session-{}'.format(session_id), session)
    return session.contact_loader.layout_states


@app.callback([Output("fasta-text-area", "valid"),
               Output("fasta-text-area", "invalid"),
               Output("fasta-invalid-collapse", "is_open"),
               Output("fasta-filename-alert", "is_open"),
               Output('fasta-filename-alert', 'children'),
               Output('sequence-upload-head', 'color')],
              [Input('upload-fasta', 'filename'),
               Input("fasta-text-area", "value")],
              [State('upload-fasta', 'contents'),
               State('session-id', 'children')])
def upload_sequence(filename, fasta_text, file_contents, session_id):
    session = cache.get('session-{}'.format(session_id))

    if session is None:
        return False, False, False, False, False, 'dark'

    session.sequence_loader.register_input(fasta_text, file_contents, filename)
    session.sequence_loader.load()
    cache.set('session-{}'.format(session_id), session)
    return session.sequence_loader.layout_states


@app.callback([Output("mem-text-area", "valid"),
               Output("mem-text-area", "invalid"),
               Output("mem-invalid-collapse", "is_open"),
               Output("mem-filename-alert", "is_open"),
               Output('mem-filename-alert', 'children'),
               Output('mem-upload-head', 'color')],
              [Input('upload-mem', 'filename'),
               Input("mem-text-area", "value")],
              [State('upload-mem', 'contents'),
               State('session-id', 'children')])
def upload_membranetopology(filename, mem_text, file_contents, session_id):
    session = cache.get('session-{}'.format(session_id))

    if session is None:
        return False, False, False, False, False, 'dark'

    session.membrtopo_loader.register_input(mem_text, file_contents, filename, input_format='TOPCONS')
    session.membrtopo_loader.load()
    cache.set('session-{}'.format(session_id), session)
    return session.membrtopo_loader.layout_states


@app.callback([Output('plot-div', 'children'),
               Output('modal-div', 'children')],
              [Input('plot-button', 'n_clicks')],
              [State('session-id', 'children')])
def create_plot(n_clicks, session_id):
    session = cache.get('session-{}'.format(session_id))
    ctx = callback_context

    if session is None or ctx.triggered[0]['value'] is None:
        return no_update, None

    error = session.lookup_input_errors()
    if error is not None:
        return PlotPlaceHolder(), error
    else:
        plot = Plot(cmap=session.contact_loader.cmap, mem_pred=session.membrtopo_loader.prediction)
        return dcc.Graph(id='plot-graph', style={'height': '80vh'}, figure=plot.get_figure()), None


@app.callback([Output('upload-contact-map', 'contents'),
               Output('upload-fasta', 'contents'),
               Output('upload-mem', 'contents')],
              [Input("contact-map-filename-alert", "is_open"),
               Input("fasta-filename-alert", "is_open"),
               Input("mem-filename-alert", "is_open")],
              [State('upload-contact-map', 'contents'),
               State('upload-fasta', 'contents'),
               State('upload-mem', 'contents'),
               State('session-id', 'children')])
def remove_file(contact_fname_open, fasta_fname_open, mem_fname_open, contact_fcontents, fasta_fcontents, mem_fcontents,
                session_id):
    session = cache.get('session-{}'.format(session_id))

    if session is None:
        return no_update, no_update, no_update

    ctx = callback_context.triggered[0]

    if ctx['prop_id'] == 'contact-map-filename-alert.is_open' and session.contact_loader.valid_file \
            and contact_fcontents is not None and not contact_fname_open:
        session.contact_loader.clear()
        cache.set('session-{}'.format(session_id), session)
        return None, no_update, no_update

    elif ctx['prop_id'] == 'fasta-filename-alert.is_open' and session.sequence_loader.valid_file \
            and fasta_fcontents is not None and not fasta_fname_open:
        session.sequence_loader.clear()
        cache.set('session-{}'.format(session_id), session)
        return no_update, None, no_update

    elif ctx['prop_id'] == 'mem-filename-alert.is_open' and session.membrtopo_loader.valid_file \
            and mem_fcontents is not None and not mem_fname_open:
        session.membrtopo_loader.clear()
        cache.set('session-{}'.format(session_id), session)
        return no_update, no_update, None

    else:
        return no_update, no_update, no_update
