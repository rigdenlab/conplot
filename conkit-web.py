import dash_core_components as dcc
import dash_html_components as html
from app import app, server, cache
from utils import initiate_session
from callbacks import main_callbacks
from index import PathIndex

def serve_layout():
    session_id = initiate_session()

    return html.Div([
        html.Div(session_id, id='session-id', style={'display': 'none'}),
        dcc.Location(id='url', refresh=False),
        html.Div(PathIndex.DATAUPLOAD.value, id='plot-hidden-div', style={'display': 'none'}),
        html.Div(id='page-content'),
    ])


# serve_layout, not serve_layout()
app.layout = serve_layout
#app.config.suppress_callback_exceptions = True

# TODO: Clear cache after the app is closed!
if __name__ == '__main__':
    app.run_server(debug=True)
