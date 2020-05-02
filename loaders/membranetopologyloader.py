import base64
from loaders import DatasetReference
from loaders.loader import Loader
from parsers import MembraneFormats


class MembraneTopologyLoader(Loader):
    """Class with methods and data structures to store all the information related with a given membrane topology
    prediction and its validity"""

    def __init__(self):
        super(MembraneTopologyLoader, self).__init__()
        self.prediction = None

    @property
    def valid(self):
        if self.prediction is None or len(self.prediction) == 0:
            return False
        else:
            return True

    @property
    def datatype(self):
        return DatasetReference.MEMBRANE_TOPOLOGY

    @property
    def layout_states(self):
        return self.valid_text, self.invalid_text, self.invalid, self.valid_file, self.filename, self.head_color

    @property
    def to_clear(self):
        return 'filename', 'raw_file', 'valid_file', 'prediction'

    @property
    def parser_formats(self):
        return MembraneFormats

    def parse_text(self, text):

        parser = self.parser_formats.__dict__[self.input_format](text)
        parser.parse()

        if not parser.error:
            self.prediction = parser.output

        if self.valid:
            self.valid_text = True
        else:
            self.valid_text = False

    def parse_file(self):

        content_type, content_string = self.raw_file.split(',')
        decoded = base64.b64decode(content_string).decode()
        contents = decoded

        parser = self.parser_formats.__dict__[self.input_format](contents)
        parser.parse()

        if not parser.error:
            self.prediction = parser.output

        if self.valid:
            self.valid_file = True
        else:
            self.valid_file = False
