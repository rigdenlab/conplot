import numpy as np
from loaders import AdditionalDatasetReference, DatasetReference
from parsers import DatasetStates
from utils import create_cmap_trace, color_palettes, cache_utils, lookup_data, cmap_utils, math_utils


def calculate_density(cmap, seq_length, factor):
    contact_list = cmap_utils.slice_cmap(cmap, seq_length, factor)
    return math_utils.get_contact_density(contact_list, seq_length)


DISTANCE_BINS = {0: 0, 1: 5, 2: 7, 3: 9, 4: 11, 5: 13, 6: 15, 7: 17, 8: 19, 9: 20}


def get_distance_array(cmap, seq_length):
    array = np.full((seq_length, seq_length), 20)
    for contact in cmap:
        array[seq_length - contact[0], contact[1] - 1] = DISTANCE_BINS[contact[3]]
        array[seq_length - contact[1], contact[0] - 1] = DISTANCE_BINS[contact[3]]
    return array


def get_cmap_mcc(cmap_1, cmap_2, size):
    cmap_1_set = {resn: {(c[0], c[1]) for c in cmap_1 if resn in (c[0], c[1])} for resn in range(1, size + 1)}
    cmap_2_set = {resn: {(c[0], c[1]) for c in cmap_2 if resn in (c[0], c[1])} for resn in range(1, size + 1)}
    diff = []

    for resn in cmap_1_set.keys():
        tp = len(cmap_1_set[resn] & cmap_2_set[resn])
        fp = len(cmap_2_set[resn] - cmap_1_set[resn])
        fn = len(cmap_1_set[resn] - cmap_2_set[resn])
        tn = size - sum((tp, fp, fn))
        mcc = math_utils.calculate_mcc(tp, fp, tn, fn)
        diff.append(int(round(mcc, 0)))

    return diff


def get_cmap_rmsd(cmap_1, cmap_2, seq_length):
    cmap_1_array = get_distance_array(cmap_1, seq_length)
    cmap_2_array = get_distance_array(cmap_2, seq_length)
    rmsd = math_utils.calculate_rmsd(cmap_1_array, cmap_2_array, seq_length)
    return rmsd.astype(int).tolist()


def calculate_diff(cmap_1, cmap_2, display_settings):
    if cmap_utils.contains_distances(cmap_1) and cmap_utils.contains_distances(cmap_2):
        cmap_1 = cmap_utils.slice_cmap(cmap_1, display_settings.seq_length, 0)
        cmap_2 = cmap_utils.slice_cmap(cmap_2, display_settings.seq_length, 0)
        return get_cmap_rmsd(cmap_1, cmap_2, display_settings.seq_length)
    else:
        cmap_1 = cmap_utils.slice_cmap(cmap_1, display_settings.seq_length, display_settings.factor)
        cmap_2 = cmap_utils.slice_cmap(cmap_2, display_settings.seq_length, display_settings.factor)
        return get_cmap_mcc(cmap_1, cmap_2, display_settings.seq_length)


def get_diff_args(fname, factor):
    cmap_1 = fname.split('|')[0].rstrip().lstrip()
    cmap_2 = fname.split('|')[1].rstrip().lstrip()
    cachekey = cache_utils.CacheKeys.CMAP_DIFF.value.format(cmap_1, cmap_2, factor).encode()
    return cmap_1, cmap_2, cachekey


def retrieve_dataset_prediction(session_id, session, fname, display_settings, cache):
    if fname == session[DatasetReference.SEQUENCE.value.encode()]:
        return DatasetReference.HYDROPHOBICITY.value, session[DatasetReference.HYDROPHOBICITY.value.encode()]

    # TODO: If it is a PDB lookup data should not care about the L factor since it will always be the same
    if fname in session[DatasetReference.CONTACT_MAP.value.encode()]:
        cachekey = cache_utils.CacheKeys.CMAP_DENSITY.value.format(fname, display_settings.factor).encode()
        density = lookup_data(session, session_id, cachekey, cache)
        if not density:
            density = calculate_density(session[fname.encode()], display_settings.seq_length, display_settings.factor)
            cache_utils.store_data(session_id, cachekey, density, cache_utils.CacheKeys.CONTACT_DENSITY.value, cache)

        return DatasetReference.CONTACT_DENSITY.value, density

    # TODO: If looking for diff for distance predictions, we also don't care about L factor (using all)
    if cache_utils.MetadataTags.SEPARATOR.value in fname:
        cmap_1, cmap_2, cachekey = get_diff_args(fname, display_settings.factor)
        diff = lookup_data(session, session_id, cachekey, cache)
        if not diff:
            cmap_1 = session[cmap_1.encode()]
            cmap_2 = session[cmap_2.encode()]
            diff = calculate_diff(cmap_1, cmap_2, display_settings)
            cache_utils.store_data(session_id, cachekey, diff, cache_utils.CacheKeys.CONTACT_DIFF.value, cache)
        return DatasetReference.CONTACT_DIFF.value, diff

    for dataset in AdditionalDatasetReference:
        if dataset.value.encode() in session.keys() and fname in session[dataset.value.encode()]:
            return dataset.value, session[fname.encode()]


def transform_coords_diagonal_xaxis(indices, distance, track_idx, ratio=1):
    factor = distance / (1 + ratio ** 2)
    if track_idx < 4:
        factor = factor * -1
    return [idx + factor for idx in indices]


def transform_coords_diagonal_yaxis(prediction, state, distance, track_idx, ratio=1):
    factor = ratio * (distance / (1 + ratio ** 2))
    if track_idx > 4:
        factor = factor * -1
    return [idx + factor if residue == state else None for idx, residue in enumerate(prediction, 1)]


def get_diagonal_trace(prediction, dataset, marker_size, sequence, alpha, color_palette):
    if prediction is None:
        return None

    x = [idx for idx in range(1, len(prediction) + 1)]
    states = DatasetStates.__getattr__(dataset).value
    palette = color_palettes.DatasetColorPalettes.__getattr__(dataset).value.__getattr__(color_palette).value
    traces = []

    for state in states:
        y = [idx if residue == state.value else None for idx, residue in enumerate(prediction, 1)]
        if not any(y):
            continue
        hovertext = ['Residue: {} ({}) | {}'.format(resid, idx, state.name) for idx, resid in enumerate(sequence, 1)]
        color = palette.__getattr__(state.name).value.format(alpha)
        traces.append(create_cmap_trace(x, y, 'diamond', marker_size=marker_size, color=color, hovertext=hovertext))

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

    x = transform_coords_diagonal_xaxis(x_diagonal, track_distance, track_idx)

    for state in states:
        y = transform_coords_diagonal_yaxis(prediction, state.value, track_distance, track_idx)
        if not any(y):
            continue
        hovertext = ['%s' % state.name for i in x]
        color = palette.__getattr__(state.name).value.format(alpha)

        traces.append(create_cmap_trace(x, y, 'diamond', marker_size=marker_size, color=color, hovertext=hovertext))

    return traces
