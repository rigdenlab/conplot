from .membranetopologyloader import MembraneTopologyLoader
from index.formatindex import DisorderFormats


class DisorderLoader(MembraneTopologyLoader):
    """Class with methods and data structures to store all the information related with disorder scores obtained
    for a given sequence and its validity"""

    def __init__(self):
        super(DisorderLoader, self).__init__()
        self.prediction = None

    @property
    def datatype(self):
        return 'Disorder prediction'

    @property
    def parser_formats(self):
        return DisorderFormats
