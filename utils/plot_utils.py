import plotly.graph_objects as go
from enum import Enum
from loaders import DatasetReference
from parsers import DatasetStates
from components import MissingInputModal, MismatchModal, PlotPlaceHolder, DisplayControlCard
from layouts import ContextReference
from utils import ensure_triggered
import dash_core_components as dcc
from dash.dash import no_update
from operator import itemgetter


class ColorReference(Enum):
    INSIDE = 'green'
    OUTSIDE = 'yellow'
    INSERTED = 'red'
    DISORDER = 'rgba(120,0,0,0.4)'
    ORDER = 'rgba(0,120,0,0.4)'
    CONSERVED = 'rgba(0, 30, 255,0.4)'
    AVERAGE = 'rgba(0, 130, 255,0.4)'
    VARIABLE = 'rgba(0, 225, 255,0.4)'
    HELIX = 'rgba(247, 0, 255, 0.4)'
    COIL = 'rgba(255, 162, 0,0.4)'
    SHEET = 'rgba(0, 4, 255,0.4)'


def create_ConPlot(session, trigger, selected_tracks, factor=2, contact_marker_size=5, track_marker_size=7,
                   track_separation=2):
    if session is None or not ensure_triggered(trigger):
        return PlotPlaceHolder(), None, DisplayControlCard(), True

    available_tracks = get_available_tracks(session)
    selected_tracks = get_track_selection(selected_tracks)
    error = lookup_input_errors(session)

    if error is not None:
        return PlotPlaceHolder(), error, DisplayControlCard(), True

    axis_range = (0, len(session[DatasetReference.SEQUENCE.value]) + 1)
    figure = create_figure(axis_range)
    figure.add_trace(create_contact_trace(cmap=session[DatasetReference.CONTACT_MAP.value],
                                          seq_length=len(session[DatasetReference.SEQUENCE.value]),
                                          marker_size=contact_marker_size, factor=factor))

    for idx, dataset in enumerate(selected_tracks):
        if dataset is None:
            continue
        elif idx == 3:
            traces = get_diagonal_traces(sequence=session[DatasetReference.SEQUENCE.value], dataset=dataset,
                                         marker_size=track_marker_size, prediction=session[dataset])
        else:
            traces = get_traces(track_idx=idx, track_separation=track_separation, marker_size=track_marker_size,
                                dataset=dataset, prediction=session[dataset])

        for trace in traces:
            figure.add_trace(trace)

    graph = dcc.Graph(
        className='square-content', id='plot-graph', figure=figure,
        config={"toImageButtonOptions": {"width": None, "height": None}}
    )

    if trigger['prop_id'] == ContextReference.PLOT_CLICK.value:
        return graph, None, DisplayControlCard(available_tracks=available_tracks,
                                               selected_tracks=selected_tracks), False
    else:
        return graph, None, no_update, False


def get_available_tracks(session):
    available_tracks = []
    for track in session.keys():
        if track == DatasetReference.SEQUENCE.value or track == DatasetReference.CONTACT_MAP.value:
            pass
        elif session[track] is not None:
            available_tracks.append(track)
    return available_tracks


def get_missing_data(session):
    return [dataset for dataset in (DatasetReference.SEQUENCE, DatasetReference.CONTACT_MAP)
            if dataset.value not in session.keys() or session[dataset.value] is None]


def lookup_input_errors(session):
    """Check user input is coherent"""

    missing_data = get_missing_data(session)

    if any(missing_data):
        return MissingInputModal(*[missing.name for missing in missing_data])

    seq_length = len(session[DatasetReference.SEQUENCE.value])
    cmap_max_register = max((max(session[DatasetReference.CONTACT_MAP.value], key=itemgetter(0))[0],
                             max(session[DatasetReference.CONTACT_MAP.value], key=itemgetter(1))[0]))
    if cmap_max_register > seq_length - 1:
        return MismatchModal(DatasetReference.SEQUENCE)

    mismatched = []
    for dataset in session.keys():
        if dataset == DatasetReference.CONTACT_MAP.value or dataset == DatasetReference.SEQUENCE.value:
            pass
        elif session[dataset] is not None and len(session[dataset]) != seq_length:
            mismatched.append(dataset)

    if any(mismatched):
        return MismatchModal(*mismatched)

    return None


def create_scatter(x, y, symbol, marker_size, color, hovertext=None):
    return go.Scatter(
        x=x,
        y=y,
        hovertext=hovertext,
        hoverinfo='text' if hovertext is not None else 'none',
        mode="markers",
        marker={
            'symbol': symbol,
            'size': marker_size,
            'color': color
        },
    )


def create_figure(axis_range):
    figure = go.Figure(
        layout=go.Layout(
            xaxis={'range': axis_range, 'scaleanchor': "y", 'scaleratio': 1,
                   'tickvals': [x for x in range(*axis_range, 100)], 'ticks': 'inside',
                   'showline': True, 'linewidth': 2, 'linecolor': 'black'},
            yaxis={'range': axis_range, 'scaleanchor': "x", 'scaleratio': 1,
                   'tickvals': [x for x in range(*axis_range, 100)], 'ticks': 'inside',
                   'showline': True, 'linewidth': 2, 'linecolor': 'black'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10, 'autoexpand': False},
            hovermode='closest',
            showlegend=False,
            plot_bgcolor='rgba(0,0,0,0)',
        )
    )

    return figure


def create_contact_trace(cmap, seq_length, marker_size=5, factor=2):
    contacts = cmap[:int(round(seq_length / factor, 0))]
    res1_list = []
    res2_list = []
    hover_1 = []
    hover_2 = []
    for contact in contacts:
        res1_list.append(contact[0])
        res2_list.append(contact[1])
        hover_1.append('Contact: %s - %s | Confidence: %s' % (contact[0], contact[1], contact[2]))
        hover_2.append('Contact: %s - %s | Confidence: %s' % (contact[1], contact[0], contact[2]))

    x = res1_list + res2_list
    y = res2_list + res1_list
    hovertext = hover_1 + hover_2

    return create_scatter(x=x, y=y, symbol='circle', hovertext=hovertext, marker_size=marker_size, color='black')


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


def get_diagonal_traces(prediction, dataset, marker_size, sequence):
    if prediction is None:
        return None

    x_diagonal = [idx for idx in range(1, len(prediction) + 1)]
    states = DatasetStates.__getattr__(dataset).value
    traces = []

    for state in states:
        y = [idx if residue == state.value else None for idx, residue in enumerate(prediction, 1)]
        if not any(y):
            continue

        hovertext = ['Residue: {} ({}) | {}'.format(sequence[idx - 1], idx, state.name) for idx in x_diagonal]
        color = ColorReference.__getattr__(state.name).value

        traces.append(
            create_scatter(x_diagonal, y, 'diamond', marker_size=marker_size, color=color, hovertext=hovertext))

    return traces


def get_traces(prediction, dataset, track_idx, track_separation, marker_size):
    if prediction is None:
        return None

    traces = []
    x_diagonal = [idx for idx in range(1, len(prediction) + 1)]
    states = DatasetStates.__getattr__(dataset).value
    track_origin = abs(3 - track_idx)
    track_distance = track_separation * track_origin
    if track_idx > 3:
        lower_bound = True
    else:
        lower_bound = False

    for state in states:
        y_diagonal = [idx if residue == state.value else None for idx, residue in enumerate(prediction, 1)]
        if not any(y_diagonal):
            continue

        y = [transform_coords_diagonal_axis(y, track_distance, lower_bound=lower_bound) for y in y_diagonal]
        x = [transform_coords_diagonal_axis(x, track_distance, lower_bound=lower_bound, y_axis=False) for x in
             x_diagonal]
        hovertext = ['%s' % state.name for idx in enumerate(x)]
        color = ColorReference.__getattr__(state.name).value

        traces.append(create_scatter(x, y, 'diamond', marker_size=marker_size, color=color, hovertext=hovertext))

    return traces


def get_track_selection(selection):
    if len(selection) == 0:
        return [None] * 7
    else:
        return [track if track != 'None' else None for track in selection]
