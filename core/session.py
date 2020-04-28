from .contactloader import ContactLoader
from .sequenceloader import SequenceLoader
from .membranetopologyloader import MembraneTopologyLoader
from .secondarystructureloader import SecondaryStructureLoader
from .disorderloader import DisorderLoader
from .conservationloader import ConservationLoader
from components import MismatchModal, MissingInput_Modal
from index import DatasetReference


class Session(object):
    """Class with methods and data structures to store all the information related with a given session"""

    def __init__(self, id):
        self.id = id
        self.contact_loader = ContactLoader()
        self.sequence_loader = SequenceLoader()
        self.membranetopology_loader = MembraneTopologyLoader()
        self.secondarystructure_loader = SecondaryStructureLoader()
        self.disorder_loader = DisorderLoader()
        self.conservation_loader = ConservationLoader()

    def __iter__(self):
        for loader in (self.contact_loader, self.sequence_loader, self.secondarystructure_loader,
                       self.disorder_loader, self.conservation_loader, self.membranetopology_loader):
            yield loader

    @property
    def missing_data(self):
        """Data fields required to create a plot that are not present in the user input"""
        return [loader for loader in (self.contact_loader, self.sequence_loader) if not loader.valid]

    def lookup_input_errors(self):
        """Check user input is coherent"""

        if any(self.missing_data):
            return MissingInput_Modal(*[missing.datatype.name for missing in self.missing_data])

        try:
            self.contact_loader.cmap.sequence = self.sequence_loader.sequence
            self.contact_loader.cmap.set_sequence_register()
        except IndexError as e:
            return MismatchModal(DatasetReference.SEQUENCE)

        mismatched = []
        for loader in self:
            if loader.datatype == DatasetReference.CONTACT_MAP or loader.datatype == DatasetReference.SEQUENCE:
                pass
            elif loader.prediction is not None and len(self.sequence_loader.sequence) != len(loader.prediction):
                mismatched.append(loader.datatype.name)

        if any(mismatched):
            return MismatchModal(*mismatched)

        return None
