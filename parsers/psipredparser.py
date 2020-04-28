from .parser import Parser
from index.statesindex import SecondaryStructureStates


class PsipredParser(Parser):

    def __init__(self, input):
        super(PsipredParser, self).__init__(input)

    def parse(self):
        contents = self.input.split('\n')
        self.output = []

        for line in contents:
            line = line.split()
            if len(line) != 6 or line[0] == '#':
                continue
            elif line[2] == 'H':
                self.output.append(SecondaryStructureStates.HELIX)
            elif line[2] == 'C':
                self.output.append(SecondaryStructureStates.COIL)
            elif line[2] == 'E':
                self.output.append(SecondaryStructureStates.SHEET)
            else:
                self.error = True
                self.output = None
                return
