import dash_bootstrap_components as dbc
import dash_html_components as html


def HelpBadge():
    return dbc.Badge([
        html.I(className="fas fa-question-circle"),
    ], color="light", className="mr-1")


def ExampleLinkBadge(url):
    return dbc.Badge([
        html.I(className="fas fa-download"),
    ], color="light", className="mr-1", href=url)
