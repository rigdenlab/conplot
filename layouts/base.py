import dash_html_components as html
import dash_core_components as dcc


def Base(session_id):
    return html.Div([
        html.Div(session_id, id='session-id', style={'display': 'none'}),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content'),
    ])
