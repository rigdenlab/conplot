from utils.exceptions import InvalidFormat
from operator import itemgetter


def BbcontactsParser(input):
    contents = input.split('\n')
    output = []

    for line in contents:
        line = line.lstrip().split()
        if not line or line[0].isalpha():
            continue
        try:
            if line[6].isdigit() and line[7].isdigit() and len(line) >= 5:
                if abs(int(line[6]) - int(line[7])) >= 5:
                    output.append((int(line[6]), int(line[7]), (0)))
        except IndexError:
            raise InvalidFormat('Unable to parse contacts')

    if not output:
        raise InvalidFormat('Unable to parse contacts')
    else:
        output = sorted(output, key=itemgetter(2), reverse=True)
        return output
