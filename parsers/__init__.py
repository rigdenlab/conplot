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

def EvfoldParser(*args, **kwargs):
    from parsers.evfoldparser import EvfoldParser

    return EvfoldParser(*args, **kwargs)


def CCMpredParser(*args, **kwargs):
    from parsers.ccmpredparser import CCMpredParser

    return CCMpredParser(*args, **kwargs)

# def CasprrParser(*args, **kwargs):
#     from parsers.casprrparser import CasprrParser
#
#     return CasprrParser(*args, **kwargs)


class ParserFormats(Enum):
    TOPCONS = TopconsParser
    CONSURF = ConsurfParser
    PSIPRED = PsipredParser
    IUPRED = IupredParser
    PSICOV = PsicovParser
    METAPSICOV = PsicovParser
    NEBCON = PsicovParser
    EVFOLD = EvfoldParser
    CCMPRED = CCMpredParser
    CASPRR = PsicovParser


class ContactFormats(Enum):
    PSICOV = PsicovParser
    METAPSICOV = PsicovParser
    NEBCON = PsicovParser
    EVFOLD = EvfoldParser
    CCMPRED = CCMpredParser
    CASPRR = PsicovParser


class MembraneStates(Enum):
    INSIDE = 1
    OUTSIDE = 2
    INSERTED = 3


class ConservationStates(Enum):
    CONSERVED = 1
    AVERAGE = 2
    VARIABLE = 3


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
