import io
import conkit.io
import gemmi
from operator import itemgetter
from utils import unique_by_key
from utils.exceptions import InvalidFormat


def get_first_chain(structure):
    new_model = gemmi.Model('1')
    new_model.add_chain(structure[0][0].clone())
    new_structure = gemmi.Structure()
    new_structure.add_model(new_model)
    return new_structure.make_minimal_pdb()


def PDBParser(input):
    try:
        structure = gemmi.read_pdb_string(input)
        input_chain = get_first_chain(structure)
        parser = conkit.io.PARSER_CACHE.import_class('pdb')()
        cmap = parser.read(f_handle=io.StringIO(input_chain))
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
