from dash.dependencies import Input, Output, State
from app import app, cache
from layouts import noPage, Home, DataUpload, Contact
from components import PathIndex


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname'),
               Input('plot-hidden-div', 'children')],
              [State('session-id', 'children')])
def display_page(url, url_plot, session_id):
    if url == PathIndex.HOME.value or url == PathIndex.ROOT.value:
        return Home(session_id)
    elif url == PathIndex.CONTACT.value:
        return Contact(session_id)
    elif url == PathIndex.PLOT.value:
        return DataUpload(session_id)
    else:
        return noPage()
