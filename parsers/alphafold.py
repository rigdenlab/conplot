import io
import base64
import numpy as np
from scipy.special import softmax
from utils.exceptions import InvalidFormat
from parsers import get_unique_distances


def parse_distogram(distogram):
    # Output are raw logits rather than probabilities, apply softmax
    probs = softmax(distogram['logits'], axis=-1)
    assert probs.shape[-1] == 64
    # Bin edges represent interval boundaries, which are half-open (open on the left) (hence n-1 bin edges)
    assert distogram['bin_edges'].shape[-1] == 63
    assert distogram['bin_edges'][1] - distogram['bin_edges'][0] == 0.3125
    contacts = np.sum(probs[:, :, :19], axis=-1)
    L = contacts.shape[0]
    BINS = [np.sum(probs[:, :, :6], axis=-1)]
    BINS += [np.sum(probs[:, :, int((x * 2 + 0.0125) / 0.3125):int((x * 2 + 2.0125) / 0.3125)], axis=-1) for x in
             range(1, 9)]
    BINS.append(np.sum(probs[:, :, 57:], axis=-1))
    array = np.dstack(BINS)
    dist_bins = np.nanargmax(array, axis=2)
    dist_prob = np.amax(array, axis=2)
    return [[i + 1, j + 1, float(contacts[i, j]), int(dist_bins[i, j]), float(dist_prob[i, j])]
            for i in range(L) for j in range(i + 5, L)]


def AlphafoldParser(input, input_format=None):
    output = []
    content_type, content_string = input.split(',')
    try:
        decoded = base64.b64decode(content_string)
        results = np.load(io.BytesIO(decoded), allow_pickle=True)
        distogram = results['distogram']
        tmp_output = parse_distogram(distogram)
    except (OSError, KeyError, IndexError) as e:
        raise InvalidFormat('Unable to parse alphafold pkl file')

    for contact in tmp_output:
        # contact = [res_1, res_2, raw_score, distance_bin, distance_score]
        contact[:2] = sorted(contact[:2], reverse=True)
        output.append((tuple(contact[:2]), *contact[2:]))

    if not output:
        raise InvalidFormat('Unable to parse alphafold pkl file')
    else:
        unique_contacts = get_unique_distances(output)
        if any([p for p in unique_contacts[1:] if p[3] > 9 or p[4] > 1.01]):
            raise InvalidFormat('Unable to parse alphafold pkl file')
        return unique_contacts
