import dash_bootstrap_components as dbc
from .pathindex import PathIndex


def NavBar(pathname=None):
    return dbc.Nav([
        dbc.NavItem(dbc.NavLink("About", active=(pathname == PathIndex.HOME.value or pathname == PathIndex.ROOT.value),
                                href=PathIndex.HOME.value)),
        dbc.NavItem(dbc.NavLink("Plot", href=PathIndex.PLOT.value, active=(PathIndex.PLOT.value == pathname))),
        dbc.NavItem(dbc.NavLink("Contact", active=(pathname == PathIndex.CONTACT.value), href=PathIndex.CONTACT.value)),
    ],
        pills=True, fill=True, justified=True
    )
