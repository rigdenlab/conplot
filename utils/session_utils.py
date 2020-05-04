import uuid
import json
from utils import decompressBytesToString, compressStringToBytes, SessionTimeOut


def initiate_session():
    session_id = str(uuid.uuid4())
    session = {}
    compressed_session = compress_session(session)
    return session_id, compressed_session


def decompress_session(compressed_session):
    decompressed = decompressBytesToString(compressed_session)
    if decompressed is None:
        raise SessionTimeOut
    return json.loads(decompressed)


def compress_session(session):
    session_json = json.dumps(session)
    return compressStringToBytes(session_json)
