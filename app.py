import dash
import dash_bootstrap_components as dbc
from components import PathIndex
from flask_caching import Cache

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX], url_base_pathname=PathIndex.HOME.value)
app.title = 'Conkit-Web'
server = app.server
app.config.suppress_callback_exceptions = True
