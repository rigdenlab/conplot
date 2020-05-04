import dash_bootstrap_components as dbc
import dash_html_components as html
from utils import PathIndex


def github_link():
    return dbc.Row(
        [
            dbc.Col(html.A(html.Img(src=PathIndex.GITHUB_LOGO.value, height="30px"), href=PathIndex.GITHUB.value)),
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
                        dbc.Col(html.Img(src=PathIndex.CONKIT_LOGO.value, height="40px")),
                        dbc.Col(dbc.NavbarBrand('Conkit-Web', className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href=PathIndex.HOME.value,
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(github_link(), id="navbar-collapse", navbar=True),
        ],
    )
