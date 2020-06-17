from enum import Enum
import json
import gzip
from io import BytesIO


class CacheKeys(Enum):
    ID = 'id'
    USER = 'user'
    SESSION_PKID = 'session_pkid'
    GRAPH = 'graph'
    CONTACT_DATA = 'contact_data'
    CONTACT_FNAMES = 'contact_fnames'
    CUSTOM_DATA = 'custom_data'
    CUSTOM_FNAMES = 'custom_fnames'
    SEQUENCE_DATA = 'sequence_data'
    SEQUENCE_FNAME = 'sequence_fname'
    MEMBDANRE_TOPOLOGY_DATA = 'membranetopology_data'
    MEMBRANE_TOPOLOGY_FNAMES = 'membranetopology_fnames'
    SECONDARY_STRUCTURE_DATA = 'secondarystructure_data'
    SECONDARY_STRUCTURE_FNAMES = 'secondarystructure_fnames'
    CONSERVATION_DATA = 'conservation_data'
    CONSERVATION_FNAMES = 'conservation_fnames'
    DISORDER_DATA = 'disorder_data'
    DISORDER_FNAMES = 'disorder_fnames'


def compress_data(data_raw):
    data_json = json.dumps(data_raw)
    return compressStringToBytes(data_json)


def decompress_data(data_compressed):
    decompressed = decompressBytesToString(data_compressed)
    return json.loads(decompressed)


def compressStringToBytes(inputString):
    """
    read the given string, encode it in utf-8,
    compress the data and return it as a byte array.
    """
    bio = BytesIO()
    bio.write(inputString.encode("utf-8"))
    bio.seek(0)
    stream = BytesIO()
    compressor = gzip.GzipFile(fileobj=stream, mode='w')
    while True:  # until EOF
        chunk = bio.read(8192)
        if not chunk:  # EOF?
            compressor.close()
            return stream.getvalue()
        compressor.write(chunk)


def decompressBytesToString(inputBytes):
    """
    decompress the given byte array (which must be valid
    compressed gzip data) and return the decoded text (utf-8).
    """
    bio = BytesIO()
    stream = BytesIO(inputBytes)
    decompressor = gzip.GzipFile(fileobj=stream, mode='r')
    while True:  # until EOF
        chunk = decompressor.read(8192)
        if not chunk:
            decompressor.close()
            bio.seek(0)
            return bio.read().decode("utf-8")
        bio.write(chunk)
    return None
