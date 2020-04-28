from .parser import Parser
from index.statesindex import DisorderStates


class IupredParser(Parser):

    def __init__(self, input):
        super(IupredParser, self).__init__(input)

    def parse(self):
        contents = self.input.split('\n')
        self.output = []

        for line in contents:

            line = line.lstrip().split()
            if len(line) < 1 or line[0] == '#' or len(line) < 3:
                continue
            else:
                try:
                    score = float(line[2])
                except ValueError:
                    self.error = True
                    self.output = None
                    return

            if score >= 0.5:
                self.output.append(DisorderStates.DISORDER)
            else:
                self.output.append(DisorderStates.ORDER)

        if not self.output:
            self.error = True
            self.output = None
