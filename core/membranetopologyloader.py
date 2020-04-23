import base64
from .loader import Loader
from enum import Enum
from parsers import TopconsParser


class ParserFormats(Enum):
    TOPCONS = TopconsParser


class MembraneTopologyLoader(Loader):
    """Class with methods and data structures to store all the information related with a given membrane topology
    prediction and its validity"""

    def __init__(self):
        super(MembraneTopologyLoader, self).__init__()
        self.prediction = None
        self.input_format = 'TOPCONS'

    def parse_text(self, text):

        parser = ParserFormats.__getattribute__(ParserFormats, self.input_format).value(text)
        parser.parse()

        if not parser.error:
            self.prediction = parser.output

        if self.valid:
            self.valid_text = True
        else:
            self.valid_text = False

    def parse_file(self):

        content_type, content_string = self.raw_file.split(',')
        decoded = base64.b64decode(content_string)
        decoded = decoded.decode()
        contents = decoded


        parser = ParserFormats(self.input_format).value(contents)
        parser.parse()

        if not parser.error:
            self.prediction = parser.output

        if self.valid:
            self.valid_file = True
        else:
            self.valid_file = False

    @property
    def valid(self):
        if self.prediction is None or len(self.prediction) == 0:
            return False
        else:
            return True

    @property
    def datatype(self):
        return 'Membrane Topology'

    @property
    def layout_states(self):
        return self.valid_text, self.invalid_text, self.invalid, self.valid_file, self.filename, self.head_color
