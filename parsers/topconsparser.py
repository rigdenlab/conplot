from parsers import MembraneStates
from utils.exceptions import InvalidFormat


def TopconsParser(input, input_format=None):
    contents = input.split('\n')

    try:
        topcons_prediction = contents[contents.index('TOPCONS predicted topology:') + 1].rstrip()
    except ValueError as e:
        raise InvalidFormat

    output = []
    for residue in topcons_prediction.rstrip().lstrip():
        if residue == 'i':
            output.append(MembraneStates.INSIDE.value)
        elif residue == 'o':
            output.append(MembraneStates.OUTSIDE.value)
        elif residue == 'M':
            output.append(MembraneStates.INSERTED.value)
        else:
            raise InvalidFormat('Invalid residue topology {}'.format(residue))

    if not output:
        raise InvalidFormat('Unable to parse prediction in topcons file')
    else:
        return output
