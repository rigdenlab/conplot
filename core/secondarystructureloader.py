from .loader import Loader
from enum import Enum
from parsers import PsipredParser


class ParserFormats(Enum):
    PSIPRED = PsipredParser


class SecondaryStructureLoader(Loader):
    """Class with methods and data structures to store all the information related with a given secondary structure
    prediction and its validity"""

    def __init__(self):
        super(SecondaryStructureLoader, self).__init__()
        self.prediction = None

    def parse_text(self, text):
        pass

    def parse_file(self):
        pass

    @property
    def valid(self):
        if self.prediction is None or len(self.prediction) == 0:
            return False
        else:
            return True

    @property
    def datatype(self):
        return 'Secondary Structure'

    @property
    def layout_states(self):
        return self.valid_text, self.invalid_text, self.invalid, self.valid_file, self.filename, self.head_color

    @property
    def to_clear(self):
        return 'filename', 'raw_file', 'valid_file', 'prediction'
