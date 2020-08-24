import dash_html_components as html
import dash_core_components as dcc


def Base(session_id):
    return html.Div([
        dcc.Store(id='session-id', data=session_id, storage_type='session'),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content'),
    ])
