from .membranetopologyloader import MembraneTopologyLoader
from enum import Enum
from parsers import PsipredParser


class _ParserFormats(Enum):
    PSIPRED = PsipredParser


class SecondaryStructureStates(Enum):
    HELIX = 1
    COIL = 2
    SHEET = 3


class SecondaryStructureLoader(MembraneTopologyLoader):
    """Class with methods and data structures to store all the information related with a given secondary structure
    prediction and its validity"""

    def __init__(self):
        super(SecondaryStructureLoader, self).__init__()
        self.prediction = None

    @property
    def datatype(self):
        return 'Secondary Structure'

    @property
    def parser_formats(self):
        return _ParserFormats
