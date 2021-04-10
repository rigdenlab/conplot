from parsers import DisorderStates
from utils.exceptions import InvalidFormat


def IupredParser(input, input_format=None):
    contents = input.split('\n')
    output = []

    for line in contents:

        line = line.lstrip().split()
        if len(line) < 1 or line[0] == '#' or len(line) < 3:
            continue
        else:
            try:
                score = float(line[2])
            except ValueError:
                raise InvalidFormat('Invalid score field {}'.format(line[2]))
        if score >= 0.5:
            output.append(DisorderStates.DISORDER.value)
        else:
            output.append(DisorderStates.ORDER.value)

    if not output:
        raise InvalidFormat('Unable to parse prediction on iupred file')
    else:
        return output
