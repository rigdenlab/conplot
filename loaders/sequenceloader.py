from loaders import decode_raw_file, LayoutFieldsReference
from Bio import SeqIO
from Bio.Alphabet.IUPAC import protein
from io import StringIO


def SequenceLoader(filename, raw_file):
    result = {
        LayoutFieldsReference.VALID.value: False,
        LayoutFieldsReference.INVALID.value: False,
        LayoutFieldsReference.HEAD_COLOR.value: 'dark',
        LayoutFieldsReference.FILENAME.value: filename,
    }

    data = None

    if raw_file is not None:

        decoded = decode_raw_file(raw_file)
        fasta = SeqIO.parse(StringIO(decoded), "fasta")
        records = [record for record in fasta]

        if records is not None and any(records):
            data = records[0].seq._data
            if any([residue not in protein.letters for residue in data]) or len(data) == 0:
                result[LayoutFieldsReference.INVALID.value] = True
                result[LayoutFieldsReference.HEAD_COLOR.value] = 'danger'
                result[LayoutFieldsReference.VALID.value] = False
            else:
                result[LayoutFieldsReference.INVALID.value] = False
                result[LayoutFieldsReference.HEAD_COLOR.value] = 'success'
                result[LayoutFieldsReference.VALID.value] = True
        else:
            result[LayoutFieldsReference.INVALID.value] = True
            result[LayoutFieldsReference.HEAD_COLOR.value] = 'danger'
            result[LayoutFieldsReference.VALID.value] = False

    return data, result[LayoutFieldsReference.INVALID.value], result[LayoutFieldsReference.VALID.value], \
           result[LayoutFieldsReference.FILENAME.value], result[LayoutFieldsReference.HEAD_COLOR.value]
