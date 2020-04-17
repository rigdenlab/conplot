import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app, server
from layouts import noPage, Home, UploadPlot, Contact
from components import PathIndex

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == PathIndex.HOME.value:
        return Home()
    elif pathname == PathIndex.PLOT.value:
        return UploadPlot()
    elif pathname == PathIndex.CONTACT.value:
        return Contact()
    else:
        return noPage()


if __name__ == '__main__':
    app.run_server(debug=True)
