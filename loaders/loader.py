from loaders import decode_raw_file, LayoutFieldsReference
from parsers import ParserFormats, InvalidFormat


def Loader(filename, raw_file, input_format):
    result = {
        LayoutFieldsReference.VALID.value: False,
        LayoutFieldsReference.INVALID.value: False,
        LayoutFieldsReference.HEAD_COLOR.value: 'dark',
        LayoutFieldsReference.FILENAME.value: filename,
    }

    data = None

    if raw_file is not None:
        decoded = decode_raw_file(raw_file)
        try:
            data = ParserFormats.__dict__[input_format](decoded)
            result[LayoutFieldsReference.INVALID.value] = False
            result[LayoutFieldsReference.HEAD_COLOR.value] = 'success'
            result[LayoutFieldsReference.VALID.value] = True
        except InvalidFormat:
            pass

    return data, result[LayoutFieldsReference.INVALID.value], result[LayoutFieldsReference.VALID.value], \
           result[LayoutFieldsReference.FILENAME.value], result[LayoutFieldsReference.HEAD_COLOR.value]
