from parsers import get_unique_distances
from utils.exceptions import InvalidFormat


def MappredParser(input, input_format=None):
    contents = input.split('\n')
    output = []
    res_1_idx = 0
    res_2_idx = 1
    line_size = 36

    for idx, line in enumerate(contents):

        line = line.lstrip().rstrip().split()

        if not line or len(line) < line_size or not line[res_1_idx].isdigit() or not line[res_2_idx].isdigit():
            continue

        res_1 = int(line[res_1_idx])
        res_2 = int(line[res_2_idx])
        seq_distance = res_1 - res_2

        if abs(seq_distance) >= 5:
            line = [float(prob) for prob in line[2:]]
            raw_score = sum([prob for prob in line[:9]])
            distance_probabilities = [line[0]]
            distance_probabilities += [sum(line[x:x+4]) for x in range(1, 30, 4)]
            distance_probabilities.append(line[-1])
            distance_score = max(distance_probabilities)
            distance_bin = distance_probabilities.index(distance_score)
            contact = [res_1, res_2, raw_score, distance_bin, distance_score]
            contact[:2] = sorted(contact[:2], reverse=True)
            output.append((tuple(contact[:2]), *contact[2:]))

    if not output:
        raise InvalidFormat('Unable to parse MapPred file')
    else:
        unique_contacts = get_unique_distances(output)
        return unique_contacts
