from loaders import DatasetReference
from loaders.membranetopologyloader import MembraneTopologyLoader
from parsers import SecondaryStructureFormats


class SecondaryStructureLoader(MembraneTopologyLoader):
    """Class with methods and data structures to store all the information related with a given secondary structure
    prediction and its validity"""

    def __init__(self):
        super(SecondaryStructureLoader, self).__init__()
        self.prediction = None

    @property
    def datatype(self):
        return DatasetReference.SECONDARY_STRUCTURE

    @property
    def parser_formats(self):
        return SecondaryStructureFormats
