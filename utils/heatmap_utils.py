import plotly.graph_objects as go
import numpy as np
from utils import color_palettes, DistanceLabels, HoverTemplates


def init_heatmap(seq_length):
    shape = (seq_length + 1, seq_length + 1)
    heat = np.zeros(shape).tolist()
    hover = np.full(shape, None).tolist()
    return heat, hover


def create_heatmap(session, display_settings, verbose_labels):
    heat, hover = init_heatmap(display_settings.seq_length)
    for idx, fname in enumerate(display_settings.cmap_selection):
        if fname == '--- Empty ---':
            continue
        heat, hover = populate_heatmap(session[fname.encode()], idx, heat, hover, verbose_labels)

    palette_idx = [x.value for x in color_palettes.PaletteDefaultLayout].index(b'heatmap')
    colorscale = color_palettes.get_heatmap_colorscale(display_settings.selected_palettes[palette_idx])
    return heat, hover, colorscale


def superimpose_heatmaps(session, display_settings, verbose_labels):
    heat, hover = init_heatmap(display_settings.seq_length)
    for idx, fname in enumerate(display_settings.cmap_selection):
        if fname == '--- Empty ---':
            continue
        heat, hover = populate_superimposed_heatmap(session[display_settings.cmap_selection[0].encode()],
                                                    session[display_settings.cmap_selection[1].encode()],
                                                    heat, hover, verbose_labels)
    palette_idx = [x.value for x in color_palettes.PaletteDefaultLayout].index(b'heatmap')
    colorscale = color_palettes.get_heatmap_colorscale(display_settings.selected_palettes[palette_idx])
    return heat, hover, colorscale


def populate_heatmap(cmap, idx, distances, hover, verbose_labels=None):
    if idx == 1:
        idx_x = 1
        idx_y = 0
    else:
        idx_x = 0
        idx_y = 1

    if cmap[0] == 'DISTO' or cmap[0] == 'PDB':
        cmap = cmap[1:]

        if verbose_labels is not None:
            for contact in cmap:
                distances[contact[idx_x]][contact[idx_y]] = 9 - contact[3]
                label = DistanceLabels.__getitem__(DistanceLabels, 'BIN_{}'.format(contact[3]))
                hover_label = HoverTemplates.DISTOGRAM_VERBOSE.format(contact[idx_y], contact[idx_x], label, contact[4],
                                                                      verbose_labels[contact[idx_y] - 1],
                                                                      verbose_labels[contact[idx_x] - 1])
                hover[contact[idx_x]][contact[idx_y]] = hover_label
        else:
            for contact in cmap:
                distances[contact[idx_x]][contact[idx_y]] = 9 - contact[3]
                label = DistanceLabels.__getitem__(DistanceLabels, 'BIN_{}'.format(contact[3]))
                hover_label = HoverTemplates.DISTOGRAM.format(contact[idx_y], contact[idx_x], label, contact[4])
                hover[contact[idx_x]][contact[idx_y]] = hover_label

        return distances, hover

    if verbose_labels is None:
        for contact in cmap:
            distances[contact[idx_x]][contact[idx_y]] = contact[2]
            hover_label = HoverTemplates.CMAP.format(contact[idx_y], contact[idx_x], contact[2])
            hover[contact[idx_x]][contact[idx_y]] = hover_label

    else:
        for contact in cmap:
            distances[contact[idx_x]][contact[idx_y]] = contact[2]
            hover_label = HoverTemplates.CMAP_VERBOSE.format(contact[idx_y], contact[idx_x], contact[2],
                                                             verbose_labels[contact[idx_y] - 1],
                                                             verbose_labels[contact[idx_x] - 1])
            hover[contact[idx_x]][contact[idx_y]] = hover_label

    return distances, hover


def populate_superimposed_heatmap(reference_cmap, secondary_cmap, heat, hover, verbose_labels=None):
    idx_x = 1
    idx_y = 0
    reference_cmap = reference_cmap[1:]
    secondary_cmap = secondary_cmap[1:]
    predicted_set = {(x[0], x[1]): x[3] for x in secondary_cmap}

    if verbose_labels is not None:
        for reference_distance in reference_cmap:
            residues = tuple(reference_distance[:2])
            predicted_bin = predicted_set[residues] if residues in predicted_set.keys() else 9
            reference_bin = reference_distance[3]
            error = abs((9 - reference_bin) - (9 - predicted_bin))
            resid_y = reference_distance[idx_y]
            resid_x = reference_distance[idx_x]
            heat[resid_x][resid_y] = error
            heat[resid_y][resid_x] = error
            map_a_distance = DistanceLabels.__getitem__(DistanceLabels, 'BIN_{}'.format(reference_bin))
            map_b_distance = DistanceLabels.__getitem__(DistanceLabels, 'BIN_{}'.format(predicted_bin))
            hover_label_a = HoverTemplates.DISTOGRAM_SUPERIMPOSE_VERBOSE.format(resid_y, resid_x, map_a_distance,
                                                                                map_b_distance, error,
                                                                                verbose_labels[resid_y - 1],
                                                                                verbose_labels[resid_x - 1])
            hover_label_b = HoverTemplates.DISTOGRAM_SUPERIMPOSE_VERBOSE.format(resid_x, resid_y, map_a_distance,
                                                                                map_b_distance, error,
                                                                                verbose_labels[resid_x - 1],
                                                                                verbose_labels[resid_y - 1])
            hover[resid_x][resid_y] = hover_label_a
            hover[resid_y][resid_x] = hover_label_b
    else:
        for reference_distance in reference_cmap:
            residues = tuple(reference_distance[:2])
            predicted_bin = predicted_set[residues] if residues in predicted_set.keys() else 9
            reference_bin = reference_distance[3]
            error = abs((9 - reference_bin) - (9 - predicted_bin))
            resid_y = reference_distance[idx_y]
            resid_x = reference_distance[idx_x]
            heat[resid_x][resid_y] = error
            heat[resid_y][resid_x] = error
            map_a_distance = DistanceLabels.__getitem__(DistanceLabels, 'BIN_{}'.format(reference_bin))
            map_b_distance = DistanceLabels.__getitem__(DistanceLabels, 'BIN_{}'.format(predicted_bin))
            hover_label_a = HoverTemplates.DISTOGRAM_SUPERIMPOSE.format(resid_y,  resid_x, map_a_distance,
                                                                        map_b_distance, error)
            hover_label_b = HoverTemplates.DISTOGRAM_SUPERIMPOSE.format(resid_x, resid_y, map_a_distance,
                                                                        map_b_distance, error)
            hover[resid_x][resid_y] = hover_label_a
            hover[resid_y][resid_x] = hover_label_b

    return heat, hover


def create_heatmap_trace(distances, colorscale, hovertext=None):
    return go.Heatmap(
        z=distances,
        hovertext=hovertext,
        colorscale=colorscale,
        hoverinfo='text' if hovertext is not None else 'none',
    )
