from operator import attrgetter
import components
from utils.exceptions import UserDoesntExist
import loaders
import uuid
from utils import decompress_data, compress_data
from utils import sql_utils


def get_current_info(session_id, cache):
    username = decompress_data(cache.hget(session_id, 'user'))
    if cache.hexists(session_id, 'session_pkid'):
        current_session_pkid = cache.hget(session_id, 'session_pkid')
    else:
        current_session_pkid = None

    return username, current_session_pkid


def load_session(username, selected_session_pkid, session_id, cache, logger):
    owner_user, session_name, loaded_session = sql_utils.retrieve_session(selected_session_pkid)
    logger.info('Session {} user {} loads session {} - {} - {}'
                ''.format(session_id, username, owner_user, session_name, selected_session_pkid))

    cache.hset(session_id, 'session_pkid', selected_session_pkid)
    for dataset in loaders.DatasetReference:
        if dataset.value in loaded_session:
            cache.hset(session_id, dataset.value, loaded_session[dataset.value])
        else:
            cache.hdel(session_id, dataset.value)

    toast = components.SuccesfulSessionLoadToast(session_name)
    stored_div = components.SessionList(username, components.SessionListType.STORED, selected_session_pkid)
    shared_div = components.SessionList(username, components.SessionListType.SHARED, selected_session_pkid)
    return toast, stored_div, shared_div


def delete_session(selected_session_pkid, current_session_pkid, session_id, logger):
    username, session_name = sql_utils.delete_session(selected_session_pkid)
    logger.info('Session {} user {} deleted session {}'.format(session_id, username, session_name))
    toast = components.SuccesfulSessionDeleteToast(session_name)
    stored_div = components.SessionList(username, components.SessionListType.STORED, current_session_pkid)
    shared_div = components.SessionList(username, components.SessionListType.SHARED, current_session_pkid)
    return toast, stored_div, shared_div


def stop_share_session(username, selected_session_pkid, current_session_pkid, session_id, logger):
    sql_utils.stop_sharing_session(selected_session_pkid, username)
    logger.info('Session {} user {} stop sharing session {}'.format(session_id, username, selected_session_pkid))
    toast = components.SuccesfulSessionStopShareToast()
    stored_div = components.SessionList(username, components.SessionListType.STORED, current_session_pkid)
    shared_div = components.SessionList(username, components.SessionListType.SHARED, current_session_pkid)
    return toast, stored_div, shared_div


def share_session(session_pkid, share_with, logger):
    if session_pkid in map(attrgetter('pkid'), sql_utils.list_sessions(share_with, components.SessionListType.SHARED)):
        return components.SessionAlreadyShared(share_with)

    try:
        sql_utils.share_session(session_pkid, share_with)
        logger.info('Session {} shared with {}'.format(session_pkid, share_with))
        return components.SuccesfulSessionShareToast(share_with)
    except UserDoesntExist:
        return components.FailedSessionShareToast(share_with)


def store_session(session_name, session_id, cache, logger):
    username = decompress_data(cache.hget(session_id, 'user'))
    session = cache.hgetall(session_id)

    if not session_name:
        return components.SessionStoreModal(None)

    logger.info('Session {} user {} stores new session {}'.format(session_id, username, session_name))
    session_pkid = sql_utils.store_session(username, session_name, session)
    cache.hset(session_id, 'session_pkid', session_pkid)

    return components.SessionStoreModal(session_name)


def decompress_session(session):
    for key in (b'id', b'user', b'session_pkid'):
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
