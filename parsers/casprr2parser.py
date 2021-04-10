from operator import itemgetter
from utils import unique_by_key
from utils.exceptions import InvalidFormat


def CASPRR2Parser(input, input_format=None):
    contents = input.split('\n')
    output = []
    res_1_idx = 0
    res_2_idx = 1
    raw_score_idx = 2
    line_size = 13

    for idx, line in enumerate(contents):

        line = line.lstrip().rstrip().split()

        if not line or len(line) < line_size or not line[res_1_idx].isdigit() or not line[res_2_idx].isdigit():
            continue

        res_1 = int(line[res_1_idx])
        res_2 = int(line[res_2_idx])
        seq_distance = res_1 - res_2

        if abs(seq_distance) >= 5:
            raw_score = float(line[raw_score_idx])
            distance_probabilities = [float(p) for p in line[raw_score_idx + 1:]]
            distance_score = max(distance_probabilities)
            distance_bin = distance_probabilities.index(distance_score)
            contact = [res_1, res_2, raw_score, distance_bin, distance_score]
            contact[:2] = sorted(contact[:2], reverse=True)
            output.append((tuple(contact[:2]), *contact[2:]))

    if not output:
        raise InvalidFormat('Unable to parse CASPRR_MODE_2 file')
    else:
        unique_contacts = unique_by_key(output, key=itemgetter(0))
        output = [(*contact[0], *contact[1:]) for contact in unique_contacts]
        output = sorted(output, key=itemgetter(2), reverse=True)
        output.append('DISTO')
        return output
