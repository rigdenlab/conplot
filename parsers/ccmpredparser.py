from operator import itemgetter
from utils.exceptions import InvalidFormat
from utils import unique_by_key


def CCMpredParser(input, input_format=None):
    contents = input.split('\n')

    output = []

    for res_1, line in enumerate(contents, 1):
        line = line.lstrip().split()
        if not line or line[0].isalpha() or len(line) == 1 or '#' in line[0]:
            continue

        for res_2, raw_score in enumerate(line, 1):
            try:
                raw_score = float(raw_score)
            except ValueError:
                raise InvalidFormat('Unable to parse contacts')
            if raw_score == '' or raw_score < 0.1:
                continue

            seq_distance = abs(res_1 - res_2)

            if seq_distance >= 5:
                contact = [res_1, res_2, raw_score]
                contact[:2] = sorted(contact[:2], reverse=True)
                output.append((tuple(contact[:2]), contact[2]))

    if not output:
        raise InvalidFormat('Unable to parse contacts')
    else:
        unique_contacts = unique_by_key(output, key=itemgetter(0))
        output = [(*contact[0], contact[1]) for contact in unique_contacts]
        output = sorted(output, key=itemgetter(2), reverse=True)
        return output
