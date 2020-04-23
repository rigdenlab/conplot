import plotly.graph_objects as go
import dash_core_components as dcc

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


def MakePlot(session, factor=2, remove_neighbors=True):
    if remove_neighbors:
        session.contact_loader.cmap.remove_neighbors(inplace=True)
    session.contact_loader.cmap.sort('raw_score', reverse=True, inplace=True)

    contacts = session.contact_loader.cmap.as_list()[:session.contact_loader.cmap.sequence.seq_len * factor]

    x_coords = [contact[0] for contact in contacts] + [contact[1] for contact in contacts]
    y_coords = [contact[1] for contact in contacts] + [contact[0] for contact in contacts]
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
                'color': 'black'
            }
        ),
        layout=go.Layout(
            xaxis={'title': 'Residue 1', 'range': [0, session.contact_loader.cmap.sequence.seq_len + 1]},
            yaxis={'title': 'Residue 2', 'range': [0, session.contact_loader.cmap.sequence.seq_len + 1]},
            autosize=True,
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            hovermode='closest',
            showlegend=False,
            plot_bgcolor='rgba(0,0,0,0)'

        )
    )

    return dcc.Graph(id='plot-graph', style={'height': '80vh'}, figure=fig)
