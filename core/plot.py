import plotly.graph_objects as go
from werkzeug.utils import cached_property
from enum import Enum
from index import DatasetReference, MembraneStates, SecondaryStructureStates, DisorderStates, ConservationStates


class MembraneTopologyColor(Enum):
    INSIDE = 'green'
    OUTSIDE = 'yellow'
    INSERTED = 'red'


class DisorderColor(Enum):
    DISORDER = 'rgba(120,0,0,0.2)'
    ORDER = 'rgba(0,120,0,0.2)'


class ConservationColor(Enum):
    CONSERVED = 'rgba(0, 30, 255,0.2)'
    AVERAGE = 'rgba(0, 130, 255,0.2)'
    VARIABLE = 'rgba(0, 225, 255,0.2)'


class SecondaryStructureColor(Enum):
    HELIX = 'rgba(135, 16, 232, 0.2)'
    COIL = 'rgba(255, 136, 0,0.2)'
    SHEET = 'rgba(232, 16, 149,0.2)'


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
        return (0, self.cmap.sequence.seq_len + 1)

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

        contacts = cmap.as_list()[:int(round(cmap.sequence.seq_len / self.factor, 0))]

        res1_list = [contact[0] for contact in contacts]
        res2_list = [contact[1] for contact in contacts]

        return go.Scatter(
            x=res1_list + res2_list,
            y=res2_list + res1_list,
            hoverinfo='text',
            hovertext=['Contact: %s - %s | Confidence: %s' % (contact.res1_seq, contact.res2_seq, contact.raw_score) for
                       contact in cmap],
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

        x = [idx for idx in range(1, len(self.mem_pred) + 1)]
        y = [idx if residue == topology else None for idx, residue in enumerate(self.mem_pred, 1)]

        residue_names = ['Residue: {} ({}) | {}'.format(self.cmap.sequence.seq[idx - 1], idx, topology.name)
                         for idx in x]

        return go.Scatter(
            x=x,
            y=y,
            hovertext=residue_names,
            hoverinfo='text',
            mode="markers",
            marker={
                'symbol': 'diamond',
                'size': 7,
                'color': MembraneTopologyColor.__getattr__(topology.name).value,
            },
        )

    @staticmethod
    def transform_coords_diagonal_axis(coord, distance, lower_bound=False, ratio=1, y_axis=True):

        if coord is None:
            return None

        if y_axis:
            factor = ratio * (distance / (1 + ratio ** 2))
            if lower_bound:
                factor = factor * -1
        else:
            factor = distance / (1 + ratio ** 2)
            if not lower_bound:
                factor = factor * -1

        return coord + factor

    @property
    def ss_traces(self):

        traces = []

        if self.ss_pred is not None:
            x_diagonal = [idx for idx in range(1, len(self.ss_pred) + 1)]

            for ss_element in SecondaryStructureStates:
                y_diagonal = [idx if residue == ss_element else None for idx, residue in enumerate(self.ss_pred, 1)]
                if not any(y_diagonal):
                    continue

                trace_y_lower = [self.transform_coords_diagonal_axis(y, 1.5, lower_bound=True) for y in y_diagonal]
                trace_y_upper = [self.transform_coords_diagonal_axis(y, 1.5, lower_bound=False) for y in y_diagonal]
                trace_x_lower = [self.transform_coords_diagonal_axis(x, 1.5, lower_bound=True, y_axis=False) for x in
                                 x_diagonal]
                trace_x_upper = [self.transform_coords_diagonal_axis(x, 1.5, lower_bound=False, y_axis=False) for x in
                                 x_diagonal]

                traces += [
                    go.Scatter(
                        x=x,
                        y=y,
                        hovertext=['%s' % ss_element.name for idx in enumerate(x)],
                        hoverinfo='text',
                        mode="markers",
                        marker={
                            'symbol': 'diamond',
                            'size': 7,
                            'color': SecondaryStructureColor.__getattr__(ss_element.name).value,
                        },
                    ) for x, y in zip([trace_x_lower, trace_x_upper], [trace_y_lower, trace_y_upper])
                ]

        yield from traces

    @property
    def disorder_traces(self):

        traces = []

        if self.disorder_pred is not None:
            x_diagonal = [idx for idx in range(1, len(self.disorder_pred) + 1)]

            for state in DisorderStates:
                y_diagonal = [idx if residue == state else None for idx, residue in enumerate(self.disorder_pred, 1)]
                if not any(y_diagonal):
                    continue

                trace_y_lower = [self.transform_coords_diagonal_axis(y, 4.3, lower_bound=True) for y in y_diagonal]
                trace_y_upper = [self.transform_coords_diagonal_axis(y, 4.3, lower_bound=False) for y in y_diagonal]
                trace_x_lower = [self.transform_coords_diagonal_axis(x, 4.3, lower_bound=True, y_axis=False) for x in
                                 x_diagonal]
                trace_x_upper = [self.transform_coords_diagonal_axis(x, 4.3, lower_bound=False, y_axis=False) for x in
                                 x_diagonal]

                traces += [
                    go.Scatter(
                        x=x,
                        y=y,
                        hovertext=['%s' % state.name for idx in enumerate(x)],
                        hoverinfo='text',
                        mode="markers",
                        marker={
                            'symbol': 'diamond',
                            'size': 7,
                            'color': DisorderColor.__getattr__(state.name).value,
                        },
                    ) for x, y in zip([trace_x_lower, trace_x_upper], [trace_y_lower, trace_y_upper])
                ]

        yield from traces

    @property
    def conservation_traces(self):

        traces = []

        if self.conserv_pred is not None:
            x_diagonal = [idx for idx in range(1, len(self.conserv_pred) + 1)]

            for state in ConservationStates:
                y_diagonal = [idx if residue == state else None for idx, residue in enumerate(self.conserv_pred, 1)]
                if not any(y_diagonal):
                    continue

                trace_y_lower = [self.transform_coords_diagonal_axis(y, 6.3, lower_bound=True) for y in y_diagonal]
                trace_y_upper = [self.transform_coords_diagonal_axis(y, 6.3, lower_bound=False) for y in y_diagonal]
                trace_x_lower = [self.transform_coords_diagonal_axis(x, 6.3, lower_bound=True, y_axis=False) for x in
                                 x_diagonal]
                trace_x_upper = [self.transform_coords_diagonal_axis(x, 6.3, lower_bound=False, y_axis=False) for x in
                                 x_diagonal]

                traces += [
                    go.Scatter(
                        x=x,
                        y=y,
                        hovertext=['%s' % state.name for idx in enumerate(x)],
                        hoverinfo='text',
                        mode="markers",
                        marker={
                            'symbol': 'diamond',
                            'size': 7,
                            'color': ConservationColor.__getattr__(state.name).value,
                        },
                    ) for x, y in zip([trace_x_lower, trace_x_upper], [trace_y_lower, trace_y_upper])
                ]

        yield from traces

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

        if self.ss_pred is not None and DatasetReference.SECONDARY_STRUCTURE.name in self.active_tracks:
            for trace in self.ss_traces:
                figure.add_trace(trace)

        if self.disorder_pred is not None and DatasetReference.DISORDER.name in self.active_tracks:
            for trace in self.disorder_traces:
                figure.add_trace(trace)

        if self.conserv_pred is not None and DatasetReference.CONSERVATION.name in self.active_tracks:
            for trace in self.conservation_traces:
                figure.add_trace(trace)

        return figure
