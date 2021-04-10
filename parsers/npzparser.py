import io
import base64
import numpy as np
from operator import itemgetter
from utils.exceptions import InvalidFormat
from utils import unique_by_key


def parse_array(array):
    contacts = np.sum(array[:, :, 1:13], axis=-1)
    L = contacts.shape[0]
    BINS = [np.sum(array[:, :, x:x+4], axis=-1) for x in range(1, 37, 4)]
    BINS.append(array[:, :, 0].copy())
    array = np.dstack(BINS)
    dist_bins = np.nanargmax(array, axis=2)
    dist_prob = np.amax(array, axis=2)
    return [[i + 1, j + 1, float(contacts[i, j]), int(dist_bins[i, j]), float(dist_prob[i, j])]
            for i in range(L) for j in range(i + 5, L)]


def NpzParser(input, input_format):
    output = []
    content_type, content_string = input.split(',')
    decoded = base64.b64decode(content_string)
    archive = np.load(io.BytesIO(decoded), allow_pickle=True)
    array = archive['dist']
    # Bin #0 corresponds with d>20A
    # Bins #1 ~ #36 correspond with 2A<d<20A in increments of 0.5A
    tmp_output = parse_array(array)

    for contact in tmp_output:
        # contact = [res_1, res_2, raw_score, distance_bin, distance_score]
        contact[:2] = sorted(contact[:2], reverse=True)
        output.append((tuple(contact[:2]), *contact[2:]))

    if not output:
        raise InvalidFormat('Unable to parse contacts')
    else:
        unique_contacts = unique_by_key(output, key=itemgetter(0))
        output = [(*contact[0], *contact[1:]) for contact in unique_contacts]
        output = sorted(output, key=itemgetter(2), reverse=True)
        output.append('DISTO')
        return output
