from enum import Enum


def ConsurfParser(*args, **kwargs):
    from parsers.consurfparser import ConsurfParser

    return ConsurfParser(*args, **kwargs)


def Ss2Parser(*args, **kwargs):
    from parsers.ss2parser import Ss2Parser

    return Ss2Parser(*args, **kwargs)


def HorizParser(*args, **kwargs):
    from parsers.horizparser import HorizParser

    return HorizParser(*args, **kwargs)


def guess_psipred_format(*args, **kwargs):
    from parsers.psipredparser import guess_psipred_format

    return guess_psipred_format(*args, **kwargs)


def CASPRR2Parser(*args, **kwargs):
    from parsers.casprr2parser import CASPRR2Parser

    return CASPRR2Parser(*args, **kwargs)


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


def A3mParser(*args, **kwargs):
    from parsers.a3mparser import A3mParser

    return A3mParser(*args, **kwargs)


def FastaMsaParser(*args, **kwargs):
    from parsers.fastamsaparser import FastaMsaParser

    return FastaMsaParser(*args, **kwargs)


def CCMpredParser(*args, **kwargs):
    from parsers.ccmpredparser import CCMpredParser

    return CCMpredParser(*args, **kwargs)


def PDBParser(*args, **kwargs):
    from parsers.pdbparser import PDBParser

    return PDBParser(*args, **kwargs)


def MappredParser(*args, **kwargs):
    from parsers.mappred import MappredParser

    return MappredParser(*args, **kwargs)


def CustomParser(*args, **kwargs):
    from parsers.customparser import CustomParser

    return CustomParser(*args, **kwargs)


def NpzParser(*args, **kwargs):
    from parsers.npzparser import NpzParser

    return NpzParser(*args, **kwargs)


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
    CASPRR_MODE_2 = CASPRR2Parser
    trROSETTA_NPZ = NpzParser
    MAPPRED = MappredParser
    A3M = A3mParser


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
    trROSETTA_NPZ = 21
    MAPPRED = 22


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
    trROSETTA_NPZ = 2
    MAPPRED = 3


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


class HydrophobicityStates(Enum):
    HYDROPATHY_10 = 10
    HYDROPATHY_9 = 9
    HYDROPATHY_8 = 8
    HYDROPATHY_7 = 7
    HYDROPATHY_6 = 6
    HYDROPATHY_5 = 5
    HYDROPATHY_4 = 4
    HYDROPATHY_3 = 3
    HYDROPATHY_2 = 2
    HYDROPATHY_1 = 1
    HYDROPATHY_0 = 0


class DensityStates(Enum):
    CONTACT_DENSITY_0 = 0
    CONTACT_DENSITY_1 = 1
    CONTACT_DENSITY_2 = 2
    CONTACT_DENSITY_3 = 3
    CONTACT_DENSITY_4 = 4
    CONTACT_DENSITY_5 = 5
    CONTACT_DENSITY_6 = 6
    CONTACT_DENSITY_7 = 7
    CONTACT_DENSITY_8 = 8
    CONTACT_DENSITY_9 = 9
    CONTACT_DENSITY_10 = 10


class DiffStates(Enum):
    CONTACT_DIFF_0 = 0
    CONTACT_DIFF_1 = 1
    CONTACT_DIFF_2 = 2
    CONTACT_DIFF_3 = 3
    CONTACT_DIFF_4 = 4
    CONTACT_DIFF_5 = 5
    CONTACT_DIFF_6 = 6
    CONTACT_DIFF_7 = 7
    CONTACT_DIFF_8 = 8
    CONTACT_DIFF_9 = 9
    CONTACT_DIFF_10 = 10


class MsaStates(Enum):
    MSA_COVERAGE_0 = 0
    MSA_COVERAGE_1 = 1
    MSA_COVERAGE_2 = 2
    MSA_COVERAGE_3 = 3
    MSA_COVERAGE_4 = 4
    MSA_COVERAGE_5 = 5
    MSA_COVERAGE_6 = 6
    MSA_COVERAGE_7 = 7
    MSA_COVERAGE_8 = 8
    MSA_COVERAGE_9 = 9
    MSA_COVERAGE_10 = 10


class DatasetStates(Enum):
    membranetopology = MembraneStates
    secondarystructure = SecondaryStructureStates
    conservation = ConservationStates
    disorder = DisorderStates
    custom = CustomStates
    hydrophobicity = HydrophobicityStates
    density = DensityStates
    diff = DiffStates
    msa = MsaStates
