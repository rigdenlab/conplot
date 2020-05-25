from utils.exceptions import InvalidFormat
from operator import itemgetter


def BclcontactsParser(input):
    contents = input.split('\n')
    output = []

    for line in contents:
        line = line.lstrip().split()
        if not line or line[0].isalpha():
            continue
        elif line[0].isdigit() and line[2].isdigit() and len(line) >= 9:
            if abs(int(line[0]) - int(line[2])) >= 5:
                output.append((int(line[0]), int(line[2]), float(line[9])))

    if not output:
        raise InvalidFormat('Unable to parse contacts')
    else:
        output = sorted(output, key=itemgetter(2), reverse=True)
        return output