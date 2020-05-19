from loaders import decode_raw_file
from Bio import SeqIO
from Bio.Alphabet.IUPAC import protein
from io import StringIO
from utils import compress_data


def SequenceLoader(raw_file, fname):
    data = None
    invalid = False

    if raw_file is not None:

        decoded = decode_raw_file(raw_file)
        fasta = SeqIO.parse(StringIO(decoded), "fasta")
        records = [record for record in fasta]

        if records is not None and any(records):
            data_raw = list(records[0].seq._data)
            if any([residue not in protein.letters for residue in data_raw]) or len(data_raw) == 0:
                invalid = True
            else:
                data_raw.append(fname)
                data = compress_data(data_raw)
        else:
            invalid = True

    return data, invalid
