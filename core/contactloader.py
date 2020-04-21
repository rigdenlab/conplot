import conkit.io
from .loader import Loader
import base64


class ContactLoader(Loader):
    """Class with methods and data structures to store all the information related with a given contact map and
    its validity"""

    def __init__(self):

        super(ContactLoader, self).__init__()
        self.cmap = None

    def load(self):
        if self.input_format is None:
            return
        elif self.raw_text is not None:
            self.parse_text(self.raw_text)
            if not self.valid_text and self.raw_file is not None:
                self.parse_file()
        elif self.raw_file is not None:
            self.parse_file()

    def parse_text(self, text):

        text = text.split('\n')

        self.cmap = self.parse_map(text, self.input_format)

        if self.valid:
            self.valid_text = True
        else:
            self.valid_text = False

    def parse_file(self):
        content_type, content_string = self.raw_file.split(',')
        decoded = base64.b64decode(content_string)
        contents = str(decoded)
        self.cmap = self.parse_map(contents.split('\\n'), self.input_format)
        if self.valid:
            self.valid_file = True
        else:
            self.valid_file = False

    @property
    def valid(self):
        if self.cmap is not None and len(self.cmap) != 0:
            return True
        else:
            return False

    @property
    def format_selected(self):
        if self.input_format is not None:
            return None
        else:
            return 'danger'

    @property
    def layout_states(self):
        return self.valid_text, self.invalid_text, self.invalid, self.valid_file, self.filename, self.format_selected

    @property
    def datatype(self):
        return 'Contact Map'

    @staticmethod
    def parse_map(text, cmap_format):
        try:
            parser = conkit.io.PARSER_CACHE.import_class(cmap_format)()
            cmap = parser.read(f_handle=text)
            return cmap.top_map
        except:
            return None
