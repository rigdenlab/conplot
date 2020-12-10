from collections import namedtuple
import components
from enum import Enum
import json
from operator import itemgetter
from parsers import DatasetStates
import plotly.graph_objects as go
from loaders import DatasetReference, AdditionalDatasetReference
from layouts import ContextReference
from utils import decompress_session, color_palettes, cache_utils
import dash_core_components as dcc

DisplayControlSettings = namedtuple('DisplayControlSettings', ('available_tracks', 'selected_tracks', 'axis_range',
                                                               'contact_marker_size', 'factor', 'track_marker_size',
                                                               'transparent', 'track_separation', 'selected_cmaps',
                                                               'available_maps', 'superimpose', 'selected_palettes',
                                                               'seq_length', 'seq_fname', 'alpha', 'cmap_selection',
                                                               'available_cmaps', 'distance_matrix', 'verbose_labels'))


class DefaultTrackLayout(Enum):
    MEMBRANE_TOPOLOGY = DatasetReference.MEMBRANE_TOPOLOGY.value.encode()
    SECONDARY_STRUCTURE = DatasetReference.SECONDARY_STRUCTURE.value.encode()
    DISORDER = DatasetReference.DISORDER.value.encode()
    CONSERVATION = DatasetReference.CONSERVATION.value.encode()
    CUSTOM = DatasetReference.CUSTOM.value.encode()


class PaletteDefaultLayout(Enum):
    MEMBRANE_TOPOLOGY = DatasetReference.MEMBRANE_TOPOLOGY.value.encode()
    SECONDARY_STRUCTURE = DatasetReference.SECONDARY_STRUCTURE.value.encode()
    DISORDER = DatasetReference.DISORDER.value.encode()
    CONSERVATION = DatasetReference.CONSERVATION.value.encode()
    CUSTOM = DatasetReference.CUSTOM.value.encode()
    HEATMAP = b'heatmap'


class DistanceLabels(Enum):
    BIN_0 = 'd ≤ 4Å'
    BIN_1 = '4Å < d ≤ 6Å'
    BIN_2 = '6Å < d ≤ 8Å'
    BIN_3 = '8Å < d ≤ 10Å'
    BIN_4 = '10Å < d ≤ 12Å'
    BIN_5 = '12Å < d ≤ 14Å'
    BIN_6 = '14Å < d ≤ 16Å'
    BIN_7 = '16Å < d ≤ 18Å'
    BIN_8 = '18Å < d ≤ 20Å'
    BIN_9 = 'd > 20Å'


def create_ConPlot(session_id, cache, trigger, selected_tracks, cmap_selection, selected_palettes, factor=2,
                   contact_marker_size=5, track_marker_size=5, track_separation=2, transparent=True, superimpose=False,
                   distance_matrix=False, verbose_labels=False):
    session = cache.hgetall(session_id)
    session, display_settings, verbose_labels, error = process_args(session, trigger, selected_tracks, cmap_selection,
                                                                    factor, contact_marker_size, track_separation,
                                                                    transparent, selected_palettes, superimpose,
                                                                    track_marker_size, distance_matrix, verbose_labels)

    if error is not None:
        cache_utils.remove_figure(session_id, cache)
        return components.PlotPlaceHolder(), error, components.DisplayControlCard(), True

    display_card = get_display_control_card(display_settings)
    figure = create_figure(display_settings.axis_range)

    if display_settings.superimpose:
        reference, matched, mismatched = get_superimposed_contact_traces(
            reference_cmap=session[display_settings.cmap_selection[0].encode()],
            secondary_cmap=session[display_settings.cmap_selection[1].encode()],
            seq_length=display_settings.seq_length, factor=display_settings.factor)
        figure.add_trace(
            create_superimposed_contact_traces(reference, marker_size=display_settings.contact_marker_size,
                                               color='grey', symbol='circle', verbose_labels=verbose_labels)
        )
        figure.add_trace(
            create_superimposed_contact_traces(mismatched, marker_size=display_settings.contact_marker_size,
                                               color='red', symbol='circle', verbose_labels=verbose_labels)
        )
        figure.add_trace(
            create_superimposed_contact_traces(matched, marker_size=display_settings.contact_marker_size,
                                               color='black', symbol='circle', verbose_labels=verbose_labels)
        )

    elif display_settings.distance_matrix:

        heat = [[0 for x in range(display_settings.seq_length + 1)] for y in range(display_settings.seq_length + 1)]
        hover = [[None for x in range(display_settings.seq_length + 1)] for y in range(display_settings.seq_length + 1)]

        for idx, fname in enumerate(display_settings.cmap_selection):
            if fname == '---':
                continue
            heat, hover = create_distogram(session[fname.encode()], idx, heat, hover, verbose_labels)

        colorscale = color_palettes.get_heatmap_colorscale(display_settings.selected_palettes[-1])
        figure.add_trace(create_heatmap(hovertext=hover, distances=heat, colorscale=colorscale))

    else:
        for idx, fname in enumerate(display_settings.cmap_selection):
            if fname == '---':
                continue
            figure.add_trace(
                create_contact_trace(cmap=session[fname.encode()], idx=idx, factor=display_settings.factor,
                                     marker_size=display_settings.contact_marker_size,
                                     seq_length=display_settings.seq_length, verbose_labels=verbose_labels)
            )

    for idx, fname in enumerate(display_settings.selected_tracks):
        if fname == '---':
            continue

        dataset = get_dataset(session, fname)
        index = [x.name for x in color_palettes.DatasetColorPalettes].index(dataset)
        palette = display_settings.selected_palettes[index]

        if idx == 4:
            traces = get_diagonal_traces(sequence=session[display_settings.seq_fname.encode()],
                                         dataset=dataset, color_palette=palette, prediction=session[fname.encode()],
                                         marker_size=display_settings.track_marker_size, alpha=display_settings.alpha)
        else:
            traces = get_traces(track_idx=idx, track_separation=display_settings.track_separation, dataset=dataset,
                                marker_size=display_settings.track_marker_size, alpha=display_settings.alpha,
                                color_palette=palette, prediction=session[fname.encode()])

        for trace in traces:
            figure.add_trace(trace)

    figure.update_xaxes(spikemode="across", showspikes=False)
    figure.update_yaxes(spikemode="across", showspikes=False)

    cache_utils.store_figure(session_id, figure.to_json(), json.dumps(display_settings._asdict()), cache)

    graph = dcc.Graph(
        className='square-content', id='plot-graph', figure=figure,
        config={'displaylogo': False, 'modeBarButtonsToRemove': ['select2d', 'lasso2d'],
                "toImageButtonOptions": {"width": None, "height": None}}
    )

    return graph, None, display_card, False


def get_display_control_card(display_settings):
    return components.DisplayControlCard(factor=display_settings.factor, superimpose=display_settings.superimpose,
                                         available_tracks=display_settings.available_tracks,
                                         selected_tracks=display_settings.selected_tracks,
                                         contact_marker_size=display_settings.contact_marker_size,
                                         track_marker_size=display_settings.track_marker_size,
                                         transparent=display_settings.transparent,
                                         track_separation=display_settings.track_separation,
                                         selected_cmaps=display_settings.cmap_selection,
                                         available_maps=display_settings.available_cmaps,
                                         selected_palettes=display_settings.selected_palettes,
                                         distance_matrix=display_settings.distance_matrix,
                                         verbose_labels=display_settings.verbose_labels)


def load_figure_json(figure_json):
    figure_kwargs = json.loads(figure_json)
    return go.Figure(**figure_kwargs)


def load_display_settings(display_json):
    display_dict = json.loads(display_json)
    return DisplayControlSettings(**display_dict)


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
        if session[cmap_fname.encode()][-1] == 'PDB' or session[cmap_fname.encode()][-1] == 'DISTO':
            cmap_max_register = max((max(session[cmap_fname.encode()][:-1], key=itemgetter(0))[0],
                                     max(session[cmap_fname.encode()][:-1], key=itemgetter(1))[0]))
        else:
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
                    mismatched.append(fname)

    if any(mismatched):
        return components.MismatchModal(*mismatched)

    return None


def process_args(session, trigger, selected_tracks, cmap_selection, factor, contact_marker_size, track_separation,
                 transparent, selected_palettes, superimpose, track_marker_size, distance_matrix, verbose_labels):
    session = decompress_session(session)

    error = lookup_input_errors(session)
    if error is not None:
        return None, None, None, error

    available_tracks, available_cmaps = get_available_data(session)
    seq_fname = session[DatasetReference.SEQUENCE.value.encode()]
    seq_length = len(session[seq_fname.encode()])
    axis_range = (0, len(session[seq_fname.encode()]) + 1)

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

    if superimpose and any(selection not in available_cmaps for selection in cmap_selection):
        superimpose = False

    display_settings = DisplayControlSettings(available_tracks=available_tracks, selected_tracks=selected_tracks,
                                              contact_marker_size=contact_marker_size, factor=factor,
                                              track_marker_size=track_marker_size, transparent=transparent,
                                              track_separation=track_separation, selected_cmaps=cmap_selection,
                                              available_maps=available_cmaps, superimpose=superimpose,
                                              selected_palettes=selected_palettes, axis_range=axis_range,
                                              seq_length=seq_length, seq_fname=seq_fname, alpha=alpha,
                                              cmap_selection=cmap_selection, available_cmaps=available_cmaps,
                                              distance_matrix=distance_matrix, verbose_labels=verbose_labels)

    if verbose_labels:
        fnames = [fname for fname in selected_tracks if fname != '---']
        verbose_labels = get_verbose_labels(fnames, session[display_settings.seq_fname.encode()], session)
    else:
        verbose_labels = None

    return session, display_settings, verbose_labels, error


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
                   'linewidth': 2, 'linecolor': 'black', 'nticks': 10},
            yaxis={'range': axis_range, 'scaleanchor': "x", 'scaleratio': 1, 'ticks': 'inside', 'showline': True,
                   'linewidth': 2, 'linecolor': 'black', 'nticks': 10},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10, 'autoexpand': False},
            hovermode='closest',
            showlegend=False,
            plot_bgcolor='rgba(0,0,0,0)',
        )
    )


def create_heatmap(distances, colorscale, hovertext=None):
    return go.Heatmap(
        z=distances,
        hovertext=hovertext,
        colorscale=colorscale,
        hoverinfo='text' if hovertext is not None else 'none',
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


def create_distogram(cmap, idx, distances, hover, verbose_labels=None):
    if idx == 1:
        idx_x = 1
        idx_y = 0
    else:
        idx_x = 0
        idx_y = 1

    if cmap[-1] == 'PDB':
        del cmap[-1]

    elif cmap[-1] == 'DISTO':
        cmap = cmap[:-1]

        if verbose_labels is not None:
            hover_template = 'Contact: {} - {} | Distance {} | Confidence: {}<br>{}<br>{}'
            for contact in cmap:
                distances[contact[idx_x]][contact[idx_y]] = 9 - contact[3]
                label = DistanceLabels.__getitem__(('BIN_{}'.format(contact[3]))).value
                hover_label = hover_template.format(contact[idx_y], contact[idx_x], label, contact[4],
                                                    verbose_labels[contact[idx_y] - 1],
                                                    verbose_labels[contact[idx_x] - 1])
                hover[contact[idx_x]][contact[idx_y]] = hover_label
        else:
            hover_template = 'Contact: {} - {} | Distance {} | Confidence: {}'
            for contact in cmap:
                distances[contact[idx_x]][contact[idx_y]] = 9 - contact[3]
                label = DistanceLabels.__getitem__(('BIN_{}'.format(contact[3]))).value
                hover_label = hover_template.format(contact[idx_y], contact[idx_x], label, contact[4])
                hover[contact[idx_x]][contact[idx_y]] = hover_label

        return distances, hover

    if verbose_labels is None:
        hover_template = 'Contact: {} - {} | Confidence: {}'
        for contact in cmap:
            distances[contact[idx_x]][contact[idx_y]] = contact[2]
            hover_label = hover_template.format(contact[idx_y], contact[idx_x], contact[2])
            hover[contact[idx_x]][contact[idx_y]] = hover_label

    else:
        hover_template = 'Contact: {} - {} | Confidence: {}<br>{}<br>{}'
        for contact in cmap:
            distances[contact[idx_x]][contact[idx_y]] = contact[2]
            hover_label = hover_template.format(contact[idx_y], contact[idx_x], contact[2],
                                                verbose_labels[contact[idx_y] - 1], verbose_labels[contact[idx_x] - 1])
            hover[contact[idx_x]][contact[idx_y]] = hover_label

    return distances, hover


def create_contact_trace(cmap, idx, seq_length, marker_size=5, factor=2, verbose_labels=None):
    if cmap[-1] == 'PDB' or cmap[-1] == 'DISTO':
        del cmap[-1]

    if factor != 0:
        cmap = cmap[:int(round(seq_length / factor, 0))]

    if idx == 1:
        idx_x = 0
        idx_y = 1
    else:
        idx_x = 1
        idx_y = 0

    res1_list = []
    res2_list = []
    hover = []

    if verbose_labels is not None:
        hover_template = 'Contact: %s - %s | Confidence: %s<br>%s<br>%s'
        for contact in cmap:
            res1_list.append(contact[idx_x])
            res2_list.append(contact[idx_y])
            res_x_label = verbose_labels[contact[idx_x] - 1]
            res_y_label = verbose_labels[contact[idx_y] - 1]
            hover.append(hover_template % (contact[idx_x], contact[idx_y], contact[2], res_x_label, res_y_label))
    else:
        hover_template = 'Contact: %s - %s | Confidence: %s'
        for contact in cmap:
            res1_list.append(contact[idx_x])
            res2_list.append(contact[idx_y])
            hover.append(hover_template % (contact[idx_x], contact[idx_y], contact[2]))

    return create_scatter(x=res1_list, y=res2_list, symbol='circle', hovertext=hover,
                          marker_size=marker_size, color='black')


def get_superimposed_contact_traces(reference_cmap, secondary_cmap, seq_length, factor=2):
    if factor != 0:
        secondary_cmap = secondary_cmap[:int(round(seq_length / factor, 0))]
        if reference_cmap[-1] == 'PDB' or reference_cmap[-1] == 'DISTO':
            del reference_cmap[-1]
        else:
            reference_cmap = reference_cmap[:int(round(seq_length / factor, 0))]

    reference_contacts = [contact[:2] for contact in reference_cmap]
    secondary_contacts = [contact[:2] for contact in secondary_cmap]

    matched = []
    mismatched = []
    reference = []

    for contact in reference_cmap:
        if contact[:2] in secondary_contacts:
            matched.append(contact)
        else:
            reference.append(contact)

    for contact in secondary_cmap:
        if contact[:2] not in reference_contacts:
            mismatched.append(contact)

    return reference, matched, mismatched


def create_superimposed_contact_traces(contacts, marker_size=5, color='black', symbol='circle', verbose_labels=None):
    res1_list = []
    res2_list = []
    hover_1 = []
    hover_2 = []

    if verbose_labels is not None:
        hover_template = 'Contact: %s - %s | Confidence: %s<br>%s<br>%s'
        for contact in contacts:
            res1_list.append(contact[0])
            res2_list.append(contact[1])
            res_1_label = verbose_labels[contact[0] - 1]
            res_2_label = verbose_labels[contact[1] - 1]
            hover_1.append(hover_template % (contact[0], contact[1], contact[2], res_1_label, res_2_label))
            hover_2.append(hover_template % (contact[1], contact[0], contact[2], res_2_label, res_1_label))
    else:
        hover_template = 'Contact: %s - %s | Confidence: %s'
        for contact in contacts:
            res1_list.append(contact[0])
            res2_list.append(contact[1])
            hover_1.append(hover_template % (contact[0], contact[1], contact[2]))
            hover_2.append(hover_template % (contact[1], contact[0], contact[2]))

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


def get_verbose_labels(fnames, sequence, session):
    states_dict = {
        DatasetReference.MEMBRANE_TOPOLOGY.value: {
            1: 'INSIDE',
            2: 'OUTSIDE',
            3: 'INSERTED'
        },
        DatasetReference.CONSERVATION.value: {
            1: 'VARIABLE_1',
            2: 'VARIABLE_2',
            3: 'VARIABLE_3',
            4: 'AVERAGE_4',
            5: 'AVERAGE_5',
            6: 'AVERAGE_6',
            7: 'CONSERVED_7',
            8: 'CONSERVED_8',
            9: 'CONSERVED_9'
        },
        DatasetReference.CUSTOM.value: {
            1: 'CUSTOM_1',
            2: 'CUSTOM_2',
            3: 'CUSTOM_3',
            4: 'CUSTOM_4',
            5: 'CUSTOM_5',
            6: 'CUSTOM_6',
            7: 'CUSTOM_7',
            8: 'CUSTOM_8',
            9: 'CUSTOM_9',
            10: 'CUSTOM_10',
            11: 'CUSTOM_11',
            'NAN': 'CUSTOM_NAN'
        },
        DatasetReference.DISORDER.value: {
            1: 'DISORDER',
            2: 'ORDER'
        },
        DatasetReference.SECONDARY_STRUCTURE.value: {
            1: 'HELIX',
            2: 'COIL',
            3: 'SHEET'
        }
    }

    all_predictions = []
    for fname in set(fnames):
        dataset = get_dataset(session, fname)
        dataset_dict = states_dict[dataset]
        prediction = [dataset_dict[x] for x in session[fname.encode()]]
        all_predictions.append(prediction)

    labels = []
    for idx, residue in enumerate(sequence, 1):
        current_label = 'Residue {} ({})'.format(idx, residue)
        for prediction in all_predictions:
            current_label += ' | {}'.format(prediction[idx - 1])
        labels.append(current_label)

    return labels
