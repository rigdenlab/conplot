from enum import Enum
from operator import itemgetter
import re
from utils import unique_by_key
from utils.exceptions import InvalidFormat


class FieldSeparatorContactFormats(Enum):
    PSICOV = re.compile(r'\s+')
    METAPSICOV = re.compile(r'\s+')
    NEBCON = re.compile(r'\s+')
    CASPRR = re.compile(r'\s+')
    GREMLIN = re.compile(r'\s+')
    EPCMAP = re.compile(r'\s+')
    EVFOLD = re.compile(r'\s+')
    FREECONTACT = re.compile(r'\s+')
    PLMDCA = re.compile(',')
    PCONS = re.compile(r'\s+')
    FLIB = re.compile(r'\s+')
    SAINT2 = re.compile(r'\s+')
    BCLCONTACTS = re.compile(r'\s+')
    BBCONTACTS = re.compile(r'\s+')
    COMSAT = re.compile(r'\s+')
    MAPALIGN = re.compile(r'\s+')
    ALEIGEN = re.compile(r'\s+')


class LineSizeContactFormats(Enum):
    PSICOV = 5
    METAPSICOV = 5
    NEBCON = 5
    CASPRR = 5
    GREMLIN = 5
    EPCMAP = 5
    EVFOLD = 5
    FREECONTACT = 5
    PLMDCA = 3
    PCONS = 3
    FLIB = 3
    SAINT2 = 3
    BCLCONTACTS = 9
    BBCONTACTS = 8
    COMSAT = 5
    MAPALIGN = 4
    ALEIGEN = 2


class FieldResidueOneContactFormats(Enum):
    PSICOV = 0
    METAPSICOV = 0
    NEBCON = 0
    CASPRR = 0
    GREMLIN = 0
    EPCMAP = 0
    EVFOLD = 0
    FREECONTACT = 0
    PLMDCA = 0
    PCONS = 0
    FLIB = 0
    SAINT2 = 0
    BCLCONTACTS = 0
    BBCONTACTS = 6
    COMSAT = 0
    MAPALIGN = 1
    ALEIGEN = 0


class FieldResidueTwoContactFormats(Enum):
    PSICOV = 1
    METAPSICOV = 1
    NEBCON = 1
    CASPRR = 1
    GREMLIN = 1
    EPCMAP = 1
    EVFOLD = 2
    FREECONTACT = 2
    PLMDCA = 1
    PCONS = 1
    FLIB = 1
    SAINT2 = 1
    BCLCONTACTS = 2
    BBCONTACTS = 7
    COMSAT = 2
    MAPALIGN = 2
    ALEIGEN = 1


class FieldRawScoreContactFormats(Enum):
    PSICOV = 4
    METAPSICOV = 4
    NEBCON = 4
    CASPRR = 4
    GREMLIN = 4
    EPCMAP = 4
    EVFOLD = 5
    FREECONTACT = 4
    PLMDCA = 2
    PCONS = 2
    FLIB = 2
    SAINT2 = 2
    BCLCONTACTS = 9
    BBCONTACTS = None
    COMSAT = None
    MAPALIGN = 3
    ALEIGEN = None


def ContactParser(input, input_format):
    contents = input.split('\n')
    output = []
    res_1_idx = FieldResidueOneContactFormats.__getattr__(input_format).value
    res_2_idx = FieldResidueTwoContactFormats.__getattr__(input_format).value
    raw_score_idx = FieldRawScoreContactFormats.__getattr__(input_format).value
    line_size = LineSizeContactFormats.__getattr__(input_format).value
    regex = FieldSeparatorContactFormats.__getattr__(input_format).value

    for idx, line in enumerate(contents):

        line = line.lstrip().rstrip()
        line = re.split(regex, line)

        if not line or len(line) < line_size or not line[res_1_idx].isdigit() or not line[res_2_idx].isdigit():
            continue

        res_1 = int(line[res_1_idx])
        res_2 = int(line[res_2_idx])
        seq_distance = res_1 - res_2

        if abs(seq_distance) >= 5:
            if raw_score_idx is not None:
                raw_score = float(line[raw_score_idx])
            else:
                raw_score = 0
            contact = [res_1, res_2, raw_score]
            contact[:2] = sorted(contact[:2], reverse=True)
            output.append((tuple(contact[:2]), contact[2]))

    if not output:
        raise InvalidFormat('Unable to parse contacts')
    else:
        unique_contacts = unique_by_key(output, key=itemgetter(0))
        output = [(*contact[0], contact[1]) for contact in unique_contacts]
        output = sorted(output, key=itemgetter(2), reverse=True)
        return output
