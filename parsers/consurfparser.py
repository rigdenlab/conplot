from parsers import ConservationStates
from utils.exceptions import InvalidFormat


def ConsurfParser(input):
    contents = input.split('\n')
    output = []

    for line in contents:

        line = line.lstrip().split()

        if len(line) < 4 or not line[0].isnumeric() or not line[3][0].isnumeric():
            continue
        else:
            score = int(line[3][0])

        if score <= 3:
            output.append(ConservationStates.VARIABLE.value)
        elif score < 7:
            output.append(ConservationStates.AVERAGE.value)
        elif score >= 7:
            output.append(ConservationStates.CONSERVED.value)

    if not output:
        raise InvalidFormat('Unable to parse prediction on consurf file')
    else:
        return output
