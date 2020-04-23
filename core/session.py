from .contactloader import ContactLoader
from .sequenceloader import SequenceLoader
from .membranetopologyloader import MembraneTopologyLoader

class Session(object):
    """Class with methods and data structures to store all the information related with a given session"""

    def __init__(self, id):
        self.id = id
        self.contact_loader = ContactLoader()
        self.sequence_loader = SequenceLoader()
        self.membrtopo_loader = MembraneTopologyLoader()

    def __iter__(self):
        for loader in (self.contact_loader, self.sequence_loader):
            yield loader

    @property
    def missing_data(self):
        return [loader for loader in self if not loader.valid]
