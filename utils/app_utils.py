import components
import layouts
from utils import UrlIndex
from utils import decompress_data, compress_data
from utils import sql_utils


def change_password(new_password, old_password, cache, session_id, logger):
    username = decompress_data(cache.hget(session_id, 'user'))
    if sql_utils.change_password(username, old_password, new_password):
        logger.info('Session {} user {} changed password'.format(session_id, username))
        return components.SuccessChangePasswordAlert(username)
    else:
        return components.FailChangePasswordAlert(username)


def create_user(username, password, email, session_id, cache, logger):
    if any([True for x in (username, password, email) if x is None or x == '']):
        return True, None
    elif sql_utils.create_user(username, password, email):
        logger.info('Session {} created user {} - {}'.format(session_id, username, email))
        cache.hset(session_id, 'user', compress_data(username))
        return False, components.SuccessCreateUserAlert(username)
    else:
        return True, None


def user_logout(session_id, cache, logger):
    cache.hdel(session_id, 'user')
    cache.hdel(session_id, 'session_name')
    logger.info('Session {} logout user'.format(session_id))
    return components.SuccessLogoutAlert()


def user_login(username, password, session_id, cache, logger):
    if sql_utils.userlogin(username, password):
        logger.info('Session {} login user {}'.format(session_id, username))
        cache.hset(session_id, 'user', compress_data(username))
        return False, components.SuccessLoginAlert(username)
    else:
        return True, None


def serve_url(url, session_id, cache, logger):
    if cache.hexists(session_id, 'user'):
        username = decompress_data(cache.hget(session_id, 'user'))
    else:
        username = None

    if url == UrlIndex.HOME.value or url == UrlIndex.ROOT.value:
        return layouts.Home(session_id, username)
    elif url == UrlIndex.CONTACT.value:
        return layouts.Contact(session_id, username)
    elif url == UrlIndex.PLOT.value:
        return layouts.Plot(session_id, username)
    elif url == UrlIndex.HELP.value:
        return layouts.Help(session_id, username)
    elif url == UrlIndex.RIGDEN.value:
        return layouts.RigdenLab(session_id, username)
    elif url == UrlIndex.USERS_PORTAL.value:
        return layouts.UsersPortal(username)
    elif url == UrlIndex.CREATE_USER.value:
        return layouts.CreateUser(username)
    elif url == UrlIndex.CHANGE_PASSWORD.value:
        return layouts.ChangeUserPassword(username)
    elif url == UrlIndex.USER_STORAGE.value:
        if cache.hexists(session_id, 'session_name'):
            return layouts.UserStorage(username, decompress_data(cache.hget(session_id, 'session_name')))
        else:
            return layouts.UserStorage(username)
    else:
        logger.error('404 page not found {}'.format(url))
        return layouts.noPage(url, username)
