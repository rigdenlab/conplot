from utils.exceptions import InvalidFormat
from parsers import CustomStates


def CustomParser(input):
    contents = input.split('\n')

    len_flag = []
    while not len_flag:
        len_flag = contents.pop(0).split()

    if len(len_flag) > 1 and len_flag[1].isnumeric() and len_flag[0] == 'LEN':
        length = int(len_flag[1])
        output = [CustomStates.CUSTOM_NAN.value for x in range(0, length)]
    else:
        raise InvalidFormat('First line does not correspond with a valid protein length flag: {}'
                            ''.format(' '.join(len_flag)))

    for line in contents:
        line = line.lstrip().split()

        if not line:
            continue
        elif len(line) != 3 or any([not x.isnumeric() for x in line]) or int(line[0]) > int(line[1]) \
                or 1 > int(line[2]) or int(line[2]) > 11:
            raise InvalidFormat('Invalid line detected: {}'.format(' '.join(line)))

        try:
            for idx in range(int(line[0]) - 1, int(line[1])):
                output[idx] = int(line[2])
        except IndexError:
            raise InvalidFormat('Residues outside protein range detected in line: {}'.format(' '.join(line)))

    if not output:
        raise InvalidFormat('Unable to parse prediction on custom file')
    else:
        return output
