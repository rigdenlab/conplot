import dash_bootstrap_components as dbc
import dash_html_components as html


def DisplayControlCard():
    return dbc.Card(
        dbc.CardBody(
            [
                dbc.Spinner(
                    html.Div([
                        html.H5("Display Controls", className="card-title"),
                        html.Br(),
                        dbc.Row([
                            dbc.Card([
                                dbc.InputGroup(
                                    [
                                        dbc.InputGroupAddon("L /", addon_type="prepend"),
                                        dbc.Input(id='L-cutoff-input', type="number", min=1, max=10, step=1,
                                                  placeholder='1'),
                                    ],
                                ),
                            ]),
                            dbc.Card([
                                dbc.Input(id='score-threshold-input', type="number", min=0.000, max=1.000, step=0.01,
                                          placeholder='Score threshold'),
                            ]),
                        ]),
                        html.Br(),
                        dbc.Row([
                            dbc.Col([
                                dbc.Checklist(
                                    options=[{"label": "Remove neighbours", "value": 1}, ],
                                    value=[],
                                    id="switches-inline-input",
                                    inline=True,
                                    switch=True,
                                ),

                            ])
                        ]),
                    ])
                )
            ]
        )
    )
