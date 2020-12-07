import dash_html_components as html
import dash_bootstrap_components as dbc
from components import HelpBadge, ExampleLinkButton
import visdcc


def HelpToolTip(id, text, msg, example_url=None):
    children = [
        text,
        html.Span([
            HelpBadge()
        ], id='{}-tooltip'.format(id)),
        dbc.Tooltip(msg, target='{}-tooltip'.format(id))
    ]

    if example_url is not None:
        children.append(
            html.Span([
                ExampleLinkButton(example_url),
                visdcc.Run_js(id='refresh-page')
            ], id='{}-example-tooltip'.format(id))
        )
        children.append(dbc.Tooltip('Click here to get example data', target='{}-example-tooltip'.format(id)))

    return children
