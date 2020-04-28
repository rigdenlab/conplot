from enum import Enum
from parsers.topconsparser import TopconsParser
from parsers.consurfparser import ConsurfParser
from parsers.psipredparser import PsipredParser


class MembraneFormats(Enum):
    TOPCONS = TopconsParser


class ConservationFormats(Enum):
    CONSURF = ConsurfParser


class SecondaryStructureFormats(Enum):
    PSIPRED = PsipredParser


