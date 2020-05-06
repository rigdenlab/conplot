from loaders import decode_raw_file
from parsers import ParserFormats
from utils.exceptions import InvalidFormat


def Loader(raw_file, input_format):
    data = None
    invalid = False

    if raw_file is not None:
        decoded = decode_raw_file(raw_file)
        try:
            data = ParserFormats.__dict__[input_format](decoded)
        except InvalidFormat:
            data = None
            invalid = True

    return data, invalid
