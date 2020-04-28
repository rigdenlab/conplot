import plotly.graph_objects as go
from werkzeug.utils import cached_property
from enum import Enum
from index import DatasetReference, MembraneStates


class MembraneTopologyColor(Enum):
    INSIDE = 'green'
    OUTSIDE = 'yellow'
    INSERTED = 'red'


class SecondaryStructureColor(Enum):
    HELIX = 'orange'
    COIL = 'blue'
    SHEET = 'pink'


class Plot(object):

    def __init__(self, session, factor=2, remove_neighbors=True):
        self.session = session
        self.factor = factor
        self.remove_neighbors = remove_neighbors
        self.cmap = session.contact_loader.cmap
        self.mem_pred = session.membranetopology_loader.prediction
        self.ss_pred = session.secondarystructure_loader.prediction
        self.conserv_pred = session.conservation_loader.prediction
        self.disorder_pred = session.disorder_loader.prediction

        self.active_tracks = []
        for track in self.session:
            if track.datatype == DatasetReference.SEQUENCE or track.datatype == DatasetReference.CONTACT_MAP:
                pass
            elif track.prediction is not None:
                self.active_tracks.append(track.datatype.name)

    @cached_property
    def axis_range(self):
        # TODO: NEED TO THINK AGAIN ABOUT NUMBERING
        return (1, self.cmap.sequence.seq_len + 1)

    @cached_property
    def aa_properties(self):
        return {
            'A': 'Non-polar, aliphatic',
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

    @cached_property
    def spectrum(self):
        return {
            1: '#f7fbff',
            2: '#deebf7',
            3: '#c6dbef',
            4: '#9ecae1',
            5: '#6baed6',
            6: '#4292c6',
            7: '#2171b5',
            8: '#08519c',
            9: '#08306b'
        }

    @property
    def contact_trace(self):

        if self.remove_neighbors:
            cmap = self.cmap.remove_neighbors(inplace=False)
            cmap.sort('raw_score', reverse=True, inplace=True)

        else:
            cmap = self.cmap.sort('raw_score', reverse=True, inplace=False)

        contacts = cmap.as_list()[:cmap.sequence.seq_len * self.factor]

        res1_list = [contact[0] for contact in contacts]
        res2_list = [contact[1] for contact in contacts]

        return go.Scatter(
            x=res1_list + res2_list,
            y=res2_list + res1_list,
            hoverinfo='none',
            mode='markers',
            marker={
                'symbol': 'circle',
                'size': 5,
                'color': 'black'
            }
        )

    def get_membrane_trace(self, topology):

        if self.mem_pred is None:
            return None

        res_idx = [idx + 1 for idx, residue in enumerate(self.mem_pred) if residue == topology]
        residue_names = ['Residue: {} ({}) | {}'.format(self.cmap.sequence.seq[idx - 1], idx, topology.name)
                         for idx in res_idx]

        return go.Scatter(
            x=res_idx,
            y=res_idx,
            hovertext=residue_names,
            hoverinfo='text',
            mode='markers',
            marker={
                'symbol': 'circle',
                'size': 5,
                'color': MembraneTopologyColor.__getattr__(topology.name).value
            }
        )

    def get_figure(self):

        figure = go.Figure(
            layout=go.Layout(
                xaxis={'title': 'Residue 1', 'range': self.axis_range},
                yaxis={'title': 'Residue 2', 'range': self.axis_range},
                autosize=True,
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                hovermode='closest',
                showlegend=False,
                plot_bgcolor='rgba(0,0,0,0)'

            )
        )

        figure.add_trace(self.contact_trace)
        if self.mem_pred is not None and DatasetReference.MEMBRANE_TOPOLOGY.name in self.active_tracks:
            figure.add_trace(self.get_membrane_trace(MembraneStates.INSIDE))
            figure.add_trace(self.get_membrane_trace(MembraneStates.OUTSIDE))
            figure.add_trace(self.get_membrane_trace(MembraneStates.INSERTED))

        return figure
