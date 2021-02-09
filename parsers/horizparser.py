from parsers import SecondaryStructureStates
from utils.exceptions import InvalidFormat


def HorizParser(contents):
    output = []

    for line in contents:
        if 'Pred: ' in line and line[0] != '#':
            prediction = line.split()[-1]
            for residue in prediction:
                if residue == 'H':
                    output.append(SecondaryStructureStates.HELIX.value)
                elif residue == 'C':
                    output.append(SecondaryStructureStates.COIL.value)
                elif residue == 'E':
                    output.append(SecondaryStructureStates.SHEET.value)
                else:
                    raise InvalidFormat('Invalid secondary structure element {}'.format(residue))

    if not output:
        raise InvalidFormat('Unable to parse prediction in psipred file')
    else:
        return output
