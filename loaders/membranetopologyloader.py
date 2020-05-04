import base64
from loaders import DatasetReference
from loaders.loader import Loader
from parsers import MembraneFormats


class MembraneTopologyLoader(Loader):
    """Class with methods and data structures to store all the information related with a given membrane topology
    prediction and its validity"""

    def __init__(self, *args, **kwargs):
        super(MembraneTopologyLoader, self).__init__(*args, **kwargs)
        self.input_format = 'TOPCONS'

    @property
    def valid(self):
        if self.data is None or len(self.data) == 0:
            return False
        else:
            return True

    @property
    def datatype(self):
        return DatasetReference.MEMBRANE_TOPOLOGY

    @property
    def layout_states(self):
        return self.invalid, self.valid, self.filename, self.head_color

    @property
    def parser_formats(self):
        return MembraneFormats

    def parse(self):

        content_type, content_string = self.raw_file.split(',')
        decoded = base64.b64decode(content_string).decode()
        contents = decoded

        parser = self.parser_formats.__dict__[self.input_format](contents)
        parser.parse()

        if not parser.error:
            self.data = parser.output
