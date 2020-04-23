from .parser import Parser


class TopconsParser(Parser):

    def __init__(self, input):
        super(TopconsParser, self).__init__(input)

    def parse(self):
        contents = self.input.split('\n')
        try:
            topcons_prediction = contents[contents.index('TOPCONS predicted topology:') + 1].rstrip()
            self.output = topcons_prediction.rstrip().lstrip()
            if any([residue not in ('i', 'o', 'M') for residue in self.output]):
                self.error = True
        except ValueError as e:
            self.output = None
            self.error = True
