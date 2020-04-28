from .parser import Parser
from index.statesindex import ConservationStates


class ConsurfParser(Parser):

    def __init__(self, input):
        super(ConsurfParser, self).__init__(input)

    def parse(self):
        contents = self.input.split('\n')
        self.output = []

        for line in contents:

            line = line.lstrip().split()

            if len(line) < 4 or not line[0].isnumeric() or not line[3][0].isnumeric():
                continue
            else:
                score = int(line[3][0])

            if score <= 3:
                self.output.append(ConservationStates.VARIABLE)
            elif score < 7:
                self.output.append(ConservationStates.AVERAGE)
            elif score >= 7:
                self.output.append(ConservationStates.CONSERVED)

        if not self.output:
            self.error = True
            self.output = None
