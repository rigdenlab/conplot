import conkit.io
import base64
from loaders.loader import Loader
from loaders import DatasetReference
from io import StringIO


class ContactLoader(Loader):
    """Class with methods and data structures to store all the information related with a given contact map and
    its validity"""

    def __init__(self, *args, **kwargs):
        super(ContactLoader, self).__init__(*args, **kwargs)

    def parse(self):
        content_type, content_string = self.raw_file.split(',')
        decoded = base64.b64decode(content_string).decode()
        cmap = self.parse_map(StringIO(decoded), self.input_format)

        if cmap is not None and len(cmap) != 0:

            cmap = cmap.remove_neighbors(inplace=False)
            cmap.sort('raw_score', reverse=True, inplace=True)
            self.data = []
            for contact in cmap:
                self.data.append((contact.res1_seq, contact.res2_seq, contact.raw_score))

    @property
    def valid(self):
        if self.data is not None and len(self.data) != 0:
            return True
        else:
            return False

    @property
    def layout_states(self):
        return self.invalid, self.valid, self.filename, self.head_color

    @property
    def datatype(self):
        return DatasetReference.CONTACT_MAP

    @staticmethod
    def parse_map(fhandle, cmap_format):
        try:
            parser = conkit.io.PARSER_CACHE.import_class(cmap_format)()
            cmap = parser.read(f_handle=fhandle)
            return cmap.top_map
        except:
            return None
