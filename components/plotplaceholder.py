import dash_html_components as html


def PlotPlaceHolder():
    return html.Div([
        html.Img(
            src='https://raw.githubusercontent.com/rigdenlab/conkit-web/master/assets/conkit_small_logo.png',
            style={'margin': 'auto', 'vertical-align': 'middle'}
        )
    ], style={'display': 'flex', 'justify-content': 'center'})
