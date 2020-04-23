import abc

ABC = abc.ABCMeta('ABC', (object,), {})


class Parser(ABC):
    """Parser abstract class
    This class contains general methods and data structures to parse and hold information from the input files
    """

    def __init__(self, input):
        self.input = input
        self.output = None
        self.error = False

    @abc.abstractmethod
    def parse(self):
        pass
