from parsers.fastamsaparser import extract_sequences
from utils.exceptions import InvalidFormat


def A3mParser(input, input_format=None):
    sequences, seq_lenght, n_sequences = extract_sequences(input)
    if sequences is None or len(sequences) <= 1 or n_sequences < 0.1 or seq_lenght < 1:
        raise InvalidFormat('Unable to parse contents of A3M MSA file')

    residue_count = [0 for x in range(1, seq_lenght + 1)]
    try:
        for sequence in sequences:
            idx = 0
            for residue in sequence:
                if residue.islower():
                    continue
                elif residue != '-':
                    residue_count[idx] += 1
                idx += 1
    except IndexError:
        raise InvalidFormat('Unable to parse the A3M MSA file')

    norm = [int(round(x / n_sequences)) for x in residue_count]
    return norm
