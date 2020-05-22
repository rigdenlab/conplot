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

def FreecontactParser(*args, **kwargs):
    from parsers.freecontactparser import FreecontactParser

    return FreecontactParser(*args, **kwargs)

def ComsatParser(*args, **kwargs):
    from parsers.comsatparser import ComsatParser

    return ComsatParser(*args, **kwargs)

def PlmdcaParser(*args, **kwargs):
    from parsers.plmdcaparser import PlmdcaParser

    return PlmdcaParser(*args, **kwargs)


def CCMpredParser(*args, **kwargs):
    from parsers.ccmpredparser import CCMpredParser

    return CCMpredParser(*args, **kwargs)


def BbcontactsParser(*args, **kwargs):
    from parsers.bbcontactsparser import BbcontactsParser

    return BbcontactsParser(*args, **kwargs)


def CustomParser(*args, **kwargs):
    from parsers.customparser import CustomParser

    return CustomParser(*args, **kwargs)


class ParserFormats(Enum):
    TOPCONS = TopconsParser
    CONSURF = ConsurfParser
    PSIPRED = PsipredParser
    IUPRED = IupredParser
    PSICOV = PsicovParser
    METAPSICOV = PsicovParser
    NEBCON = PsicovParser
    CUSTOM = CustomParser
    EVFOLD = EvfoldParser
    CCMPRED = CCMpredParser
    CASPRR = PsicovParser
    GREMLIN = PsicovParser
    COLSTATS = CCMpredParser
    FREECONTACT = FreecontactParser
    EPCMAP = PsicovParser
    COMSAT = ComsatParser
    PLMDCA = PlmdcaParser
    PCONS = PlmdcaParser
    BBCONTACTS = BbcontactsParser


class ContactFormats(Enum):
    PSICOV = PsicovParser
    METAPSICOV = PsicovParser
    NEBCON = PsicovParser
    EVFOLD = EvfoldParser
    CCMPRED = CCMpredParser
    CASPRR = PsicovParser
    GREMLIN = PsicovParser
    COLSTATS = CCMpredParser
    FREECONTACT = FreecontactParser
    EPCMAP = PsicovParser
    COMSAT = ComsatParser
    PLMDCA = PlmdcaParser
    PCONS = PlmdcaParser
    BBCONTACTS = BbcontactsParser



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
