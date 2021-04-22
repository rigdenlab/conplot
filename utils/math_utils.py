import math
from numba import njit
import numpy as np
from sklearn.neighbors import KernelDensity

"""Credits to Felix Simkovic; code taken from GitHub rigdenlab/conkit"""
"""Credits to Felix Simkovic; code taken from GitHub rigdenlab/conkit"""

SQRT_PI = math.sqrt(math.pi)
SQRT_2PI = math.sqrt(2.0 * math.pi)


@njit(fastmath=True)
def calculate_mcc(tp, fp, tn, fn):
    denominator = (tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)
    denominator = np.sqrt(denominator)
    if denominator == 0:
        return 1
    numerator = (tp * tn - fp * fn) * 10
    if numerator < 0:
        return 10
    mcc = 10 - (numerator / denominator)
    return mcc


@njit(fastmath=True)
def calculate_bowman_bw(data):
    M, N = data.shape
    bw = math.sqrt((data ** 2).sum() / M - (data.sum() / M) ** 2) * ((((N + 2) * M) / 4.0) ** (-1.0 / (N + 4)))
    return bw


@njit(fastmath=True)
def calculate_amise_bw(data, n_iterations=25, eps=0.001):
    data = np.asarray(data)
    x0 = calculate_bowman_bw(data)
    y0 = optimize_bandwidth(data, x0)
    x = 0.8 * x0
    y = optimize_bandwidth(data, x)
    for i in range(n_iterations):
        x = x - (y * (x0 - x) / (y0 - y))
        y = optimize_bandwidth(data, x)
        if abs(y) < (eps * y0):
            break
    return x


@njit(cache=True, fastmath=True)
def optimize_bandwidth(A, v):
    alpha = 1.0 / (2.0 * SQRT_PI)
    sigma = 1.0
    integral = get_stiffness_integral(A, v, 0.0001)
    result = v - ((A.shape[0] * integral * sigma ** 4) / alpha) ** (-1.0 / (A.shape[1] + 4))
    return result


@njit(fastmath=True)
def get_stiffness_integral(A, v, eps):
    min_ = A.min() - v * 3
    max_ = A.max() + v * 3
    dx = 1.0 * (max_ - min_)
    maxn = dx / math.sqrt(eps)
    if maxn > 2048:
        maxn = 2048
    y1 = get_gauss_curvature(A, min_, v)
    y2 = get_gauss_curvature(A, max_, v)
    yy = 0.5 * dx * (y1 * y1 + y2 * y2)
    n = 2

    while n <= maxn:
        dx = dx / 2.0
        y = 0.0
        for i in range(1, n, 2):
            y3 = get_gauss_curvature(A, min_ + i * dx, v)
            y = y + (y3 * y3)
        yy = 0.5 * yy + y * dx
        if n > 8 and math.fabs(y * dx - 0.5 * yy) < eps * yy:
            break
        n = n * 2

    return yy


@njit(cache=True, fastmath=True)
def get_gauss_curvature(A, x, w):
    w_sq = w * w
    w_sqrt_2pi = w * SQRT_2PI
    curvature = 0.0
    shape_1 = A.shape[1]
    for i in range(A.shape[0]):
        for j in range(shape_1):
            z = (x - A[i, j]) / w
            z = z * z
            curvature = curvature + (shape_1 * (z - 1.0) * (math.exp(-0.5 * z) / w_sqrt_2pi) / w_sq)
    return curvature / A.shape[0]


def get_contact_density(contact_list, seq_length):
    x = np.array([i for c in contact_list for i in np.arange(c[1], c[0] + 1)], dtype=np.int64)[:, np.newaxis]
    bw = calculate_amise_bw(x)
    kde = KernelDensity(bandwidth=bw).fit(x)
    x_fit = np.arange(1, seq_length + 1)[:, np.newaxis]
    density = np.exp(kde.score_samples(x_fit)).tolist()
    density_max = max(density)
    density = [int(round(float(i) / density_max, 1) * 10) for i in density]
    return density
