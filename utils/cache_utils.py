from enum import Enum
import json
import gzip
import loaders
from io import BytesIO


class CacheKeys(Enum):
    ID = 'id'
    USER = 'user'
    SESSION_PKID = 'session_pkid'
    SEQUENCE_HYDROPHOBICITY = 'hydro'
    FIGURE_JSON = 'figure_json'
    DISPLAY_CONTROL_JSON = 'display_control_json'
    CONTACT_MAP = loaders.DatasetReference.CONTACT_MAP.value
    CUSTOM = loaders.DatasetReference.CUSTOM.value
    SEQUENCE = loaders.DatasetReference.SEQUENCE.value
    MEMBRANE_TOPOLOGY = loaders.DatasetReference.MEMBRANE_TOPOLOGY.value
    SECONDARY_STRUCTURE = loaders.DatasetReference.SECONDARY_STRUCTURE.value
    CONSERVATION = loaders.DatasetReference.CONSERVATION.value
    DISORDER = loaders.DatasetReference.DISORDER.value


def store_fname(cache, session_id, fname, cache_key):
    fname_list = cache.hget(session_id, cache_key)

    if not fname_list:
        cache.hset(session_id, cache_key, compress_data([fname]))
    else:
        fname_list = decompress_data(fname_list)
        fname_list.append(fname)
        cache.hset(session_id, cache_key, compress_data(fname_list))


def remove_fname(cache, session_id, fname, cache_key):
    fname_list = cache.hget(session_id, cache_key)

    if not fname_list:
        return
    elif cache_key == CacheKeys.SEQUENCE.value:
        cache.hdel(session_id, cache_key)
        cache.hdel(session_id, CacheKeys.SEQUENCE_HYDROPHOBICITY.value)
        return

    fname_list = decompress_data(fname_list)
    if fname in fname_list:
        index = fname_list.index(fname)
        del fname_list[index]
        cache.hset(session_id, cache_key, compress_data(fname_list))


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


def store_figure(session_id, figure_json, display_json, cache):
    cache.hset(session_id, CacheKeys.FIGURE_JSON.value, compress_data(figure_json))
    cache.hset(session_id, CacheKeys.DISPLAY_CONTROL_JSON.value, compress_data(display_json))


def clear_cache(session_id, cache):
    remove_datasets(session_id, cache)
    remove_figure(session_id, cache)
    remove_sequence(session_id, cache)


def remove_datasets(session_id, cache):
    for dataset in loaders.DatasetReference.exclude_seq():
        if cache.hexists(session_id, dataset.value):
            fname_list = decompress_data(cache.hget(session_id, dataset.value))
            if fname_list:
                for fname in fname_list:
                    cache.hdel(session_id, fname)
            cache.hdel(session_id, dataset.value)


def remove_figure(session_id, cache):
    if cache.hexists(session_id, CacheKeys.FIGURE_JSON.value):
        cache.hdel(session_id, CacheKeys.FIGURE_JSON.value)
        cache.hdel(session_id, CacheKeys.DISPLAY_CONTROL_JSON.value)


def remove_sequence(session_id, cache):
    if cache.hexists(session_id, CacheKeys.SEQUENCE.value):
        cache.hdel(session_id, decompress_data(cache.hget(session_id, CacheKeys.SEQUENCE.value)))
        cache.hdel(session_id, CacheKeys.SEQUENCE.value)
        cache.hdel(session_id, CacheKeys.SEQUENCE_HYDROPHOBICITY.value)


def is_redis_available(cache):
    try:
        cache.ping()
        return True
    except:
        return False

def get_active_sessions(cache):
    return cache.dbsize()