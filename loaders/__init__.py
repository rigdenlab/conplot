from enum import Enum


class DatasetReference(Enum):
    SEQUENCE = 'sequence'
    CONTACT_MAP = 'contact'
    MEMBRANE_TOPOLOGY = 'membranetopology'
    SECONDARY_STRUCTURE = 'secondarystructure'
    CONSERVATION = 'conservation'
    DISORDER = 'disorder'


def ConservationLoader(*args, **kwargs):
    from loaders.conservationloader import ConservationLoader

    return ConservationLoader(*args, **kwargs)


def ContactLoader(*args, **kwargs):
    from loaders.contactloader import ContactLoader

    return ContactLoader(*args, **kwargs)


def SequenceLoader(*args, **kwargs):
    from loaders.sequenceloader import SequenceLoader

    return SequenceLoader(*args, **kwargs)


def DisorderLoader(*args, **kwargs):
    from loaders.disorderloader import DisorderLoader

    return DisorderLoader(*args, **kwargs)


def SecondaryStructureLoader(*args, **kwargs):
    from loaders.secondarystructureloader import SecondaryStructureLoader

    return SecondaryStructureLoader(*args, **kwargs)


def MembraneTopologyLoader(*args, **kwargs):
    from loaders.membranetopologyloader import MembraneTopologyLoader

    return MembraneTopologyLoader(*args, **kwargs)
