from loaders import decode_raw_file
from parsers import ParserFormats, ContactFormats
from utils.exceptions import InvalidFormat
from utils import compress_data


def Loader(raw_file, input_format):
    data = None
    invalid = False

    if raw_file is not None:
        decoded = decode_raw_file(raw_file)
        try:
            if input_format in ContactFormats.__members__ and input_format != ContactFormats.CCMPRED.name:
                data_raw = ParserFormats.__dict__[input_format](decoded, input_format)
            else:
                data_raw = ParserFormats.__dict__[input_format](decoded)
            data = compress_data(data_raw)
        except InvalidFormat:
            data = None
            invalid = True

    return data, invalid
