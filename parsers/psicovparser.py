from utils.exceptions import InvalidFormat
from operator import itemgetter


def PsicovParser(input):
    contents = input.split('\n')
    output = []

    for line in contents:

        line = line.lstrip().split()

        if not line or line[0].isalpha():
            continue
        elif line[0].isdigit() and line[1].isdigit() and len(line) >= 5:
            if abs(int(line[0]) - int(line[1])) >= 5:
                # TODO: Sorting the residue numbers here will save time when creating the plot
                output.append((int(line[0]), int(line[1]), float(line[4])))

    if not output:
        raise InvalidFormat('Unable to parse contacts')
    else:
        output = sorted(output, key=itemgetter(2), reverse=True)
        return output
