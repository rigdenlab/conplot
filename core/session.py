from .contactloader import ContactLoader
from .sequenceloader import SequenceLoader
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objects as go


class Session(object):
    """Class with methods and data structures to store all the information related with a given session"""

    def __init__(self, id):
        self.id = id
        self.contact_loader = ContactLoader()
        self.sequence_loader = SequenceLoader()

    def __iter__(self):
        for loader in (self.contact_loader, self.sequence_loader):
            yield loader

    @property
    def missing_data(self):
        return [loader for loader in self if not loader.valid]

    def create_plot(self):
        df = pd.DataFrame(self.contact_loader.cmap.as_list())
        x_coords = df[0].tolist()[:100]
        y_coords = df[1].tolist()[:100]
        labels = [(x, y) for x, y in zip(x_coords, y_coords)]

        fig = go.Figure(
            data=[
                dict(
                    x=x_coords,
                    y=y_coords,
                    text=labels,
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 4,
                        'line': {'width': 0.1, 'color': 'black'}
                    },
                    name=i
                ) for i in range(0, 100)
            ],
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
