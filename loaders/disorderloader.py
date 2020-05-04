from loaders import DatasetReference
from loaders.membranetopologyloader import MembraneTopologyLoader
from parsers import DisorderFormats


class DisorderLoader(MembraneTopologyLoader):
    """Class with methods and data structures to store all the information related with disorder scores obtained
    for a given sequence and its validity"""

    def __init__(self, *args, **kwargs):
        super(DisorderLoader, self).__init__(*args, **kwargs)

    @property
    def datatype(self):
        return DatasetReference.DISORDER

    @property
    def parser_formats(self):
        return DisorderFormats
