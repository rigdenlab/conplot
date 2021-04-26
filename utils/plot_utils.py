from collections import namedtuple
import components
from dash.dash import no_update
import dash_core_components as dcc
from enum import Enum
import itertools
import json
from loaders import DatasetReference, AdditionalDatasetReference, STATES
from layouts import ContextReference
import plotly.graph_objects as go
from utils import decompress_session, color_palettes, cache_utils, tracks_utils, cmap_utils, heatmap_utils

DisplayControlSettings = namedtuple('DisplayControlSettings', ('available_tracks', 'selected_tracks', 'axis_range',
                                                               'contact_marker_size', 'factor', 'track_marker_size',
                                                               'transparent', 'track_separation', 'selected_cmaps',
                                                               'available_maps', 'superimpose', 'selected_palettes',
                                                               'seq_length', 'seq_fname', 'alpha', 'cmap_selection',
                                                               'available_cmaps', 'heatmap', 'verbose_labels'))


class DefaultTrackLayout(Enum):
    MEMBRANE_TOPOLOGY = DatasetReference.MEMBRANE_TOPOLOGY.value.encode()
    SECONDARY_STRUCTURE = DatasetReference.SECONDARY_STRUCTURE.value.encode()
    DISORDER = DatasetReference.DISORDER.value.encode()
    CONSERVATION = DatasetReference.CONSERVATION.value.encode()
    CUSTOM = DatasetReference.CUSTOM.value.encode()


def create_ConPlot(session_id, cache, trigger, selected_tracks, cmap_selection, selected_palettes, factor=2,
                   contact_marker_size=5, track_marker_size=5, track_separation=2, transparent=True, superimpose=False,
                   heatmap=False, verbose_labels=False):
    session = cache.hgetall(session_id)
    session, display_settings, verbose_labels, error = process_args(session_id, session, trigger, selected_tracks,
                                                                    cmap_selection, factor, contact_marker_size,
                                                                    track_separation, transparent, selected_palettes,
                                                                    superimpose, track_marker_size, heatmap,
                                                                    verbose_labels, cache)

    if error is not None:
        return error

    display_card = get_display_control_card(display_settings)
    figure = create_figure(display_settings.axis_range)

    add_contact_trace(session, display_settings, figure, verbose_labels)
    add_additional_tracks(session_id, session, display_settings, figure, cache)

    figure.update_xaxes(spikemode="across", showspikes=False)
    figure.update_yaxes(spikemode="across", showspikes=False)

    cache_utils.store_figure(session_id, figure.to_json(), json.dumps(display_settings._asdict()), cache)

    graph = dcc.Graph(className='square-content', id='plot-graph', figure=figure,
                      config={'displaylogo': False, 'modeBarButtonsToRemove': ['select2d', 'lasso2d'],
                              "toImageButtonOptions": {"width": None, "height": None}})

    return graph, None, display_card, False


def add_additional_tracks(session_id, session, display_settings, figure, cache):
    for idx, fname in enumerate(display_settings.selected_tracks):
        if fname == '--- Empty ---':
            continue

        dataset, prediction = tracks_utils.retrieve_dataset_prediction(session_id, session, fname, display_settings,
                                                                       cache)
        palette_idx = [x.name for x in color_palettes.DatasetColorPalettes].index(dataset)
        palette = display_settings.selected_palettes[palette_idx]

        if idx == 4:
            traces = tracks_utils.get_diagonal_trace(prediction, dataset, display_settings.track_marker_size,
                                                     session[display_settings.seq_fname.encode()],
                                                     display_settings.alpha, palette)
        else:
            traces = tracks_utils.get_traces(prediction, dataset, idx, display_settings.track_separation,
                                             display_settings.track_marker_size, display_settings.alpha, palette)

        for trace in traces:
            figure.add_trace(trace)


def add_contact_trace(session, display_settings, figure, verbose_labels):
    if display_settings.superimpose and display_settings.heatmap:
        heat, hover, colorscale = heatmap_utils.superimpose_heatmaps(session, display_settings, verbose_labels)
        figure.add_trace(heatmap_utils.create_heatmap_trace(hovertext=hover, distances=heat, colorscale=colorscale))

    elif display_settings.heatmap:
        heat, hover, colorscale = heatmap_utils.create_heatmap(session, display_settings, verbose_labels)
        figure.add_trace(heatmap_utils.create_heatmap_trace(hovertext=hover, distances=heat, colorscale=colorscale))

    elif display_settings.superimpose:
        reference_cmap = session[display_settings.cmap_selection[0].encode()]
        predicted_cmap = session[display_settings.cmap_selection[1].encode()]

        traces = cmap_utils.create_superimposed_cmap(reference_cmap, predicted_cmap, display_settings, verbose_labels)
        for trace in traces:
            figure.add_trace(trace)

    else:
        for idx, fname in enumerate(display_settings.cmap_selection):
            if fname == '--- Empty ---':
                continue

            cmap = session[fname.encode()]
            size = display_settings.contact_marker_size
            x, y, hover = cmap_utils.create_cmap(cmap, idx, display_settings, verbose_labels)
            figure.add_trace(cmap_utils.create_cmap_trace(x, y, 'circle', size, 'black', hover))


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
                                         distance_matrix=display_settings.heatmap,
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


def lookup_input_errors(session_id, session, cmap_selection, superimpose, heatmap, cache):
    missing_data = get_missing_data(session)

    if any(missing_data):
        cache_utils.remove_figure(session_id, cache)
        error = components.PlotPlaceHolder(), \
                components.MissingInputModal(*[missing.name for missing in missing_data]), \
                components.DisplayControlCard(), True
        return None, None, None, error

    if superimpose and heatmap:
        reference_cmap = session[cmap_selection[0].encode()]
        predicted_cmap = session[cmap_selection[1].encode()]
        error = no_update, components.InvalidSuperposeHeatmapModal(), no_update, no_update
        if not isinstance(reference_cmap[0], str) or not isinstance(predicted_cmap[0], str):
            return None, None, None, error

    return None


def process_args(session_id, session, trigger, selected_tracks, cmap_selection, factor, contact_marker_size,
                 track_separation, transparent, selected_palettes, superimpose, track_marker_size, heatmap,
                 verbose_labels, cache):
    session = decompress_session(session)

    error = lookup_input_errors(session_id, session, cmap_selection, superimpose, heatmap, cache)
    if error is not None:
        return error

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
    elif superimpose and len(set(cmap_selection)) == 1:
        superimpose = False

    display_settings = DisplayControlSettings(available_tracks=available_tracks, selected_tracks=selected_tracks,
                                              contact_marker_size=contact_marker_size, factor=factor,
                                              track_marker_size=track_marker_size, transparent=transparent,
                                              track_separation=track_separation, selected_cmaps=cmap_selection,
                                              available_maps=available_cmaps, superimpose=superimpose,
                                              selected_palettes=selected_palettes, axis_range=axis_range,
                                              seq_length=seq_length, seq_fname=seq_fname, alpha=alpha,
                                              cmap_selection=cmap_selection, available_cmaps=available_cmaps,
                                              heatmap=heatmap, verbose_labels=verbose_labels)

    if verbose_labels:
        fnames = [fname for fname in selected_tracks if fname != '--- Empty ---']
        verbose_labels = get_verbose_labels(session_id, session, fnames, display_settings, cache)
    else:
        verbose_labels = None

    return session, display_settings, verbose_labels, None


def separate_pdb_cmaps(session, cmap_fname_list):
    non_pdb_fnames = []
    pdb_fnames = []

    for fname in cmap_fname_list:
        cmap = session[fname.encode()]
        if cmap[0] == 'PDB':
            pdb_fnames.append(fname)
        else:
            non_pdb_fnames.append(fname)

    return pdb_fnames, non_pdb_fnames


def get_available_data(session):
    available_tracks = [{'label': '--- Empty ---', 'value': 'Empty_1'},
                        {'label': '--- Seq. Hydrophobicity ---', 'value': 'Hydrophobicity_Header', 'disabled': True},
                        {'label': session[DatasetReference.SEQUENCE.value.encode()],
                         'value': session[DatasetReference.SEQUENCE.value.encode()]},
                        {'label': '--- Contact Density ---', 'value': 'Density_Header', 'disabled': True}]

    available_cmaps, cmap_fname_list, cmap_density = get_cmap_density_tracks(session)

    if not cmap_fname_list:
        available_tracks.append({'label': '--- Empty ---', 'value': 'Empty_2'})
        available_tracks.append({'label': '--- Contact Diff ---', 'value': 'Diff_Header', 'disabled': True})
        available_tracks.append({'label': '--- Empty ---', 'value': 'Empty_3'})
    else:
        available_tracks += sorted(cmap_density, key=lambda k: k['label'])
        available_tracks.append({'label': '--- Contact Diff ---', 'value': 'Diff_Header', 'disabled': True})
        cmap_diff = get_cmap_diff_tracks(cmap_fname_list)
        if not cmap_diff:
            available_tracks.append({'label': '--- Empty ---', 'value': 'Empty_3'})
        else:
            available_tracks += sorted(cmap_diff, key=lambda k: k['label'])

    available_tracks.append({'label': '--- Other Tracks ---', 'value': 'AdditionalTracks_Header', 'disabled': True})
    other_tracks = get_other_tracks(session)
    if not other_tracks:
        available_tracks.append({'label': '--- Empty ---', 'value': 'Empty_4'})
    else:
        available_tracks += sorted(other_tracks, key=lambda k: k['label'])

    return available_tracks, sorted(available_cmaps)


def get_cmap_density_tracks(session):
    cmap_density = []
    available_cmaps = []
    cmap_fname_list = session[DatasetReference.CONTACT_MAP.value.encode()]
    for cmap_fname in cmap_fname_list:
        available_cmaps.append(cmap_fname)
        cmap_density.append({'label': cmap_fname, 'value': cmap_fname})
    return available_cmaps, cmap_fname_list, cmap_density


def get_cmap_diff_tracks(cmap_fname_list):
    cmap_diff = []
    for combination in itertools.combinations(cmap_fname_list, 2):
        label = '{} | {}'.format(*combination)
        cmap_diff.append({'label': label, 'value': label})
    return cmap_diff


def get_other_tracks(session):
    other_tracks = []
    for dataset in AdditionalDatasetReference:
        if dataset.value.encode() in session.keys() and session[dataset.value.encode()]:
            for fname in session[dataset.value.encode()]:
                other_tracks.append({'label': fname, 'value': fname})
    return other_tracks


def get_user_selection(cmap_selection, available_cmaps, track_selection, available_tracks):
    if len(cmap_selection) == 0:
        cmap_selection = ['--- Empty ---'] * 2
    else:
        cmap_selection = [fname if fname in available_cmaps else '--- Empty ---' for fname in cmap_selection]

    if len(track_selection) == 0:
        track_selection = ['--- Empty ---'] * 9
    else:
        available_track_labels = [track['label'] for track in available_tracks]
        track_selection = [track if track in available_track_labels else '--- Empty ---' for track in track_selection]

    return track_selection, cmap_selection


def get_default_layout(session):
    cmap_fname = session[DatasetReference.CONTACT_MAP.value.encode()][0]
    selected_palettes = ['PALETTE_1'] * len(color_palettes.DatasetColorPalettes)
    tracks = []

    for dataset in DefaultTrackLayout:
        if dataset.value in session.keys() and session[dataset.value]:
            tracks.append(session[dataset.value][0])

    if not any(tracks):
        return ['--- Empty ---'] * 9, (cmap_fname, cmap_fname), selected_palettes
    else:
        missing_tracks = ['--- Empty ---' for missing in range(0, 5 - len(tracks))]
        tracks += missing_tracks
        return tracks[1:][::-1] + tracks, (cmap_fname, cmap_fname), selected_palettes


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
            plot_bgcolor='rgba(0,0,0,0)'
        )
    )


def get_verbose_labels(session_id, session, fnames, display_settings, cache):
    sequence = session[display_settings.seq_fname.encode()]
    all_predictions = []
    for fname in set(fnames):
        dataset, prediction = tracks_utils.retrieve_dataset_prediction(session_id, session, fname,
                                                                       display_settings, cache)
        dataset_dict = STATES[dataset]
        prediction = [dataset_dict[x] for x in prediction]
        all_predictions.append(prediction)

    labels = []
    for idx, residue in enumerate(sequence, 1):
        current_label = '------<br>Residue {} ({})'.format(idx, residue)
        for prediction in all_predictions:
            current_label += '<br>{}'.format(prediction[idx - 1])
        labels.append(current_label)

    return labels
