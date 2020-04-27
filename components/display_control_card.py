import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from index import DatasetReference

def DisplayControlCard():
    return dbc.Card(
        dbc.CardBody(
            [
                dbc.Spinner(
                    html.Div([
                        html.P("Change the different data tracks", className="card-text"),
                        html.Br(),
                        dbc.Card([
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("L /", addon_type="prepend"),
                                    dbc.Input(id='L-cutoff-input', type="number", min=1, max=10, step=1,
                                              placeholder='2'),
                                ],
                            ),
                        ], outline=False),
                        html.Br(),
                        dcc.Dropdown(
                            options=[
                                {'label': 'Membrane Topology', 'value': DatasetReference.MEMBRANE_TOPOLOGY.value},
                                {'label': 'Disorder', 'value': DatasetReference.SEQUENCE.value},
                                {'label': 'Consercation', 'value': DatasetReference.CONTACT_MAP.value},
                            ],
                            value=[DatasetReference.MEMBRANE_TOPOLOGY.value],
                            multi=True
                        ),
                        html.Br(),
                        dbc.Button('Refresh', id='refresh-button', outline=True, color='primary', block=True)
                    ])
                )
            ]
        )
    )