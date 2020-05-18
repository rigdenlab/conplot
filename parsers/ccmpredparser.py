from utils.exceptions import InvalidFormat
from operator import itemgetter

def CCMpredParser(input):
    contents = input.split('\n')

    output = []

    data = []
    for line in contents:
        line = line.lstrip().split('\t')
        if not line or line[0].isalpha():
            continue
        else:
            data.append(line)

    for res_1, score_array in enumerate(data):
        for res_2, score in enumerate(score_array):
            if abs((res_1+1) - int(res_2+1)) >= 5 and score!='':
                output.append((int(res_1 + 1), int(res_2 + 1), float(score)))

    if not output:
        raise InvalidFormat('Unable to parse contacts')
    else:
        output = sorted(output, key=itemgetter(2), reverse=True)
        return tuple(output)


