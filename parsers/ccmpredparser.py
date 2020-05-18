import numpy as np
from utils.exceptions import InvalidFormat
from operator import itemgetter

def CCMpredParser(input):
    contents = input.split('\n')
    output = []

    mat = np.loadtxt(contents)
    if mat.size > 0:
        contacts = mat.argsort(axis=None)[::-1]
        raw_contacts = (contacts % mat.shape[0]).astype(np.uint16), np.floor(contacts / mat.shape[0]).astype(np.uint16)


        for res1_seq, res2_seq, raw_score in zip(raw_contacts[0], raw_contacts[1], mat[raw_contacts]):
            if res1_seq > res2_seq:
                continue

            if abs((res1_seq) - int(res2_seq)) >= 5:
                output.append((int(res1_seq + 1), int(res2_seq + 1), float(raw_score)))

    if not output:
        raise InvalidFormat('Unable to parse contacts')
    else:
        output = sorted(output, key=itemgetter(2), reverse=True)
        return tuple(output)

