import plotly.graph_objects as go
from werkzeug.utils import cached_property
from enum import Enum
from loaders import DatasetReference
from parsers import MembraneStates, SecondaryStructureStates, DisorderStates, ConservationStates
from components import MissingInput_Modal, MismatchModal, PlotPlaceHolder, DisplayControlCard
from layouts import ContextReference
from utils import ensure_triggered
import dash_core_components as dcc
from dash.dash import no_update


class MembraneTopologyColor(Enum):
    INSIDE = 'green'
    OUTSIDE = 'yellow'
    INSERTED = 'red'


class DisorderColor(Enum):
    DISORDER = 'rgba(120,0,0,0.4)'
    ORDER = 'rgba(0,120,0,0.4)'


class ConservationColor(Enum):
    CONSERVED = 'rgba(0, 30, 255,0.4)'
    AVERAGE = 'rgba(0, 130, 255,0.4)'
    VARIABLE = 'rgba(0, 225, 255,0.4)'


class SecondaryStructureColor(Enum):
    HELIX = 'rgba(247, 0, 255, 0.4)'
    COIL = 'rgba(255, 162, 0,0.4)'
    SHEET = 'rgba(0, 4, 255,0.4)'


def create_plot(session, trigger, factor, active_tracks):
    if session is None or not ensure_triggered(trigger):
        return PlotPlaceHolder(), None, DisplayControlCard()

    plot = Plot(session)
    if plot.error is not None:
        return PlotPlaceHolder(), plot.error, DisplayControlCard()
    elif trigger[0]['prop_id'] == ContextReference.PLOT_CLICK.value:
        return dcc.Graph(id='plot-graph', style={'height': '80vh'}, figure=plot.get_figure()), None, DisplayControlCard(
            available_tracks=plot.active_tracks, factor=plot.factor)
    else:
        plot.factor = factor
        plot.active_tracks = active_tracks
        return dcc.Graph(id='plot-graph', style={'height': '80vh'}, figure=plot.get_figure()), None, no_update


class Plot(object):

    def __init__(self, session, factor=2, remove_neighbors=True):
        self.session = session
        self.factor = factor
        self.remove_neighbors = remove_neighbors
        self.active_tracks = []
        self.error = None
        self._lookup_input_errors()

        for track in self.session.keys():
            if track == DatasetReference.SEQUENCE.value or track == DatasetReference.CONTACT_MAP.value:
                pass
            elif self.session[track] is not None:
                self.active_tracks.append(track)

    @property
    def missing_data(self):
        return [dataset for dataset in (DatasetReference.SEQUENCE, DatasetReference.CONTACT_MAP)
                if dataset.value not in self.session.keys() or self.session[dataset.value] is None]

    @cached_property
    def cmap_max_register(self):
        return max(
            self.session[DatasetReference.CONTACT_MAP.value][0] + self.session[DatasetReference.CONTACT_MAP.value][1])

    @cached_property
    def seq_length(self):
        return len(self.session[DatasetReference.SEQUENCE.value])

    @cached_property
    def axis_range(self):
        return (0, self.seq_length + 1)

    @property
    def y_axis_trace(self):
        return go.Scatter(
            x=[0 for x in range(*self.axis_range, 10)],
            y=[y for y in range(*self.axis_range, 10)],
            hoverinfo='none',
            mode='lines+markers',
            marker={
                'symbol': 'triangle-right',
                'size': 5,
                'color': 'black'
            }
        )

    @property
    def x_axis_trace(self):
        return go.Scatter(
            x=[x for x in range(*self.axis_range, 10)],
            y=[0 for y in range(*self.axis_range, 10)],
            hoverinfo='none',
            mode='lines+markers',
            marker={
                'symbol': 'triangle-up',
                'size': 5,
                'color': 'black'
            }
        )

    @property
    def contact_trace(self):

        contacts = self.session[DatasetReference.CONTACT_MAP.value][:int(round(self.seq_length / self.factor, 0))]
        res1_list = []
        res2_list = []
        hover_1 = []
        hover_2 = []
        for contact in contacts:
            res1_list.append(contact[0])
            res2_list.append(contact[1])
            hover_1.append('Contact: %s - %s | Confidence: %s' % (contact[0], contact[1], contact[2]))
            hover_2.append('Contact: %s - %s | Confidence: %s' % (contact[1], contact[0], contact[2]))

        return go.Scatter(
            x=res1_list + res2_list,
            y=res2_list + res1_list,
            hoverinfo='text',
            hovertext=hover_1 + hover_2,
            mode='markers',
            marker={
                'symbol': 'circle',
                'size': 5,
                'color': 'black'
            }
        )

    def get_membrane_trace(self, topology):

        if self.session[DatasetReference.MEMBRANE_TOPOLOGY.value] is None:
            return None
        else:
            mem_pred = self.session[DatasetReference.MEMBRANE_TOPOLOGY.value]

        x = [idx for idx in range(1, len(mem_pred) + 1)]
        y = [idx if residue == topology.value else None for idx, residue in enumerate(mem_pred, 1)]
        residue_names = ['Residue: {} ({}) | {}' \
                         ''.format(self.session[DatasetReference.SEQUENCE.value][idx - 1], idx, topology.name)
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

    @property
    def ss_traces(self):

        traces = []

        if self.session[DatasetReference.MEMBRANE_TOPOLOGY.value] is not None:

            ss_pred = self.session[DatasetReference.MEMBRANE_TOPOLOGY.value]
            x_diagonal = [idx for idx in range(1, len(ss_pred) + 1)]

            for ss_element in SecondaryStructureStates:
                y_diagonal = [idx if residue == ss_element.value else None for idx, residue in enumerate(ss_pred, 1)]
                if not any(y_diagonal):
                    continue

                trace_y_lower = [self.transform_coords_diagonal_axis(y, 2, lower_bound=True) for y in y_diagonal]
                trace_y_upper = [self.transform_coords_diagonal_axis(y, 2, lower_bound=False) for y in y_diagonal]
                trace_x_lower = [self.transform_coords_diagonal_axis(x, 2, lower_bound=True, y_axis=False) for x in
                                 x_diagonal]
                trace_x_upper = [self.transform_coords_diagonal_axis(x, 2, lower_bound=False, y_axis=False) for x in
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

        if self.session[DatasetReference.DISORDER.value] is not None:
            disorder_pred = self.session[DatasetReference.DISORDER.value]
            x_diagonal = [idx for idx in range(1, len(disorder_pred) + 1)]

            for state in DisorderStates:
                y_diagonal = [idx if residue == state.value else None for idx, residue in enumerate(disorder_pred, 1)]
                if not any(y_diagonal):
                    continue

                trace_y_lower = [self.transform_coords_diagonal_axis(y, 4, lower_bound=True) for y in y_diagonal]
                trace_y_upper = [self.transform_coords_diagonal_axis(y, 4, lower_bound=False) for y in y_diagonal]
                trace_x_lower = [self.transform_coords_diagonal_axis(x, 4, lower_bound=True, y_axis=False) for x in
                                 x_diagonal]
                trace_x_upper = [self.transform_coords_diagonal_axis(x, 4, lower_bound=False, y_axis=False) for x in
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

        if self.session[DatasetReference.CONSERVATION.value] is not None:
            conserv_pred = self.session[DatasetReference.CONSERVATION.value]
            x_diagonal = [idx for idx in range(1, len(conserv_pred) + 1)]

            for state in ConservationStates:
                y_diagonal = [idx if residue == state.value else None for idx, residue in enumerate(conserv_pred, 1)]
                if not any(y_diagonal):
                    continue

                trace_y_lower = [self.transform_coords_diagonal_axis(y, 6, lower_bound=True) for y in y_diagonal]
                trace_y_upper = [self.transform_coords_diagonal_axis(y, 6, lower_bound=False) for y in y_diagonal]
                trace_x_lower = [self.transform_coords_diagonal_axis(x, 6, lower_bound=True, y_axis=False) for x in
                                 x_diagonal]
                trace_x_upper = [self.transform_coords_diagonal_axis(x, 6, lower_bound=False, y_axis=False) for x in
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

    def _lookup_input_errors(self):
        """Check user input is coherent"""

        if any(self.missing_data):
            self.error = MissingInput_Modal(*[missing.name for missing in self.missing_data])
        elif self.cmap_max_register > self.seq_length - 1:
            self.error = MismatchModal(DatasetReference.SEQUENCE)

        mismatched = []
        for dataset in self.session.keys():
            if dataset == DatasetReference.CONTACT_MAP.value or dataset == DatasetReference.SEQUENCE.value:
                pass
            elif self.session[dataset] is not None and len(self.session[dataset]) != self.seq_length:
                mismatched.append(dataset)

        if any(mismatched):
            self.error = MismatchModal(*mismatched)

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
        figure.add_trace(self.x_axis_trace)
        figure.add_trace(self.y_axis_trace)
        if DatasetReference.MEMBRANE_TOPOLOGY.value in self.active_tracks:
            figure.add_trace(self.get_membrane_trace(MembraneStates.INSIDE))
            figure.add_trace(self.get_membrane_trace(MembraneStates.OUTSIDE))
            figure.add_trace(self.get_membrane_trace(MembraneStates.INSERTED))

        if DatasetReference.SECONDARY_STRUCTURE.value in self.active_tracks:
            for trace in self.ss_traces:
                figure.add_trace(trace)

        if DatasetReference.DISORDER.value in self.active_tracks:
            for trace in self.disorder_traces:
                figure.add_trace(trace)

        if DatasetReference.CONSERVATION.value in self.active_tracks:
            for trace in self.conservation_traces:
                figure.add_trace(trace)

        return figure

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
