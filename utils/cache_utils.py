from enum import Enum
import json
import gzip
import loaders
from io import BytesIO


class CacheKeys(Enum):
    ID = 'id'
    USER = 'user'
    SESSION_PKID = 'session_pkid'
    FIGURE_JSON = 'figure_json'
    DISPLAY_CONTROL_JSON = 'display_control_json'
    CONTACT_MAP = loaders.DatasetReference.CONTACT_MAP.value
    CONTACT_DENSITY = loaders.DatasetReference.CONTACT_DENSITY.value
    CONTACT_DIFF = loaders.DatasetReference.CONTACT_DIFF.value
    CUSTOM = loaders.DatasetReference.CUSTOM.value
    SEQUENCE = loaders.DatasetReference.SEQUENCE.value
    SEQUENCE_HYDROPHOBICITY = loaders.DatasetReference.HYDROPHOBICITY.value
    MEMBRANE_TOPOLOGY = loaders.DatasetReference.MEMBRANE_TOPOLOGY.value
    SECONDARY_STRUCTURE = loaders.DatasetReference.SECONDARY_STRUCTURE.value
    CONSERVATION = loaders.DatasetReference.CONSERVATION.value
    DISORDER = loaders.DatasetReference.DISORDER.value
    CMAP_DENSITY = '{}_CONPLOT-INTERNAL-USE-ONLY-METADATA-DENSITY-TAG_{}'
    CMAP_DIFF = '{}_{}_CONPLOT-INTERNAL-USE-ONLY-METADATA-DIFF-TAG_{}'
    PROTECETED_TAG = 'CONPLOT-INTERNAL-USE-ONLY-METADATA'


class MetadataTags(Enum):
    DENSITY = ' - density'
    HYDROPHOBICITY = ' - hydrophobicity'
    DIFF = ' - diff'
    SEPARATOR = '|'
    HYPHEN = '---'
    TAG = 'CONPLOT-INTERNAL-USE-ONLY-METADATA'


def retrieve_data(session_id, cachekey, cache):
    density = cache.hget(session_id, cachekey)
    return decompress_data(density)


def store_data(session_id, cachekey, data, dataset, cache):
    cache.hset(session_id, cachekey, compress_data(data))
    store_fname(cache, session_id, cachekey.decode(), dataset)


def remove_all(session_id, dataset, cache):
    cachekey_list = cache.hget(session_id, dataset)
    if not cachekey_list:
        return

    cachekey_list = decompress_data(cachekey_list)
    for cachekey in cachekey_list:
        cache.hdel(session_id, cachekey)

    cache.hdel(session_id, dataset)


def remove_density(session_id, cache, fname):
    density_list = cache.hget(session_id, CacheKeys.CONTACT_DENSITY.value)
    if not density_list:
        return
    density_list = decompress_data(density_list)

    density_cachekey = '{}_{}'.format(fname, CacheKeys.PROTECETED_TAG.value)
    for density in density_list:
        if density_cachekey in density:
            cache.hdel(session_id, density)
    density_list = [density for density in density_list if density_cachekey not in density]
    cache.hset(session_id, CacheKeys.CONTACT_DENSITY.value, compress_data(density_list))


def remove_diff(session_id, cache, fname):
    diff_list = cache.hget(session_id, CacheKeys.CONTACT_DIFF.value)
    if not diff_list:
        return
    diff_list = decompress_data(diff_list)

    for diff in diff_list:
        if fname in diff:
            cache.hdel(session_id, diff)
    diff_list = [diff for diff in diff_list if fname not in diff]
    cache.hset(session_id, CacheKeys.CONTACT_DIFF.value, compress_data(diff_list))


def is_valid_fname(fname):
    if any([x for x in CacheKeys if x.value == fname]) or any([tag for tag in MetadataTags if tag.value in fname]):
        return False
    return True


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
    remove_all(session_id, CacheKeys.CONTACT_DENSITY.value, cache)
    remove_all(session_id, CacheKeys.CONTACT_DIFF.value, cache)


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


def get_cachekey(session, fname, factor):
    if 'PDB' == session[fname.encode()][0]:
        return CacheKeys.CMAP_DENSITY.value.format(fname, fname).encode()
    else:
        return CacheKeys.CMAP_DENSITY.value.format(fname, factor).encode()
