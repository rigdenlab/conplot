from loaders import decode_raw_file
from parsers import ParserFormats, ContactInformationFormats
from utils.exceptions import InvalidFormat
from utils import compress_data


def Loader(raw_file, input_format):
    data = None
    invalid = False

    if raw_file is not None:
        try:
            decoded = decode_raw_file(raw_file)
            if input_format in ContactInformationFormats.__members__ and input_format != ContactInformationFormats.CCMPRED.name \
                    and input_format != ContactInformationFormats.PDB.name:
                data_raw = ParserFormats.__dict__[input_format](decoded, input_format)
            else:
                data_raw = ParserFormats.__dict__[input_format](decoded)
            data = compress_data(data_raw)
        except (InvalidFormat, UnicodeDecodeError) as e:
            data = None
            invalid = True

    return data, invalid
