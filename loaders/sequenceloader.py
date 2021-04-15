from loaders import decode_raw_file
from Bio import SeqIO
from Bio.Alphabet.IUPAC import protein
from io import StringIO
from utils import compress_data

normalised_Kyte_Doolittle_hydrophobicity = {'A': 7, 'R': 0, 'N': 1, 'D': 1, 'C': 7, 'E': 1, 'Q': 1, 'G': 4, 'H': 1,
                                            'I': 10, 'L': 9, 'K': 0, 'M': 7, 'F': 8, 'P': 3, 'S': 4, 'T': 4, 'W': 4,
                                            'Y': 3, 'V': 9}


def get_hydrophobicity(seq):
    hydro = []
    for residue in seq:
        try:
            hydro.append(normalised_Kyte_Doolittle_hydrophobicity[residue])
        except (AttributeError, KeyError):
            hydro.append(0)
    return hydro


def SequenceLoader(raw_file):
    sequence_data = None
    sequence_hydrophobicity = None
    invalid = False

    if raw_file is not None:

        try:
            decoded = decode_raw_file(raw_file)
        except UnicodeDecodeError:
            return None, None, True

        fasta = SeqIO.parse(StringIO(decoded), "fasta")
        records = [record for record in fasta]

        if records is not None and any(records):
            data_raw = list(records[0].seq._data)
            if any([residue not in protein.letters for residue in data_raw]) or len(data_raw) == 0:
                invalid = True
            else:
                sequence_hydrophobicity = compress_data(get_hydrophobicity(data_raw))
                sequence_data = compress_data(data_raw)
        else:
            invalid = True

    return sequence_data, sequence_hydrophobicity, invalid
