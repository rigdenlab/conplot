from parsers import DatasetStates
from loaders import AdditionalDatasetReference, DatasetReference
from utils import create_cmap_trace, color_palettes, cache_utils
from sklearn.cluster import estimate_bandwidth
from sklearn.neighbors import KernelDensity
import numpy as np


def calculate_density(cmap, seq_length, factor):
    if cmap[-1] == 'PDB' or cmap[-1] == 'DISTO':
        cmap.pop(-1)
    contact_list = cmap[:int(round(seq_length / factor, 0))]
    return get_contact_density(contact_list, seq_length)


def retrieve_dataset_prediction(session_id, session, fname, display_settings, cache):
    if cache_utils.MetadataTags.HYDROPHOBICITY.value in fname:
        return DatasetReference.HYDROPHOBICITY.value, session[DatasetReference.HYDROPHOBICITY.value.encode()]

    if cache_utils.MetadataTags.DENSITY.value in fname:
        fname = fname[:-len(cache_utils.MetadataTags.DENSITY.value)]
        cachekey = cache_utils.CacheKeys.CMAP_DENSITY.value.format(fname, display_settings.factor).encode()
        if cachekey in session.keys():
            density = session[cachekey]
        elif cache.hexists(session_id, cachekey):
            density = cache_utils.retrieve_density(session_id, cachekey, cache)
        else:
            density = calculate_density(session[fname.encode()], display_settings.seq_length, display_settings.factor)
            cache_utils.store_density(session_id, cachekey, density, cache)
        return DatasetReference.CONTACT_DENSITY.value, density

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


def get_contact_density(contact_list, seq_length):
    """Credits to Felix Simkovic; code taken from GitHub rigdenlab/conkit/core/contactmap.py"""
    x = np.array([i for c in contact_list for i in np.arange(c[1], c[0] + 1)], dtype=np.int64)[:, np.newaxis]
    bw = estimate_bandwidth(x)
    kde = KernelDensity(bandwidth=bw).fit(x)
    x_fit = np.arange(1, seq_length + 1)[:, np.newaxis]
    density = np.exp(kde.score_samples(x_fit)).tolist()
    density_max = max(density)
    density = [int(round(float(i) / density_max, 1) * 10) for i in density]
    return density
