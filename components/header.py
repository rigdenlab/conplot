import dash_bootstrap_components as dbc
import dash_html_components as html
from utils import UrlIndex


def github_link():
    return dbc.Row(
        [
            dbc.Col(html.A(html.Img(src=UrlIndex.GITHUB_LOGO.value, height="30px"), href=UrlIndex.GITHUB.value)),
        ],
        no_gutters=True,
        className="ml-auto flex-nowrap mt-3 mt-md-0",
        align="center",
    )


def Header():
    return dbc.Navbar(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=UrlIndex.CONPLOT_LOGO.value, height="40px")),
                        dbc.Col(dbc.NavbarBrand('ConPlot', className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href=UrlIndex.HOME.value,
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(github_link(), id="navbar-collapse", navbar=True),
        ],
    )
