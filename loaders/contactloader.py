from loaders import DatasetReference
from parsers import ContactFormats
from loaders.membranetopologyloader import MembraneTopologyLoader


class ContactLoader(MembraneTopologyLoader):
    """Class with methods and data structures to store all the information related with a given contact map and
    its validity"""

    def __init__(self, *args, **kwargs):
        super(ContactLoader, self).__init__(*args, **kwargs)

    @property
    def datatype(self):
        return DatasetReference.CONTACT_MAP

    @property
    def parser_formats(self):
        return ContactFormats
