import components
from enum import Enum
from operator import itemgetter
from parsers import DatasetStates
import plotly.graph_objects as go
from loaders import DatasetReference, AdditionalDatasetReference
from layouts import ContextReference
from utils import decompress_session, color_palettes
import dash_core_components as dcc


class DefaultTrackLayout(Enum):
    MEMBRANE_TOPOLOGY = DatasetReference.MEMBRANE_TOPOLOGY.value.encode()
    SECONDARY_STRUCTURE = DatasetReference.SECONDARY_STRUCTURE.value.encode()
    DISORDER = DatasetReference.DISORDER.value.encode()
    CONSERVATION = DatasetReference.CONSERVATION.value.encode()
    CUSTOM = DatasetReference.CUSTOM.value.encode()


def create_ConPlot(session, trigger, selected_tracks, cmap_selection, selected_palettes, factor=2,
                   contact_marker_size=5, track_marker_size=5, track_separation=2, transparent=True, superimpose=False):
    session, available_tracks, selected_tracks, available_cmaps, cmap_selection, factor, contact_marker_size, \
    track_separation, alpha, selected_palettes, error = process_args(session, trigger, selected_tracks, cmap_selection,
                                                                     factor, contact_marker_size, track_separation,
                                                                     transparent, selected_palettes)

    if error is not None:
        return components.PlotPlaceHolder(), error, components.DisplayControlCard(), True

    display_card = components.DisplayControlCard(available_tracks=available_tracks, selected_tracks=selected_tracks,
                                                 contact_marker_size=contact_marker_size, factor=factor,
                                                 track_marker_size=track_marker_size, transparent=transparent,
                                                 track_separation=track_separation, selected_cmaps=cmap_selection,
                                                 available_maps=available_cmaps, superimpose=superimpose,
                                                 selected_palettes=selected_palettes)
    seq_fname = session[DatasetReference.SEQUENCE.value.encode()]
    axis_range = (0, len(session[seq_fname.encode()]) + 1)
    figure = create_figure(axis_range)

    if not superimpose:
        for idx, fname in enumerate(cmap_selection):
            if fname == '---':
                continue
            figure.add_trace(
                create_contact_trace(cmap=session[fname.encode()], idx=idx, marker_size=contact_marker_size,
                                     seq_length=len(session[seq_fname.encode()]), factor=factor)
            )
    else:
        reference, matched, mismatched = get_superimposed_contact_traces(
            reference_cmap=session[cmap_selection[0].encode()],
            secondary_cmap=session[cmap_selection[1].encode()],
            seq_length=len(session[seq_fname.encode()]),
            factor=factor)
        figure.add_trace(
            create_superimposed_contact_traces(reference, marker_size=contact_marker_size,
                                               color='grey', symbol='circle')
        )
        figure.add_trace(
            create_superimposed_contact_traces(mismatched, marker_size=contact_marker_size,
                                               color='black', symbol='circle')
        )
        figure.add_trace(
            create_superimposed_contact_traces(matched, marker_size=contact_marker_size,
                                               color='red', symbol='circle')
        )

    for idx, fname in enumerate(selected_tracks):
        if fname == '---':
            continue

        dataset = get_dataset(session, fname)
        index = [x.name for x in color_palettes.DatasetColorPalettes].index(dataset)
        palette = selected_palettes[index]

        if idx == 4:
            traces = get_diagonal_traces(sequence=session[seq_fname.encode()], dataset=dataset, color_palette=palette,
                                         marker_size=track_marker_size, prediction=session[fname.encode()], alpha=alpha)
        else:
            traces = get_traces(track_idx=idx, track_separation=track_separation, marker_size=track_marker_size,
                                dataset=dataset, prediction=session[fname.encode()], alpha=alpha, color_palette=palette)

        for trace in traces:
            figure.add_trace(trace)

    graph = dcc.Graph(
        className='square-content', id='plot-graph', figure=figure,
        config={'displaylogo': False, 'modeBarButtonsToRemove': ['select2d', 'lasso2d'],
                "toImageButtonOptions": {"width": None, "height": None}}
    )

    return graph, None, display_card, False


def get_missing_data(session):
    missing_data = []

    if DatasetReference.SEQUENCE.value.encode() not in session:
        missing_data.append(DatasetReference.SEQUENCE)
    if DatasetReference.CONTACT_MAP.value.encode() not in session:
        missing_data.append(DatasetReference.CONTACT_MAP)
    elif not session[DatasetReference.CONTACT_MAP.value.encode()]:
        missing_data.append(DatasetReference.CONTACT_MAP)

    return missing_data


def lookup_input_errors(session):
    """Check user input is coherent"""

    missing_data = get_missing_data(session)

    if any(missing_data):
        return components.MissingInputModal(*[missing.name for missing in missing_data])

    seq_fname = session[DatasetReference.SEQUENCE.value.encode()]
    seq_length = len(session[seq_fname.encode()])

    mismatched = []
    for cmap_fname in session[DatasetReference.CONTACT_MAP.value.encode()]:
        cmap_max_register = max((max(session[cmap_fname.encode()], key=itemgetter(0))[0],
                                 max(session[cmap_fname.encode()], key=itemgetter(1))[0]))
        if cmap_max_register > seq_length:
            mismatched.append(cmap_fname)

    if any(mismatched):
        return components.MismatchSequenceModal(*mismatched)

    mismatched = []
    for dataset in AdditionalDatasetReference:
        if dataset.value.encode() in session.keys() and session[dataset.value.encode()]:
            for fname in session[dataset.value.encode()]:
                if len(session[fname.encode()]) != seq_length:
                    mismatched.append(dataset.value)

    if any(mismatched):
        return components.MismatchModal(*mismatched)

    return None


def process_args(session, trigger, selected_tracks, cmap_selection, factor, contact_marker_size, track_separation,
                 transparent, selected_palettes):
    session = decompress_session(session)

    error = lookup_input_errors(session)
    if error is not None:
        return None, None, None, None, None, None, None, None, None, None, error

    available_tracks, available_cmaps = get_available_data(session)
    seq_fname = session[DatasetReference.SEQUENCE.value.encode()]
    seq_length = len(session[seq_fname.encode()])

    if transparent:
        alpha = '0.6'
    else:
        alpha = '1.0'

    if trigger['prop_id'] == ContextReference.PLOT_CLICK.value:
        if seq_length >= 700:
            contact_marker_size = 2
        else:
            contact_marker_size = 3
        track_separation = round(seq_length / 100)
        selected_tracks, cmap_selection, selected_palettes = get_default_layout(session)
    else:
        selected_tracks, cmap_selection = get_user_selection(cmap_selection, available_cmaps,
                                                             selected_tracks, available_tracks)
    return session, available_tracks, selected_tracks, available_cmaps, cmap_selection, factor, contact_marker_size, \
           track_separation, alpha, selected_palettes, error


def get_available_data(session):
    available_tracks = []
    for dataset in AdditionalDatasetReference:
        if dataset.value.encode() in session.keys() and session[dataset.value.encode()]:
            available_tracks += session[dataset.value.encode()]

    available_cmaps = []
    for cmap_fname in session[DatasetReference.CONTACT_MAP.value.encode()]:
        available_cmaps.append(cmap_fname)

    return available_tracks, available_cmaps


def get_user_selection(cmap_selection, available_cmaps, track_selection, available_tracks):
    if len(cmap_selection) == 0:
        cmap_selection = ['---'] * 2
    else:
        cmap_selection = [fname if fname in available_cmaps else '---' for fname in cmap_selection]

    if len(track_selection) == 0:
        track_selection = ['---'] * 9
    else:
        track_selection = [track if track in available_tracks else '---' for track in track_selection]

    return track_selection, cmap_selection


def get_default_layout(session):
    cmap_fname = session[DatasetReference.CONTACT_MAP.value.encode()][0]
    selected_palettes = ['PALETTE_1'] * len(color_palettes.DatasetColorPalettes)
    tracks = []

    for dataset in DefaultTrackLayout:
        if dataset.value in session.keys() and session[dataset.value]:
            tracks.append(session[dataset.value][0])

    if not any(tracks):
        return ['---'] * 9, (cmap_fname, cmap_fname), selected_palettes
    else:
        missing_tracks = ['---' for missing in range(0, 5 - len(tracks))]
        tracks += missing_tracks
        return tracks[1:][::-1] + tracks, (cmap_fname, cmap_fname), selected_palettes


def get_dataset(session, fname):
    for dataset in AdditionalDatasetReference:
        if dataset.value.encode() in session.keys() and fname in session[dataset.value.encode()]:
            return dataset.value


def create_figure(axis_range):
    return go.Figure(
        layout=go.Layout(
            xaxis={'range': axis_range, 'scaleanchor': "y", 'scaleratio': 1, 'ticks': 'inside', 'showline': True,
                   'linewidth': 2, 'linecolor': 'black'},
            yaxis={'range': axis_range, 'scaleanchor': "x", 'scaleratio': 1, 'ticks': 'inside', 'showline': True,
                   'linewidth': 2, 'linecolor': 'black'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10, 'autoexpand': False},
            hovermode='closest',
            showlegend=False,
            plot_bgcolor='rgba(0,0,0,0)',
        )
    )


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


def create_contact_trace(cmap, idx, seq_length, marker_size=5, factor=2):
    if factor != 0:
        cmap = cmap[:int(round(seq_length / factor, 0))]

    res1_list = []
    res2_list = []
    hover_1 = []
    hover_2 = []
    for contact in cmap:
        contact[:2] = sorted(contact[:2])
        res1_list.append(contact[0])
        res2_list.append(contact[1])
        hover_1.append('Contact: %s - %s | Confidence: %s' % (contact[0], contact[1], contact[2]))
        hover_2.append('Contact: %s - %s | Confidence: %s' % (contact[1], contact[0], contact[2]))

    if idx == 1:
        return create_scatter(x=res1_list, y=res2_list, symbol='circle', hovertext=hover_1, marker_size=marker_size,
                              color='black')

    else:
        return create_scatter(x=res2_list, y=res1_list, symbol='circle', hovertext=hover_2, marker_size=marker_size,
                              color='black')


def get_superimposed_contact_traces(reference_cmap, secondary_cmap, seq_length, factor=2):
    if factor != 0:
        reference_cmap = reference_cmap[:int(round(seq_length / factor, 0))]
        secondary_cmap = secondary_cmap[:int(round(seq_length / factor, 0))]

    reference_contacts = [contact[:2] for contact in reference_cmap]
    secondary_contacts = [contact[:2] for contact in secondary_cmap]

    matched = []
    mismatched = []
    reference = []

    for contact in reference_cmap:
        if contact[:2] in secondary_contacts or contact[:2][::-1] in secondary_contacts:
            matched.append(contact)
        else:
            reference.append(contact)

    for contact in secondary_cmap:
        if contact[:2] not in reference_contacts or contact[:2][::-1] in reference_contacts:
            mismatched.append(contact)

    return reference, matched, mismatched


def create_superimposed_contact_traces(contacts, marker_size=5, color='black', symbol='circle'):
    res1_list = []
    res2_list = []
    hover_1 = []
    hover_2 = []

    for contact in contacts:
        contact[:2] = sorted(contact[:2])
        res1_list.append(contact[0])
        res2_list.append(contact[1])
        hover_1.append('Contact: %s - %s | Confidence: %s' % (contact[0], contact[1], contact[2]))
        hover_2.append('Contact: %s - %s | Confidence: %s' % (contact[1], contact[0], contact[2]))

    x = res1_list + res2_list
    y = res2_list + res1_list
    hovertext = hover_1 + hover_2

    return create_scatter(x=x, y=y, symbol=symbol, hovertext=hovertext, marker_size=marker_size, color=color)


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


def get_diagonal_traces(prediction, dataset, marker_size, sequence, alpha, color_palette):
    if prediction is None:
        return None

    x_diagonal = [idx for idx in range(1, len(prediction) + 1)]
    states = DatasetStates.__getattr__(dataset).value
    palette = color_palettes.DatasetColorPalettes.__getattr__(dataset).value.__getattr__(color_palette).value
    traces = []

    for state in states:
        y = [idx if residue == state.value else None for idx, residue in enumerate(prediction, 1)]
        if not any(y):
            continue

        hovertext = ['Residue: {} ({}) | {}'.format(sequence[idx - 1], idx, state.name) for idx in x_diagonal]
        color = palette.__getattr__(state.name).value
        color = color.format(alpha)

        traces.append(
            create_scatter(x_diagonal, y, 'diamond', marker_size=marker_size, color=color, hovertext=hovertext))

    return traces


def get_traces(prediction, dataset, track_idx, track_separation, marker_size, alpha, color_palette):
    if prediction is None:
        return None

    traces = []
    x_diagonal = [idx for idx in range(1, len(prediction) + 1)]
    states = DatasetStates.__getattr__(dataset).value
    palette = color_palettes.DatasetColorPalettes.__getattr__(dataset).value.__getattr__(color_palette).value
    track_origin = abs(4 - track_idx)
    track_distance = track_separation * track_origin
    if track_idx > 4:
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
        color = palette.__getattr__(state.name).value
        color = color.format(alpha)

        traces.append(create_scatter(x, y, 'diamond', marker_size=marker_size, color=color, hovertext=hovertext))

    return traces
