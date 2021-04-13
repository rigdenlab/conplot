from parsers import DatasetStates
from loaders import AdditionalDatasetReference
from utils import create_cmap_trace, color_palettes


def get_dataset(session, fname):
    for dataset in AdditionalDatasetReference:
        if dataset.value.encode() in session.keys() and fname in session[dataset.value.encode()]:
            return dataset.value


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


def get_diagonal_trace(prediction, dataset, marker_size, sequence, alpha, color_palette):
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
            create_cmap_trace(x_diagonal, y, 'diamond', marker_size=marker_size, color=color, hovertext=hovertext)
        )

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

        traces.append(create_cmap_trace(x, y, 'diamond', marker_size=marker_size, color=color, hovertext=hovertext))

    return traces
