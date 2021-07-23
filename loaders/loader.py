from loaders import decode_raw_file
from parsers import ParserFormats, BinaryFormats
from utils.exceptions import InvalidFormat
from utils import compress_data


def Loader(raw_file, input_format):
    data = None
    invalid = False

    if raw_file is not None:
        try:
            if input_format not in BinaryFormats.__members__.keys():
                decoded = decode_raw_file(raw_file)
                data_raw = ParserFormats.__dict__[input_format](decoded, input_format)
            else:
                data_raw = ParserFormats.__dict__[input_format](raw_file, input_format)
            data = compress_data(data_raw)
        except (InvalidFormat, UnicodeDecodeError) as e:
            data = None
            invalid = True

    return data, invalid