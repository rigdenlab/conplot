from .parser import Parser


class PsipredParser(Parser):

    def __init__(self, input):
        super(PsipredParser, self).__init__(input)

    def parse(self):
        contents = self.input.split('\n')
        output = []

        for line in contents:
            line = line.split()
            if line[0] == '#':
                continue
            output.append(line[2])

        if any([residue not in ('H', 'C', 'E') for residue in self.output]):
            self.error = True
            self.output = None
        else:
            self.output = output
