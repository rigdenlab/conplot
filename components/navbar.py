import dash_bootstrap_components as dbc
from utils import PathIndex


def NavBar(pathname=None):
    return dbc.Nav([
        dbc.NavItem(dbc.NavLink("Home", active=(pathname == PathIndex.HOME.value or pathname == PathIndex.ROOT.value),
                                href=PathIndex.HOME.value)),
        dbc.NavItem(dbc.NavLink("Plot", active=(pathname == PathIndex.PLOT.value), href=PathIndex.PLOT.value)),
        dbc.NavItem(dbc.NavLink("Contact", active=(pathname == PathIndex.CONTACT.value), href=PathIndex.CONTACT.value)),
        dbc.NavItem(dbc.NavLink("Help", active=(pathname == PathIndex.HELP.value), href=PathIndex.HELP.value)),
        dbc.NavItem(dbc.NavLink("Rigden Lab", active=(pathname == PathIndex.RIGDEN.value), href=PathIndex.RIGDEN.value)),
    ],
        pills=True, fill=True, justified=True
    )
