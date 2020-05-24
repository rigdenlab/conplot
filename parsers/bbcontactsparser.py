from utils.exceptions import InvalidFormat
from operator import itemgetter


def BbcontactsParser(input):
    contents = input.split('\n')
    output = []

    for line in contents:
        line = line.lstrip().split()
        if not line or len(line) != 8:
            continue
        elif line[6].isdigit() and line[7].isdigit():
            if abs(int(line[6]) - int(line[7])) >= 5:
                output.append((int(line[6]), int(line[7]), (0)))

    if not output:
        raise InvalidFormat('Unable to parse contacts')
    else:
        output = sorted(output, key=itemgetter(2), reverse=True)
        return output
