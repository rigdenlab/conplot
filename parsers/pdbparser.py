import io
import conkit.io
from operator import itemgetter
from utils import unique_by_key
from utils.exceptions import InvalidFormat


def PDBParser(input):
    try:
        parser = conkit.io.PARSER_CACHE.import_class('pdb')()
        cmap = parser.read(f_handle=io.StringIO(input))
        cmap = cmap.top_map
        cmap.remove_neighbors(inplace=True)
        cmap.sort('raw_score', reverse=True, inplace=True)
    except:
        raise InvalidFormat('Unable to parse contacts')

    output = [(tuple(sorted([contact.res1_seq, contact.res2_seq], reverse=True)), contact.raw_score)
              for contact in cmap]
    if not output:
        raise InvalidFormat('Unable to parse contacts')
    else:
        unique_contacts = unique_by_key(output, key=itemgetter(0))
        output = [(*contact[0], contact[1]) for contact in unique_contacts]
        output = sorted(output, key=itemgetter(2), reverse=True)
        return output
