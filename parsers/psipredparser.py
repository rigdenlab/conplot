from parsers import SecondaryStructureStates
from utils.exceptions import InvalidFormat


def PsipredParser(input):
    contents = input.split('\n')
    output = []

    for line in contents:
        line = line.split()
        if len(line) != 6 or line[0] == '#':
            continue
        elif line[2] == 'H':
            output.append(SecondaryStructureStates.HELIX.value)
        elif line[2] == 'C':
            output.append(SecondaryStructureStates.COIL.value)
        elif line[2] == 'E':
            output.append(SecondaryStructureStates.SHEET.value)
        else:
            raise InvalidFormat('Invalid secondary structure element {}'.format(line[2]))

    if not output:
        raise InvalidFormat('Unable to parse prediction in psipred file')
    else:
        return output
