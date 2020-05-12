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


def PsicovParser(*args, **kwargs):
    from parsers.psicovparser import PsicovParser

    return PsicovParser(*args, **kwargs)


def IupredParser(*args, **kwargs):
    from parsers.iupredparser import IupredParser

    return IupredParser(*args, **kwargs)


class ParserFormats(Enum):
    TOPCONS = TopconsParser
    CONSURF = ConsurfParser
    PSIPRED = PsipredParser
    IUPRED = IupredParser
    PSICOV = PsicovParser
    METAPSICOV = PsicovParser
    NEBCON = PsicovParser


class ContactFormats(Enum):
    PSICOV = PsicovParser
    METAPSICOV = PsicovParser
    NEBCON = PsicovParser


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
