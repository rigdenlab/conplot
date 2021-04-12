import io
import base64
import numpy as np
from utils.exceptions import InvalidFormat
from utils import get_unique_distances


def parse_array(array):
    # Bin #0 corresponds with d>20A
    # Bins #1 ~ #36 correspond with 2A<d<20A in increments of 0.5A
    contacts = np.sum(array[:, :, 1:13], axis=-1)
    L = contacts.shape[0]
    BINS = [np.sum(array[:, :, x:x+4], axis=-1) for x in range(1, 37, 4)]
    BINS.append(array[:, :, 0].copy())
    array = np.dstack(BINS)
    dist_bins = np.nanargmax(array, axis=2)
    dist_prob = np.amax(array, axis=2)
    return [[i + 1, j + 1, float(contacts[i, j]), int(dist_bins[i, j]), float(dist_prob[i, j])]
            for i in range(L) for j in range(i + 5, L)]


def NpzParser(input, input_format=None):
    output = []
    content_type, content_string = input.split(',')
    try:
        decoded = base64.b64decode(content_string)
        archive = np.load(io.BytesIO(decoded), allow_pickle=True)
        array = archive['dist']
        tmp_output = parse_array(array)
    except (OSError, KeyError, IndexError) as e:
        raise InvalidFormat('Unable to parse distance NPZ file')

    for contact in tmp_output:
        # contact = [res_1, res_2, raw_score, distance_bin, distance_score]
        contact[:2] = sorted(contact[:2], reverse=True)
        output.append((tuple(contact[:2]), *contact[2:]))

    if not output:
        raise InvalidFormat('Unable to parse NPZ file')
    else:
        unique_contacts = get_unique_distances(output)
        return unique_contacts
