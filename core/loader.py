import abc

ABC = abc.ABCMeta('ABC', (object,), {})


class Loader(ABC):
    """Loader abstract class
    This class contains general methods and data structures to extract information from the the user input
    """

    def __init__(self):
        self.raw_file = None
        self.filename = None
        self.valid_file = False
        self.raw_text = None
        self.valid_text = False
        self.input_format = None

    @abc.abstractmethod
    def parse_file(self):
        pass

    @abc.abstractmethod
    def parse_text(self, text):
        pass

    @property
    @abc.abstractmethod
    def layout_states(self):
        pass

    @property
    @abc.abstractmethod
    def valid(self):
        pass

    @property
    @abc.abstractmethod
    def datatype(self):
        pass

    @property
    def invalid(self):
        if self.raw_file is not None or self.raw_text is not None:
            if not self.valid:
                return True
        else:
            return False

    @property
    def filename_alert_open(self):
        if self.filename is None:
            return False
        else:
            return True

    @property
    def invalid_text(self):
        if self.raw_text is not None and not self.valid_text:
            return True
        else:
            return False

    def clear(self):
        self.filename = None
        self.raw_file = None
        self.valid_file = False

    def register_input(self, raw_text, raw_file, filename, input_format=None):
        self.input_format = input_format
        self.raw_text = raw_text
        if raw_file is not None:
            self.raw_file = raw_file
        if filename is not None:
            self.filename = filename

    def load(self):
        if self.raw_text is not None:
            self.parse_text(self.raw_text)
            if not self.valid_text and self.raw_file is not None:
                self.parse_file()
        elif self.raw_file is not None:
            self.parse_file()
