from Bio.PDB import PDBParser as BioPDBParser
import io
import itertools
from operator import itemgetter
from utils.exceptions import InvalidFormat

VALID_AMINOACIDS = {"A", "R", "N", "D", "C", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "M", "F", "P", "O", "S", "U",
                    "T", "W", "Y", "V", "B", "Z", "X", "X", "J"}


def get_chain_contacts(chain):
    """Credits to Felix Simkovic; code taken from GitHub rigdenlab/conkit/conkit/io/pdb.py"""
    contacts = []
    residue_range = list(range(1, len(chain) + 1))
    assert len(residue_range) == len(chain)
    iterator = itertools.product(list(zip(residue_range, chain)), list(zip(residue_range, chain)))
    for (resseq1_alt, residue1), (resseq2_alt, residue2) in iterator:
        seq_distance = int(residue1.id[1]) - int(residue2.id[1])
        if seq_distance <= 4:
            continue
        for atom1, atom2 in itertools.product(residue1, residue2):
            xyz_distance = atom1 - atom2
            if xyz_distance > 20:
                d_bin = 9
            elif xyz_distance <= 4:
                d_bin = 0
            else:
                d_bin = int(round((xyz_distance - 4) / 2, 0))
            if xyz_distance < 8:
                contact = (int(residue1.id[1]), int(residue2.id[1]), round(1.0 - (xyz_distance / 100), 6), d_bin, 1)
            else:
                contact = (int(residue1.id[1]), int(residue2.id[1]), 0, d_bin, 1)
            contacts.append(contact)
    return contacts


def remove_atoms(chain):
    """Credits to Felix Simkovic; code taken from GitHub rigdenlab/conkit/conkit/io/pdb.py"""
    for residue in chain.copy():
        if residue.id[0].strip() and residue.resname not in VALID_AMINOACIDS:
            chain.detach_child(residue.id)
            continue
        for atom in residue.copy():
            # if atom.is_disordered():
            #    chain[residue.id].detach_child(atom.id)
            if residue.resname == "GLY" and atom.id == "CA":
                continue
            elif atom.id != "CB":
                chain[residue.id].detach_child(atom.id)


def PDBParser(input, input_format=None):
    try:
        parser = BioPDBParser().get_structure('pdb', io.StringIO(input))
        chain = list(parser.get_chains())[0]
        remove_atoms(chain)
        contacts = get_chain_contacts(chain)
    except:
        raise InvalidFormat('Unable to parse contacts')

    if not contacts:
        raise InvalidFormat('Unable to parse contacts')

    output = ["PDB"]
    output += sorted(contacts, key=itemgetter(2), reverse=True)
    return output
