import dash_bootstrap_components as dbc
import dash_html_components as html
from .pathindex import PathIndex

GITHUB_LOGO = 'assets/github_logo.png'
CONKIT_LOGO = 'assets/conkit_small_logo.png'


def github_link():
    return dbc.Row(
        [
            dbc.Col(html.A(html.Img(src=GITHUB_LOGO, height="30px"), href=PathIndex.GITHUB.value)),
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
                        dbc.Col(html.Img(src=CONKIT_LOGO, height="40px")),
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
