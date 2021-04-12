from utils.exceptions import InvalidFormat


def ConsurfParser(input, input_format=None):
    contents = input.split('\n')
    output = []

    for line in contents:

        line = line.lstrip().split()

        if len(line) < 4 or not line[0].isnumeric() or not line[3][0].isnumeric():
            continue
        else:
            score = int(line[3][0])

        if score > 9:
            raise InvalidFormat('Unable to parse prediction on consurf file: score above 9 detected!')
        else:
            output.append(score)

    if not output:
        raise InvalidFormat('Unable to parse prediction on consurf file')
    else:
        return output
