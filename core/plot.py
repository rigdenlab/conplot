import pandas as pd
import plotly.graph_objects as go
import dash_core_components as dcc
import plotly.express as px

aa_properties = {'A': 'Non-polar, aliphatic',
                 'R': 'Positively charged (basic; non-acidic); Polar; Hydrophilic; pK=12.5',
                 'N': 'Polar, non-charged',
                 'D': 'Negatively charged (acidic); Polar; Hydrophilic; pK=3.9',
                 'C': 'Polar, non-charged',
                 'E': 'Negatively charged (acidic); Polar; Hydrophilic; pK=4.2',
                 'Q': 'Polar, non-charged',
                 'G': 'Non-polar, aliphatic',
                 'H': 'Positively charged (basic; non-acidic); Polar; Hydrophilic; pK=6.0',
                 'I': 'Non-polar, aliphatic',
                 'L': 'Non-polar, aliphatic',
                 'K': 'Positively charged (basic; non-acidic); Polar; Hydrophilic; pK=10.5',
                 'M': 'Polar, non-charged',
                 'F': 'Aromatic',
                 'P': 'Non-polar, aliphatic',
                 'S': 'Polar, non-charged',
                 'T': 'Polar, non-charged',
                 'W': 'Aromatic',
                 'Y': 'Aromatic',
                 'V': 'Aromatic'
                 }

spectrum = {1: '#f7fbff',
            2: '#deebf7',
            3: '#c6dbef',
            4: '#9ecae1',
            5: '#6baed6',
            6: '#4292c6',
            7: '#2171b5',
            8: '#08519c',
            9: '#08306b'
            }


def MakePlot(cmap, factor=2):
    cmap.remove_neighbors(inplace=True)
    cmap.sort('raw_score', reverse=True, inplace=True)

    df = pd.DataFrame(cmap.as_list())
    x_coords = df[0].tolist()[:cmap.sequence.seq_len * factor]
    y_coords = df[1].tolist()[:cmap.sequence.seq_len * factor]
    labels = [(x, y) for x, y in zip(x_coords, y_coords)]

    fig = go.Figure(
        data=go.Scatter(
            x=x_coords,
            y=y_coords,
            text=labels,
            mode='markers',
            marker={
                'symbol': 'circle-dot',
                'size': 5,
                'line': {'width': 0.1, 'color': 'black'}
            }
        ),
        layout=dict(
            xaxis={'title': 'Residue 1'},
            yaxis={'title': 'Residue 2'},
            autosize=True,
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            hovermode='closest',
            showlegend=False,
        )
    )

    return dcc.Graph(id='plot-graph', style={'height': '80vh'}, figure=fig)
