import base64
from Bio import SeqIO
from Bio.Alphabet.IUPAC import protein
from io import StringIO
from loaders.loader import Loader
from loaders import DatasetReference


class SequenceLoader(Loader):
    """Class with methods and data structures to store all the information related with a given sequence and
    its validity"""

    def __init__(self, *args, **kwargs):
        super(SequenceLoader, self).__init__(*args, **kwargs)

    def parse(self):
        content_type, content_string = self.raw_file.split(',')
        decoded = base64.b64decode(content_string)
        decoded = decoded.decode()
        contents = decoded
        fasta = SeqIO.parse(StringIO(contents), "fasta")
        records = [record for record in fasta]

        if records is not None and any(records):
            self.data = records[0].seq._data
        else:
            self.data = None

    @property
    def valid(self):
        if self.data is None or any([residue not in protein.letters for residue in self.data]) or len(self.data) == 0:
            return False
        else:
            return True

    @property
    def datatype(self):
        return DatasetReference.SEQUENCE

    @property
    def layout_states(self):
        return self.invalid, self.valid, self.filename, self.head_color
