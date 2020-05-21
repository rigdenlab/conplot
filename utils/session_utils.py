import components
import loaders
import uuid
from utils import decompress_data, compress_data
from utils import sql_utils


def get_current_info(session_id, cache):
    username = decompress_data(cache.hget(session_id, 'user'))
    if cache.hexists(session_id, 'session_name'):
        current_session_name = decompress_data(cache.hget(session_id, 'session_name'))
    else:
        current_session_name = None

    return username, current_session_name


def load_session(username, session_name, session_id, cache, logger):
    cache.hset(session_id, 'session_name', compress_data(session_name))
    loaded_session = sql_utils.retrieve_session(username, session_name)
    for dataset in loaders.DatasetReference:
        if dataset.value in loaded_session:
            cache.hset(session_id, dataset.value, loaded_session[dataset.value])
        else:
            cache.hdel(session_id, dataset.value)
    logger.info('Session {} user {} loads session {}'.format(session_id, username, session_name))
    return components.SuccesfulSessionLoadToast(session_name), components.StoredSessionsList(username, session_name)


def delete_session(username, session_name, current_session_name, session_id, logger):
    sql_utils.delete_session(username, session_name)
    logger.info('Session {} user {} deleted session {}'.format(session_id, username, session_name))
    return components.SuccesfulSessionDeleteToast(session_name), \
           components.StoredSessionsList(username, current_session_name)


def store_session(session_name, session_id, cache, logger):
    username = decompress_data(cache.hget(session_id, 'user'))
    session = cache.hgetall(session_id)

    logger.info('Session {} user {} stores new session {}'.format(session_id, username, session_name))
    sql_utils.store_session(username, session_name, session)
    cache.hset(session_id, 'session_name', compress_data(session_name))

    return components.SessionStoreModal(session_name)


def decompress_session(session):
    for key in (b'id', b'user', b'session_name'):
        if key in session:
            del session[key]

    for key in session.keys():
        session[key] = decompress_data(session[key])
        session[key].pop(-1)
    return session


def is_expired_session(session_id, cache, logger, expire_time=900):
    if not cache.exists(session_id):
        logger.info('Session {} has expired'.format(session_id))
        return True
    else:
        cache.expire(session_id, expire_time)
        return False


def initiate_session(cache, logger, expire_time=900):
    session_id = str(uuid.uuid4())
    logger.info('New session initiated {}'.format(session_id))
    cache.hset(session_id, 'id', compress_data(session_id))
    cache.expire(session_id, expire_time)
    return session_id
