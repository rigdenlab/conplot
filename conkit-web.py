import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app, server
from layouts import noPage, Home, DataUpload, Contact, DisplayPlot
from components import PathIndex
import uuid


def serve_layout():
    session_id = str(uuid.uuid4())

    return html.Div([
        html.Div(session_id, id='session-id', style={'display': 'none'}),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content'),
    ])


# serve_layout, not serve_layout()
app.layout = serve_layout


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')],
              [State('session-id', 'children')])
def display_page(pathname, session_id):
    if pathname == PathIndex.HOME.value:
        return Home(session_id)
    elif pathname == PathIndex.DATAUPLOAD.value:
        return DataUpload(session_id)
    elif pathname == PathIndex.PLOTDISPLAY.value:
        return DisplayPlot(session_id)
    elif pathname == PathIndex.CONTACT.value:
        return Contact(session_id)
    else:
        return noPage()


# TODO: Clear cache after the app is closed!
if __name__ == '__main__':
    app.run_server(debug=True)
