import plotly.graph_objects as go
import numpy as np
from utils import color_palettes, DistanceLabels, HoverTemplates

DISTANCE_BINS = {0: 0, 1: 5, 2: 7, 3: 9, 4: 11, 5: 13, 6: 15, 7: 17, 8: 19, 9: 20}


def init_heatmap(seq_length):
    shape = (seq_length + 1, seq_length + 1)
    heat = np.zeros(shape)
    hover = np.full(shape, None)
    return heat, hover


def get_array(cmap, seq_length):
    array = np.full((seq_length + 1, seq_length + 1), 20)
    for contact in cmap:
        array[contact[0], contact[1]] = DISTANCE_BINS[contact[3]]
        array[contact[1], contact[0]] = DISTANCE_BINS[contact[3]]
    return array


def create_heatmap(session, display_settings, verbose_labels):
    heat, hover = init_heatmap(display_settings.seq_length)
    for idx, fname in enumerate(display_settings.cmap_selection):
        if fname == '--- Empty ---':
            continue
        heat, hover = populate_heatmap(session[fname.encode()], idx, heat, hover, verbose_labels)

    palette_idx = [x.value for x in color_palettes.PaletteDefaultLayout].index(b'heatmap')
    colorscale = color_palettes.get_heatmap_colorscale(display_settings.selected_palettes[palette_idx])
    return heat.tolist(), hover.tolist(), colorscale


def superimpose_heatmaps(session, display_settings, verbose_labels):
    heat, hover = create_superimposed_heatmap(session[display_settings.cmap_selection[0].encode()][1:],
                                              session[display_settings.cmap_selection[1].encode()][1:],
                                              display_settings.seq_length, verbose_labels)
    palette_idx = [x.value for x in color_palettes.PaletteDefaultLayout].index(b'heatmap')
    colorscale = color_palettes.get_heatmap_colorscale(display_settings.selected_palettes[palette_idx])
    return heat.tolist(), hover.tolist(), colorscale


def populate_heatmap(cmap, idx, heat, hover, verbose_labels=None):
    if idx == 1:
        idx_x = 1
        idx_y = 0
    else:
        idx_x = 0
        idx_y = 1

    hover_labels = []

    if cmap[0] == 'DISTO' or cmap[0] == 'PDB':
        cmap = cmap[1:]
        cmap_array = np.array(cmap)
        res_1 = cmap_array[:, idx_x]
        res_1 = res_1.astype(int)
        res_2 = cmap_array[:, idx_y]
        res_2 = res_2.astype(int)
        distances = cmap_array[:, 3]
        scores = cmap_array[:, 4]
        heat[res_1.astype(int), res_2.astype(int)] = 9 - distances

        if verbose_labels is not None:
            for x, y, distance, score in zip(res_1, res_2, distances.astype(int), scores):
                label = DistanceLabels.__getitem__(DistanceLabels, 'BIN_{}'.format(distance))
                hover_label = HoverTemplates.DISTOGRAM_VERBOSE.format(y, x, label, score, verbose_labels[y - 1],
                                                                      verbose_labels[x - 1])
                hover_labels.append(hover_label)

        else:
            for x, y, distance, score in zip(res_1, res_2, distances.astype(int), scores):
                label = DistanceLabels.__getitem__(DistanceLabels, 'BIN_{}'.format(distance))
                hover_label = HoverTemplates.DISTOGRAM.format(y, x, label, score)
                hover_labels.append(hover_label)

        hover[res_1.astype(int), res_2.astype(int)] = hover_labels

        return heat, hover

    cmap_array = np.array(cmap)
    res_1 = cmap_array[:, idx_x]
    res_1 = res_1.astype(int)
    res_2 = cmap_array[:, idx_y]
    res_2 = res_2.astype(int)
    scores = cmap_array[:, 2]
    heat[res_1, res_2] = scores

    if verbose_labels is None:
        for x, y, score in zip(res_1, res_2, scores):
            hover_labels.append(HoverTemplates.CMAP.format(y, x, score))

    else:
        for x, y, score in zip(res_1, res_2, scores):
            hover_label = HoverTemplates.CMAP_VERBOSE.format(y, x, score, verbose_labels[y - 1], verbose_labels[x - 1])
            hover_labels.append(hover_label)

    hover[res_1.astype(int), res_2.astype(int)] = hover_labels

    return heat, hover


def create_superimposed_heatmap(reference_cmap, predicted_cmap, seq_length, verbose_labels=None):
    hover = np.full((seq_length + 1, seq_length + 1), None)
    reference_array = get_array(reference_cmap, seq_length)
    predicted_array = get_array(predicted_cmap, seq_length)
    difference_heatmap = np.abs(reference_array - predicted_array)
    predicted_set = {(x[0], x[1]): x[3] for x in predicted_cmap}
    reference_set = {(x[0], x[1]): x[3] for x in reference_cmap}

    if verbose_labels is not None:
        for x in range(1, seq_length + 1):
            for y in range(x + 5, seq_length + 1):
                residues = (y, x)
                predicted_bin = predicted_set[residues] if residues in predicted_set.keys() else 9
                reference_bin = reference_set[residues] if residues in reference_set.keys() else 9
                error = '{} Å'.format(difference_heatmap[x, y])
                map_a_distance = DistanceLabels.__getitem__(DistanceLabels, 'BIN_{}'.format(reference_bin))
                map_b_distance = DistanceLabels.__getitem__(DistanceLabels, 'BIN_{}'.format(predicted_bin))
                hover_label_a = HoverTemplates.DISTOGRAM_SUPERIMPOSE_VERBOSE.format(y, x, map_a_distance,
                                                                                    map_b_distance, error,
                                                                                    verbose_labels[y - 1],
                                                                                    verbose_labels[x - 1])
                hover_label_b = HoverTemplates.DISTOGRAM_SUPERIMPOSE_VERBOSE.format(x, y, map_a_distance,
                                                                                    map_b_distance, error,
                                                                                    verbose_labels[x - 1],
                                                                                    verbose_labels[y - 1])
                hover[x, y] = hover_label_a
                hover[y, x] = hover_label_b
    else:
        for x in range(1, seq_length + 1):
            for y in range(x + 5, seq_length + 1):
                residues = (y, x)
                predicted_bin = predicted_set[residues] if residues in predicted_set.keys() else 9
                reference_bin = reference_set[residues] if residues in reference_set.keys() else 9
                error = '{} Å'.format(difference_heatmap[x, y])
                map_a_distance = DistanceLabels.__getitem__(DistanceLabels, 'BIN_{}'.format(reference_bin))
                map_b_distance = DistanceLabels.__getitem__(DistanceLabels, 'BIN_{}'.format(predicted_bin))
                hover_label_a = HoverTemplates.DISTOGRAM_SUPERIMPOSE.format(y, x, map_a_distance,
                                                                            map_b_distance, error)
                hover_label_b = HoverTemplates.DISTOGRAM_SUPERIMPOSE.format(x, y, map_a_distance,
                                                                            map_b_distance, error)
                hover[x, y] = hover_label_a
                hover[y, x] = hover_label_b

    return difference_heatmap, hover


def create_heatmap_trace(distances, colorscale, hovertext=None):
    return go.Heatmap(
        z=distances,
        hovertext=hovertext,
        colorscale=colorscale,
        hoverinfo='text' if hovertext is not None else 'none',
    )
