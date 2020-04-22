from Bio import SeqIO
from Bio.Alphabet.IUPAC import protein
from io import StringIO
import base64
from .loader import Loader
from conkit.core import Sequence


class SequenceLoader(Loader):
    """Class with methods and data structures to store all the information related with a given sequence and
    its validity"""

    def __init__(self):
        super(SequenceLoader, self).__init__()
        self.records = []

    def parse_text(self, text):

        fasta = SeqIO.parse(StringIO(text), "fasta")
        self.records = [record for record in fasta]

        if self.valid:
            self.valid_text = True
        else:
            self.valid_text = False

    def parse_file(self):

        content_type, content_string = self.raw_file.split(',')
        decoded = base64.b64decode(content_string)
        decoded = decoded.decode()
        contents = decoded
        fasta = SeqIO.parse(StringIO(contents), "fasta")
        self.records = [record for record in fasta]

        if self.valid:
            self.valid_file = True
        else:
            self.valid_file = False

    # TODO : Need to figure out how to read it directly with conkit instead of biopython
    @property
    def sequence(self):
        if any(self.records):
            return Sequence('seq', self.records[0].seq)
        else:
            return None

    @property
    def valid(self):
        if self.sequence is None or any([residue not in protein.letters for residue in self.sequence.seq]) or \
                len(self.sequence) == 0:
            return False
        else:
            return True

    @property
    def datatype(self):
        return 'Sequence'

    @property
    def layout_states(self):
        return self.valid_text, self.invalid_text, self.invalid, self.valid_file, self.filename, self.head_color
