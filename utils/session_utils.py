import uuid
import json
from utils import decompressBytesToString, compressStringToBytes
from utils.exceptions import SessionTimeOut


def initiate_session():
    session_id = str(uuid.uuid4())
    session = {}
    compressed_session = compress_session(session)
    return session_id, compressed_session


def decompress_session(compressed_session):
    decompressed = decompressBytesToString(compressed_session)
    try:
        json.loads(decompressed)
    except json.decoder.JSONDecodeError:
        raise SessionTimeOut
    return json.loads(decompressed)


def compress_session(session):
    session_json = json.dumps(session)
    return compressStringToBytes(session_json)
