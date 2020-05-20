from utils.exceptions import InvalidFormat
from operator import itemgetter


def ColstatsParser(input):
    contents = input.split('\n')

    output = []

    data = []
    for line in contents:
        line = line.lstrip().split(' ')
        print(line)
        if not line or line[0].isalpha() or len(line) == 1:
            continue
        else:
            data.append(line)

    for res_1, score_array in enumerate(data, 1):
        for res_2, score in enumerate(score_array, 1):
            if abs((res_1) - int(res_2)) >= 5 and score != '' and float(score) > 0:
                output.append((int(res_1), int(res_2), float(score)))

    if not output:
        raise InvalidFormat('Unable to parse contacts')
    else:
        output = sorted(output, key=itemgetter(2), reverse=True)
        return output



