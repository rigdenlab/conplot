import dash_bootstrap_components as dbc
import dash_html_components as html


def HelpBadge():
    return dbc.Badge([
        html.I(className="fas fa-question-circle"),
    ], color="light", className="mr-1")


def ExampleLinkButton(url):
    return dbc.Button('Example', size='sm', outline=True, color='primary',
                      id={'index': 'load-example', 'type': 'javascript-exe-button'})
