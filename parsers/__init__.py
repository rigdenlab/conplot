from enum import Enum


def ConsurfParser(*args, **kwargs):
    from parsers.consurfparser import ConsurfParser

    return ConsurfParser(*args, **kwargs)


def DistogramParser(*args, **kwargs):
    from parsers.distogramparser import DistogramParser

    return DistogramParser(*args, **kwargs)


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


def PDBParser(*args, **kwargs):
    from parsers.pdbparser import PDBParser

    return PDBParser(*args, **kwargs)


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
    CASPRR_MODE_1 = ContactParser
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
    PDB = PDBParser
    CASPRR_MODE_2 = DistogramParser


class ContactInformationFormats(Enum):
    PSICOV = 0
    METAPSICOV = 1
    NEBCON = 2
    CASPRR_MODE_1 = 3
    CASPRR_MODE_2 = 4
    GREMLIN = 5
    EPCMAP = 6
    EVFOLD = 7
    FREECONTACT = 8
    PLMDCA = 9
    PCONS = 10
    FLIB = 11
    SAINT2 = 12
    BCLCONTCATS = 13
    BBCONTACTS = 14
    COMSAT = 15
    CCMPRED = 16
    COLSTATS = 17
    MAPALIGN = 18
    ALEIGEN = 19
    PDB = 20


class ContactMapFormats(Enum):
    PSICOV = 0
    METAPSICOV = 1
    NEBCON = 2
    CASPRR_MODE_1 = 3
    GREMLIN = 5
    EPCMAP = 6
    EVFOLD = 7
    FREECONTACT = 8
    PLMDCA = 9
    PCONS = 10
    FLIB = 11
    SAINT2 = 12
    BCLCONTCATS = 13
    BBCONTACTS = 14
    COMSAT = 15
    CCMPRED = 16
    COLSTATS = 17
    MAPALIGN = 18
    ALEIGEN = 19


class StructuralInformationFormats(Enum):
    PDB = 1


class DistanceInformationFormats(Enum):
    CASPRR_MODE_2 = 1


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
