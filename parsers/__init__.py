from enum import Enum


def ConsurfParser(*args, **kwargs):
    from parsers.consurfparser import ConsurfParser

    return ConsurfParser(*args, **kwargs)


def TopconsParser(*args, **kwargs):
    from parsers.topconsparser import TopconsParser

    return TopconsParser(*args, **kwargs)


def PsipredParser(*args, **kwargs):
    from parsers.psipredparser import PsipredParser

    return PsipredParser(*args, **kwargs)


def ContactParser(*args, **kwargs):
    from parsers.contactparser import ContactParser

    return ContactParser(*args, **kwargs)


def IupredParser(*args, **kwargs):
    from parsers.iupredparser import IupredParser

    return IupredParser(*args, **kwargs)


def CCMpredParser(*args, **kwargs):
    from parsers.ccmpredparser import CCMpredParser

    return CCMpredParser(*args, **kwargs)


def CustomParser(*args, **kwargs):
    from parsers.customparser import CustomParser

    return CustomParser(*args, **kwargs)


class ParserFormats(Enum):
    TOPCONS = TopconsParser
    CONSURF = ConsurfParser
    PSIPRED = PsipredParser
    IUPRED = IupredParser
    CUSTOM = CustomParser
    PSICOV = ContactParser
    METAPSICOV = ContactParser
    NEBCON = ContactParser
    CASPRR = ContactParser
    GREMLIN = ContactParser
    EPCMAP = ContactParser
    EVFOLD = ContactParser
    FREECONTACT = ContactParser
    PLMDCA = ContactParser
    PCONS = ContactParser
    FLIB = ContactParser
    SAINT2 = ContactParser
    BCLCONTCATS = ContactParser
    BBCONTACTS = ContactParser
    COMSAT = ContactParser
    CCMPRED = CCMpredParser
    COLSTATS = CCMpredParser


class ContactFormats(Enum):
    PSICOV = 0
    METAPSICOV = 1
    NEBCON = 2
    CASPRR = 3
    GREMLIN = 4
    EPCMAP = 5
    EVFOLD = 6
    FREECONTACT = 7
    PLMDCA = 8
    PCONS = 9
    FLIB = 10
    SAINT2 = 11
    BCLCONTCATS = 12
    BBCONTACTS = 13
    COMSAT = 14
    CCMPRED = 15
    COLSTATS = 16
    MAPALIGN = 17
    ALEIGEN = 18


class MembraneStates(Enum):
    INSIDE = 1
    OUTSIDE = 2
    INSERTED = 3


class ConservationStates(Enum):
    VARIABLE_1 = 1
    VARIABLE_2 = 2
    VARIABLE_3 = 3
    AVERAGE_4 = 4
    AVERAGE_5 = 5
    AVERAGE_6 = 6
    CONSERVED_7 = 7
    CONSERVED_8 = 8
    CONSERVED_9 = 9


class CustomStates(Enum):
    CUSTOM_1 = 1
    CUSTOM_2 = 2
    CUSTOM_3 = 3
    CUSTOM_4 = 4
    CUSTOM_5 = 5
    CUSTOM_6 = 6
    CUSTOM_7 = 7
    CUSTOM_8 = 8
    CUSTOM_9 = 9
    CUSTOM_10 = 10
    CUSTOM_11 = 11
    CUSTOM_NAN = 'NAN'


class DisorderStates(Enum):
    DISORDER = 1
    ORDER = 2


class SecondaryStructureStates(Enum):
    HELIX = 1
    COIL = 2
    SHEET = 3


class DatasetStates(Enum):
    membranetopology = MembraneStates
    secondarystructure = SecondaryStructureStates
    conservation = ConservationStates
    disorder = DisorderStates
    custom = CustomStates
