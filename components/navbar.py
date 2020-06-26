import dash_bootstrap_components as dbc
from utils import UrlIndex


def NavBar(pathname=None):
    return dbc.Nav([
        dbc.NavItem(dbc.NavLink("Home", active=(pathname == UrlIndex.HOME.value or pathname == UrlIndex.ROOT.value),
                                href=UrlIndex.HOME.value)),
        dbc.NavItem(dbc.NavLink("Plot", active=(pathname == UrlIndex.PLOT.value), href=UrlIndex.PLOT.value)),
        dbc.NavItem(dbc.NavLink("Get in touch", active=(pathname == UrlIndex.CONTACT.value), href=UrlIndex.CONTACT.value)),
        dbc.NavItem(dbc.NavLink("Help", active=(pathname == UrlIndex.HELP.value), href=UrlIndex.HELP.value)),
        dbc.NavItem(dbc.NavLink("Rigden Lab", active=(pathname == UrlIndex.RIGDEN.value), href=UrlIndex.RIGDEN.value)),
    ],
        pills=True, fill=True, justified=True
    )
