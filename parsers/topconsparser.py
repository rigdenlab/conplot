from .parser import Parser
from core.membranetopologyloader import MembraneStates


class TopconsParser(Parser):

    def __init__(self, input):
        super(TopconsParser, self).__init__(input)

    def parse(self):
        contents = self.input.split('\n')

        try:
            topcons_prediction = contents[contents.index('TOPCONS predicted topology:') + 1].rstrip()
        except ValueError as e:
            self.output = None
            self.error = True
            return

        for residue in topcons_prediction.rstrip().lstrip():
            if residue == 'i':
                self.output.append(MembraneStates.INSIDE)
            elif residue == 'o':
                self.output.append(MembraneStates.OUTSIDE)
            elif residue == 'M':
                self.output.append(MembraneStates.INSERTED)
            else:
                self.error = True
                self.output = None
                return
