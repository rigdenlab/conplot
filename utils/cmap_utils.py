import plotly.graph_objects as go
from utils import HoverTemplates


def create_cmap_trace(x, y, symbol, marker_size, color, hovertext=None):
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


def create_cmap(cmap, idx, display_settings, verbose_labels=None):

    if cmap[-1] == 'PDB' or cmap[-1] == 'DISTO':
        print('CREATE CMAP')
        print('DELETEEEE')
        del cmap[-1]

    if display_settings.factor != 0:
        cmap = cmap[:int(round(display_settings.seq_length / display_settings.factor, 0))]

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
        for contact in cmap:
            res1_list.append(contact[idx_x])
            res2_list.append(contact[idx_y])
            res_x_label = verbose_labels[contact[idx_x] - 1]
            res_y_label = verbose_labels[contact[idx_y] - 1]
            hover.append(HoverTemplates.CMAP_VERBOSE.format(contact[idx_x], contact[idx_y], contact[2],
                                                            res_x_label, res_y_label))
    else:
        for contact in cmap:
            res1_list.append(contact[idx_x])
            res2_list.append(contact[idx_y])
            hover.append(HoverTemplates.CMAP.format(contact[idx_x], contact[idx_y], contact[2]))

    return res1_list, res2_list, hover


def superimpose_cmaps(reference_cmap, predicted_cmap, display_settings):

    if display_settings.factor != 0:
        predicted_cmap = predicted_cmap[:int(round(display_settings.seq_length / display_settings.factor, 0))]
        if reference_cmap[-1] == 'PDB':
            del reference_cmap[-1]
            reference_cmap = [contact for contact in reference_cmap if contact[2] > 0]
        elif reference_cmap[-1] == 'DISTO':
            del reference_cmap[-1]
            reference_cmap = reference_cmap[:int(round(display_settings.seq_length / display_settings.factor, 0))]
        else:
            reference_cmap = reference_cmap[:int(round(display_settings.seq_length / display_settings.factor, 0))]
    elif reference_cmap[-1] == 'PDB' or reference_cmap[-1] == 'DISTO':
        del reference_cmap[-1]

    reference_contacts = [contact[:2] for contact in reference_cmap]
    predicted_contacts = [contact[:2] for contact in predicted_cmap]

    matched = []
    mismatched = []
    reference = []

    for contact in reference_cmap:
        if contact[:2] in predicted_contacts:
            matched.append(contact)
        else:
            reference.append(contact)

    for contact in predicted_cmap:
        if contact[:2] not in reference_contacts:
            mismatched.append(contact)

    return reference, matched, mismatched


def create_superimposed_cmap(contacts, verbose_labels):
    res1_list = []
    res2_list = []
    hover_1 = []
    hover_2 = []

    if verbose_labels is not None:
        for contact in contacts:
            res1_list.append(contact[0])
            res2_list.append(contact[1])
            res_1_label = verbose_labels[contact[0] - 1]
            res_2_label = verbose_labels[contact[1] - 1]
            hover_1.append(HoverTemplates.CMAP_VERBOSE.format(contact[0], contact[1], contact[2],
                                                              res_1_label, res_2_label))
            hover_2.append(HoverTemplates.CMAP_VERBOSE.format(contact[1], contact[0], contact[2],
                                                              res_2_label, res_1_label))
    else:
        for contact in contacts:
            res1_list.append(contact[0])
            res2_list.append(contact[1])
            hover_1.append(HoverTemplates.CMAP.format(contact[0], contact[1], contact[2]))
            hover_2.append(HoverTemplates.CMAP.format(contact[1], contact[0], contact[2]))

    x = res1_list + res2_list
    y = res2_list + res1_list
    hovertext = hover_1 + hover_2

    return x, y, hovertext


def get_contact_density(contact_list, sequence_range, normalize=True):
    """Credits to Felix Simkovic; code taken from GitHub rigdenlab/conkit/core/contactmap.py"""
    from sklearn.cluster import estimate_bandwidth
    from sklearn.neighbors import KernelDensity
    import numpy as np
    x = np.array([i for c in contact_list for i in np.arange(c[0], c[1] + 1)], dtype=np.int64)[:, np.newaxis]
    bw = estimate_bandwidth(x)
    kde = KernelDensity(bw).fit(x)
    x_fit = np.arange(sequence_range.min(), sequence_range.max() + 1)[:, np.newaxis]
    density = np.exp(kde.score_samples(x_fit)).tolist()

    if normalize:
        return [float(i) / max(density) for i in density]
    else:
        return density
