from dash.dependencies import Input, Output, State
from app import app, cache
from layouts import noPage, Home, DataUpload, Contact, DisplayPlot
from components import PathIndex


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')],
              [State('session-id', 'children')])
def display_page(pathname, session_id):
    if pathname == PathIndex.HOME.value or pathname == PathIndex.ROOT.value:
        return Home(session_id)
    elif pathname == PathIndex.DATAUPLOAD.value:
        return DataUpload(session_id)
    elif pathname == PathIndex.PLOTDISPLAY.value:
        return DisplayPlot(session_id)
    elif pathname == PathIndex.CONTACT.value:
        return Contact(session_id)
    else:
        return noPage()
