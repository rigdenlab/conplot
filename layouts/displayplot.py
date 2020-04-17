from app import app, cache
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from components import Header, NavBar, PathIndex
import dash_html_components as html


def DisplayPlot(session_id):
    return html.Div([
        Header(),
        NavBar(PathIndex.PLOTDISPLAY.value),
        html.Div([
            Body(session_id)
        ]),
        html.Br(),
        dcc.Link([dbc.Button("Go back", id='go-back-button', color="primary", block=True)],
                 href=PathIndex.DATAUPLOAD.value),
    ])


def Body(session_id):
    df = cache.get('contacts-{}'.format(session_id))
    print(df)
    seq = cache.get('fasta-{}'.format(session_id))
    print(seq)
    print('Plotting! %s' % session_id)

    # TODO: Need to make this decent
    x_coords = df[0].tolist()[:100]
    y_coords = df[1].tolist()[:100]
    labels = [(x, y) for x, y in zip(x_coords, y_coords)]

    return dcc.Graph(
        figure={
            'data': [
                dict(
                    x=x_coords,
                    y=y_coords,
                    text=labels,
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.1, 'color': 'black'}
                    },
                    name=i
                ) for i in range(0, 100)
            ],
            'layout': dict(
                xaxis={'title': 'Residue 1'},
                yaxis={'title': 'Residue 2'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                hovermode='closest',
                showlegend=False,
            )
        }
    )
