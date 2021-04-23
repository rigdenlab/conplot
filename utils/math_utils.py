from conkit.misc.bandwidth import bandwidth_factory
import math
from numba import njit, vectorize
import numpy as np
from sklearn.neighbors import KernelDensity


@njit()
def calculate_mcc(tp, fp, tn, fn):
    denominator = (tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)
    denominator = math.sqrt(denominator)
    if denominator == 0:
        return 1
    numerator = (tp * tn - fp * fn) * 10
    if numerator < 0:
        return 10
    mcc = 10 - (numerator / denominator)
    return mcc


@vectorize('float64(int64, int64)')
def get_difference(expected, observed):
    difference = expected - observed
    difference_squared = difference ** 2
    return difference_squared


@njit()
def calculate_rmsd(expected_array, observed_array):
    squared_differences = get_difference(expected_array, observed_array)
    rmsd = np.sum(squared_differences) / observed_array.shape[0]
    return rmsd


def get_contact_density(contact_list, seq_length):
    """Credits to Felix Simkovic; code taken from GitHub rigdenlab/conkit"""
    x = np.array([i for c in contact_list for i in np.arange(c[1], c[0] + 1)], dtype=np.int64)[:, np.newaxis]
    bw = bandwidth_factory('amise')(x).bw
    kde = KernelDensity(bandwidth=bw).fit(x)
    x_fit = np.arange(1, seq_length + 1)[:, np.newaxis]
    density = np.exp(kde.score_samples(x_fit)).tolist()
    density_max = max(density)
    density = [int(round(float(i) / density_max, 1) * 10) for i in density]
    return density
