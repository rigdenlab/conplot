from enum import Enum
import base64


class DatasetReference(Enum):
    SEQUENCE = 'sequence'
    HYDROPHOBICITY = 'hydrophobicity'
    CONTACT_MAP = 'contact'
    CONTACT_DENSITY = 'density'
    CONTACT_DIFF = 'diff'
    MEMBRANE_TOPOLOGY = 'membranetopology'
    SECONDARY_STRUCTURE = 'secondarystructure'
    CONSERVATION = 'conservation'
    DISORDER = 'disorder'
    CUSTOM = 'custom'
    MSA = 'msa'

    @classmethod
    def exclude_seq(cls):
        for item in cls:
            if item.value != 'sequence' and item.value != 'hydrophobicity':
                yield item


class AdditionalDatasetReference(Enum):
    A3M = DatasetReference.MSA.value
    TOPCONS = DatasetReference.MEMBRANE_TOPOLOGY.value
    PSIPRED = DatasetReference.SECONDARY_STRUCTURE.value
    IUPRED = DatasetReference.DISORDER.value
    CONSURF = DatasetReference.CONSERVATION.value
    CUSTOM = DatasetReference.CUSTOM.value

    @classmethod
    def include_hydrophobicity(cls):
        new_enum = Enum('AdditionalDatasetReference', {
            'A3M': DatasetReference.MSA.value,
            'TOPCONS': DatasetReference.MEMBRANE_TOPOLOGY.value,
            'PSIPRED': DatasetReference.SECONDARY_STRUCTURE.value,
            'IUPRED': DatasetReference.DISORDER.value,
            'CONSURF': DatasetReference.CONSERVATION.value,
            'CUSTOM': DatasetReference.CUSTOM.value,
            'HYDROPHOBICITY': DatasetReference.HYDROPHOBICITY.value
        })

        for item in new_enum:
            yield item


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
    },
    DatasetReference.HYDROPHOBICITY.value: {
        0: 'HYDROPATHY_0',
        1: 'HYDROPATHY_1',
        2: 'HYDROPATHY_2',
        3: 'HYDROPATHY_3',
        4: 'HYDROPATHY_4',
        5: 'HYDROPATHY_5',
        6: 'HYDROPATHY_6',
        7: 'HYDROPATHY_7',
        8: 'HYDROPATHY_8',
        9: 'HYDROPATHY_9',
        10: 'HYDROPATHY_10'},
    DatasetReference.CONTACT_DENSITY.value: {
        0: 'CONTACT_DENSITY_0',
        1: 'CONTACT_DENSITY_1',
        2: 'CONTACT_DENSITY_2',
        3: 'CONTACT_DENSITY_3',
        4: 'CONTACT_DENSITY_4',
        5: 'CONTACT_DENSITY_5',
        6: 'CONTACT_DENSITY_6',
        7: 'CONTACT_DENSITY_7',
        8: 'CONTACT_DENSITY_8',
        9: 'CONTACT_DENSITY_9',
        10: 'CONTACT_DENSITY_10',
    },
    DatasetReference.CONTACT_DIFF.value:{
        0: 'CONTACT_DIFF_0',
        1: 'CONTACT_DIFF_1',
        2: 'CONTACT_DIFF_2',
        3: 'CONTACT_DIFF_3',
        4: 'CONTACT_DIFF_4',
        5: 'CONTACT_DIFF_5',
        6: 'CONTACT_DIFF_6',
        7: 'CONTACT_DIFF_7',
        8: 'CONTACT_DIFF_8',
        9: 'CONTACT_DIFF_9',
        10: 'CONTACT_DIFF_10',
    },
    DatasetReference.MSA.value: {
        0: 'MSA_COVERAGE_0',
        1: 'MSA_COVERAGE_1',
        2: 'MSA_COVERAGE_2',
        3: 'MSA_COVERAGE_3',
        4: 'MSA_COVERAGE_4',
        5: 'MSA_COVERAGE_5',
        6: 'MSA_COVERAGE_6',
        7: 'MSA_COVERAGE_7',
        8: 'MSA_COVERAGE_8',
        9: 'MSA_COVERAGE_9',
        10: 'MSA_COVERAGE_10',
    }
}
