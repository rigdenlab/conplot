import dash_bootstrap_components as dbc
import dash_html_components as html
from utils import UrlIndex


def StartNewSessionLink():
    return dbc.Button("Start new session", block=True, color='danger',
                      id={'type': 'javascript-exe-button', 'index': 'new-session'})


def GitHubLink():
    return dbc.Row(
        [
            dbc.Col(html.A(html.Img(src=UrlIndex.GITHUB_LOGO.value, height="30px"), href=UrlIndex.GITHUB.value)),
        ],
        no_gutters=True,
        className="ml-auto flex-nowrap mt-3 mt-md-0",
        align="center"
    )
