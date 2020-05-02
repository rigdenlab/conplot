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


def IupredParser(*args, **kwargs):
    from parsers.iupredparser import IupredParser

    return IupredParser(*args, **kwargs)


class MembraneFormats(Enum):
    TOPCONS = TopconsParser


class ConservationFormats(Enum):
    CONSURF = ConsurfParser


class SecondaryStructureFormats(Enum):
    PSIPRED = PsipredParser


class DisorderFormats(Enum):
    IUPRED = IupredParser


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
