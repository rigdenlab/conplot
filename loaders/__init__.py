from enum import Enum
import base64


class DatasetReference(Enum):
    SEQUENCE = 'sequence'
    CONTACT_MAP = 'contact'
    MEMBRANE_TOPOLOGY = 'membranetopology'
    SECONDARY_STRUCTURE = 'secondarystructure'
    CONSERVATION = 'conservation'
    DISORDER = 'disorder'
    CUSTOM = 'custom'


class AdditionalTracks(Enum):
    TOPCONS = DatasetReference.MEMBRANE_TOPOLOGY.value
    CONSURF = DatasetReference.CONSERVATION.value
    PSIPRED = DatasetReference.SECONDARY_STRUCTURE.value
    IUPRED = DatasetReference.DISORDER.value
    CUSTOM = DatasetReference.CUSTOM.value


def decode_raw_file(raw_file):
    content_type, content_string = raw_file.split(',')
    decoded = base64.b64decode(content_string)
    decoded = decoded.decode()
    return decoded


def Loader(*args, **kwargs):
    from loaders.loader import Loader

    return Loader(*args, **kwargs)


def SequenceLoader(*args, **kwargs):
    from loaders.sequenceloader import SequenceLoader

    return SequenceLoader(*args, **kwargs)
