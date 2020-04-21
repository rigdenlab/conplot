from .contactloader import ContactLoader
from .sequenceloader import SequenceLoader


class Session(object):
    """Class with methods and data structures to store all the information related with a given session"""

    def __init__(self, id):
        self.id = id
        self.contact_loader = ContactLoader()
        self.sequence_loader = SequenceLoader()
