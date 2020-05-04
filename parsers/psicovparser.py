from parsers.parser import Parser
from operator import itemgetter


class PsicovParser(Parser):

    def __init__(self, input):
        super(PsicovParser, self).__init__(input)

    def parse(self):
        contents = self.input.split('\n')
        self.output = []

        for line in contents:

            line = line.lstrip().split()

            if not line or line[0].isalpha():
                continue
            elif line[0].isdigit():
                if abs(int(line[0]) - int(line[1])) >= 5:
                    self.output.append((int(line[0]), int(line[1]), float(line[4])))

        if not self.output:
            self.error = True
            self.output = None
        else:
            self.output = sorted(self.output, key=itemgetter(2), reverse=True)
            self.output = tuple(self.output)
