import dash_html_components as html
import dash_bootstrap_components as dbc


def PlotPlaceHolder():
    return dbc.Jumbotron(
        [
            dbc.Container(
                [
                    html.Img(
                        src='/conkit-web/home/assets/conkit_small_logo.png',
                        style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}
                    )
                ],
                fluid=True,
            )
        ],
        fluid=True,
    )

    """
    return html.Div([
        html.Img(
            src='https://raw.githubusercontent.com/rigdenlab/conkit-web/master/assets/conkit_small_logo.png',
            style={'margin': 'auto', 'vertical-align': 'middle'}
        )
    ], style={'display': 'flex', 'justify-content': 'center'}
    )
    """
