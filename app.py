import dash
import dash_bootstrap_components as dbc
from index import PathIndex
from flask_caching import Cache

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX, FONT_AWESOME], url_base_pathname=PathIndex.HOME.value)
app.title = 'Conkit-Web'
server = app.server
app.config.suppress_callback_exceptions = True

# TODO: Eventually we want to move this to REDIS (safer, and it works on Heroku). Alernative: dcc.Storage
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory',

    # should be equal to maximum number of users on the app at a single time
    # higher numbers will store more data in the filesystem / redis cache
    'CACHE_THRESHOLD': 2
})
