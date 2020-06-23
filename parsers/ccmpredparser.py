from utils.exceptions import InvalidFormat
from operator import itemgetter


def CCMpredParser(input):
    contents = input.split('\n')

    output = []
    contacts_cache = []

    for res_1, line in enumerate(contents, 1):
        line = line.lstrip().split()
        if not line or line[0].isalpha() or len(line) == 1:
            continue

        for res_2, raw_score in enumerate(line, 1):
            if raw_score == '' or float(raw_score) < 0.1:
                continue
            elif (res_1 - res_2) >= 5 and (res_1, res_2) not in contacts_cache:
                output.append((int(res_1), int(res_2), float(raw_score)))
                contacts_cache.append((res_1, res_2))
            elif (res_2 - res_1) >= 5 and (res_2, res_1) not in contacts_cache:
                output.append((int(res_2), int(res_1), float(raw_score)))
                contacts_cache.append((res_2, res_1))

    if not output:
        raise InvalidFormat('Unable to parse contacts')
    else:
        output = sorted(output, key=itemgetter(2), reverse=True)
        return output
