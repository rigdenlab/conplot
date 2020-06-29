import dash_bootstrap_components as dbc
import dash_html_components as html
from utils import UrlIndex


def StartNewSessionLink():
    return html.A(dbc.Button("Start new session", block=True, color='danger'), href=UrlIndex.ROOT.value,
                  style={"text-decoration": "none"})


def GitHubLink():
    return dbc.Row(
        [
            dbc.Col(html.A(html.Img(src=UrlIndex.GITHUB_LOGO.value, height="30px"), href=UrlIndex.GITHUB.value)),
        ],
        no_gutters=True,
        className="ml-auto flex-nowrap mt-3 mt-md-0",
        align="center"
    )


def ConPlotLink():
    return html.A(
        dbc.Row(
            [
                dbc.Col(html.Img(src=UrlIndex.CONPLOT_LOGO.value, height="40px")),
                dbc.Col(dbc.NavbarBrand(html.H1('ConPlot')), className="mt-2 ml-2"),
            ],
            align="center",
            no_gutters=True,
        ),
        href=UrlIndex.HOME.value,
    )
