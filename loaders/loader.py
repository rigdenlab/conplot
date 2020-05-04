import abc

ABC = abc.ABCMeta('ABC', (object,), {})


class Loader(ABC):
    """Loader abstract class
    This class contains general methods and data structures to extract information from the the user input
    """

    def __init__(self, filename, raw_file, input_format=None):

        self.raw_file = raw_file
        self.filename = filename
        self.input_format = input_format
        self.data = None

    @abc.abstractmethod
    def parse(self):
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
    def head_color(self):
        if self.raw_file is not None and not self.valid:
            return 'danger'
        elif self.raw_file is not None:
            return 'success'
        else:
            return 'dark'

    @property
    def invalid(self):
        if self.raw_file is not None and not self.valid:
            return True
        else:
            return False

    def load(self):
        if self.raw_file is not None:
            self.parse()
