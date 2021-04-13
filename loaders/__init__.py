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

    @classmethod
    def exclude_seq(cls):
        for item in cls:
            if item.value != 'sequence':
                yield item


class AdditionalDatasetReference(Enum):
    TOPCONS = DatasetReference.MEMBRANE_TOPOLOGY.value
    PSIPRED = DatasetReference.SECONDARY_STRUCTURE.value
    IUPRED = DatasetReference.DISORDER.value
    CONSURF = DatasetReference.CONSERVATION.value
    CUSTOM = DatasetReference.CUSTOM.value


def decode_raw_file(raw_file):
    content_type, content_string = raw_file.split(',')
    decoded = base64.b64decode(content_string)
    decoded = decoded.decode()
    return decoded


class ResidueHydrophobicityStates(Enum):
    HYDROPHOBIC = 1
    INDIFFERENT = 2


class ResidueHydrophobicity(Enum):
    I = ResidueHydrophobicityStates.HYDROPHOBIC.value
    L = ResidueHydrophobicityStates.HYDROPHOBIC.value
    F = ResidueHydrophobicityStates.HYDROPHOBIC.value
    V = ResidueHydrophobicityStates.HYDROPHOBIC.value
    M = ResidueHydrophobicityStates.HYDROPHOBIC.value
    P = ResidueHydrophobicityStates.HYDROPHOBIC.value
    W = ResidueHydrophobicityStates.HYDROPHOBIC.value
    H = ResidueHydrophobicityStates.INDIFFERENT.value
    T = ResidueHydrophobicityStates.INDIFFERENT.value
    E = ResidueHydrophobicityStates.HYDROPHOBIC.value
    Q = ResidueHydrophobicityStates.HYDROPHOBIC.value
    C = ResidueHydrophobicityStates.HYDROPHOBIC.value
    Y = ResidueHydrophobicityStates.INDIFFERENT.value
    A = ResidueHydrophobicityStates.INDIFFERENT.value
    S = ResidueHydrophobicityStates.INDIFFERENT.value
    N = ResidueHydrophobicityStates.INDIFFERENT.value
    D = ResidueHydrophobicityStates.INDIFFERENT.value
    R = ResidueHydrophobicityStates.INDIFFERENT.value
    G = ResidueHydrophobicityStates.INDIFFERENT.value
    K = ResidueHydrophobicityStates.INDIFFERENT.value


def Loader(*args, **kwargs):
    from loaders.loader import Loader

    return Loader(*args, **kwargs)


def SequenceLoader(*args, **kwargs):
    from loaders.sequenceloader import SequenceLoader

    return SequenceLoader(*args, **kwargs)


STATES = {
    DatasetReference.MEMBRANE_TOPOLOGY.value: {
        1: 'INSIDE',
        2: 'OUTSIDE',
        3: 'INSERTED'
    },
    DatasetReference.CONSERVATION.value: {
        1: 'VARIABLE_1',
        2: 'VARIABLE_2',
        3: 'VARIABLE_3',
        4: 'AVERAGE_4',
        5: 'AVERAGE_5',
        6: 'AVERAGE_6',
        7: 'CONSERVED_7',
        8: 'CONSERVED_8',
        9: 'CONSERVED_9'
    },
    DatasetReference.CUSTOM.value: {
        1: 'CUSTOM_1',
        2: 'CUSTOM_2',
        3: 'CUSTOM_3',
        4: 'CUSTOM_4',
        5: 'CUSTOM_5',
        6: 'CUSTOM_6',
        7: 'CUSTOM_7',
        8: 'CUSTOM_8',
        9: 'CUSTOM_9',
        10: 'CUSTOM_10',
        11: 'CUSTOM_11',
        'NAN': 'CUSTOM_NAN'
    },
    DatasetReference.DISORDER.value: {
        1: 'DISORDER',
        2: 'ORDER'
    },
    DatasetReference.SECONDARY_STRUCTURE.value: {
        1: 'HELIX',
        2: 'COIL',
        3: 'SHEET'
    }
}
