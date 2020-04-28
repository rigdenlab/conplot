from .contactloader import ContactLoader
from .sequenceloader import SequenceLoader
from .membranetopologyloader import MembraneTopologyLoader
from .secondarystructureloader import SecondaryStructureLoader
from .disorderloader import DisorderLoader
from .conservationloader import ConservationLoader
from components import MismatchSequence_Modal, MissingInput_Modal, MismatchMembrane_Modal


class Session(object):
    """Class with methods and data structures to store all the information related with a given session"""

    def __init__(self, id):
        self.id = id
        self.contact_loader = ContactLoader()
        self.sequence_loader = SequenceLoader()
        self.membrtopo_loader = MembraneTopologyLoader()
        self.secondarystructure_loader = SecondaryStructureLoader()
        self.disorder_loader = DisorderLoader()
        self.conservation_loader = ConservationLoader()

    def __iter__(self):
        for loader in (self.contact_loader, self.sequence_loader):
            yield loader

    @property
    def missing_data(self):
        """Data fields required to create a plot that are not present in the user input"""
        return [loader for loader in self if not loader.valid]

    def lookup_input_errors(self):
        """Check user input is coherent"""

        if any(self.missing_data):
            return MissingInput_Modal(*[missing.datatype for missing in self.missing_data])

        try:
            self.contact_loader.cmap.sequence = self.sequence_loader.sequence
            self.contact_loader.cmap.set_sequence_register()
        except IndexError as e:
            return MismatchSequence_Modal()

        # TODO: Need to check all predictions and return a list of those that do not match
        if self.membrtopo_loader.prediction is not None and \
                len(self.sequence_loader.sequence) != len(self.membrtopo_loader.prediction):
            return MismatchMembrane_Modal()

        return None
