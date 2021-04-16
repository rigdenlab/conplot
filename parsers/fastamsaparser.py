from utils.exceptions import InvalidFormat


def extract_sequences(input):
    try:
        sequences = []
        for line in input.split('\n'):
            if len(line) > 1 and line.rstrip().lstrip()[0] != ">" and line.rstrip().lstrip()[0] != "#":
                sequences.append(line.rstrip().lstrip())
        seq_lenght = len(sequences.pop(0))
        n_sequences = len(sequences) / 10
    except IndexError:
        return None

    return sequences, seq_lenght, n_sequences


def FastaMsaParser(input, input_format=None):
    sequences, seq_lenght, n_sequences = extract_sequences(input)
    if sequences is None or len(sequences) <= 1 or n_sequences < 0.1 or seq_lenght < 1:
        raise InvalidFormat('Unable to parse contents of A3M MSA file')

    residue_count = [0 for x in range(1, seq_lenght + 1)]
    try:
        for sequence in sequences:
            if len(sequence) != seq_lenght:
                raise InvalidFormat('Unable to parse the A3M MSA file')
            idx = 0
            for residue in sequence:
                if residue != '-' and residue != '.':
                    residue_count[idx] += 1
                idx += 1
    except IndexError:
        raise InvalidFormat('Unable to parse the A3M MSA file')

    norm = [int(round(x / n_sequences)) for x in residue_count]
    return norm
