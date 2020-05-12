from utils.exceptions import InvalidFormat
from operator import itemgetter
import re

RE_SPLIT = re.compile(r'\s+')

def EvfoldParser(input):
    contents = input.split('\n')
    output = []

    for line in contents:
        line = line.strip()
        if line:
            res1_seq, res1, res2_seq, res2, _, raw_score = RE_SPLIT.split(line)
            output.append((int(res1_seq), int(res2_seq), float(raw_score)))

    if not output:
        raise InvalidFormat('Unable to parse contacts')
    else:
        output = sorted(output, key=itemgetter(2), reverse=True)
        return tuple(output)

#test=open('/Users/shahrammesdaghi/Downloads/w9dy28.evfold','r')
#text = test.read()
#print(EvfoldParser(text))