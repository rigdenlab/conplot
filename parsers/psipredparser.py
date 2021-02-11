from parsers import HorizParser, Ss2Parser
from utils.exceptions import InvalidFormat


def guess_psipred_format(contents):
    for line in contents:
        if '# PSIPRED VFORMAT' in line:
            return Ss2Parser
        elif '# PSIPRED HFORMAT' in line:
            return HorizParser

    raise InvalidFormat('Unable to guess psipred file format')


def PsipredParser(input):
    contents = input.split('\n')
    parser = guess_psipred_format(contents)
    return parser(contents)
