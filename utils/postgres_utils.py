import os
from operator import attrgetter
from collections import namedtuple
from components import SessionListType
from enum import Enum
import datetime
import psycopg2
from utils import decompress_data, compress_data
from utils.exceptions import SQLInjectionAlert, UserExists, EmailAlreadyUsed, IntegrityError, UserDoesntExist

SessionData = namedtuple('SessionData', ['pkid', 'name', 'owner', 'date'])


class TableNames(Enum):
    USER_DATA = 'user_data'
    SESSION_DATA = 'session_data'


class SqlFieldNames(Enum):
    ID = 'id'
    OWNER = 'owner_username'
    SESSION_NAME = 'session_name'
    SESSION_JSON = 'session_data'
    USERNAME = 'username'
    EMAIL = 'email'
    PASSWORD = 'password'
    LAST_ACCESS = 'last_access_date'
    CREATED_DATE = 'created_date'
    LAST_LOGIN = 'last_login'
    RECOVERY = 'recovery'
    SHARED = 'shared_with'
    SESSION_PKID = 'session_pkid'


class SqlQueries(Enum):
    CREATE_USER = """INSERT INTO {} ({},{},{}) VALUES (%s, %s,crypt(%s, gen_salt('bf')))""".format(
        TableNames.USER_DATA.value, SqlFieldNames.USERNAME.value, SqlFieldNames.EMAIL.value,
        SqlFieldNames.PASSWORD.value)

    USER_LOGIN = """SELECT {} FROM {} WHERE {} = %s AND {} = crypt(%s, {})
    """.format(SqlFieldNames.ID.value, TableNames.USER_DATA.value, SqlFieldNames.USERNAME.value,
               SqlFieldNames.PASSWORD.value, SqlFieldNames.PASSWORD.value)

    UPDATE_LAST_LOGIN = """UPDATE {} SET {} = %s WHERE {} = %s
    """.format(TableNames.USER_DATA.value, SqlFieldNames.LAST_LOGIN.value, SqlFieldNames.USERNAME.value)

    UPDATE_LAST_ACCESS = """UPDATE {} SET {} = %s WHERE {} = %s
    """.format(TableNames.SESSION_DATA.value, SqlFieldNames.LAST_ACCESS.value, SqlFieldNames.SESSION_PKID.value)

    CHECK_SESSION_EXISTS = """SELECT * FROM {} WHERE {} = %s AND {} = %s
    """.format(TableNames.SESSION_DATA.value, SqlFieldNames.OWNER.value, SqlFieldNames.SESSION_NAME.value)

    CHECK_USER_EXISTS = """SELECT * FROM {} WHERE {} = %s
        """.format(TableNames.USER_DATA.value, SqlFieldNames.USERNAME.value)

    CHECK_EMAIL_USED = """SELECT * FROM {} WHERE {} = %s
            """.format(TableNames.USER_DATA.value, SqlFieldNames.EMAIL.value)

    CHANGE_PASSWORD = """UPDATE {} SET {} = crypt(%s, {}) WHERE {} = %s
    """.format(TableNames.USER_DATA.value, SqlFieldNames.PASSWORD.value, SqlFieldNames.PASSWORD.value,
               SqlFieldNames.USERNAME.value)

    CHECK_IS_RECOVERY = """SELECT {} FROM {} WHERE {} = crypt(%s, {}) AND {} = %s AND {} = %s
    """.format(SqlFieldNames.ID.value, TableNames.USER_DATA.value, SqlFieldNames.RECOVERY.value,
               SqlFieldNames.RECOVERY.value, SqlFieldNames.USERNAME.value, SqlFieldNames.EMAIL.value)

    RESET_RECOVERY = """UPDATE {} SET {} = 'null' WHERE {} = crypt(%s, {}) AND {} = %s AND {} = %s
    """.format(TableNames.USER_DATA.value, SqlFieldNames.RECOVERY.value, SqlFieldNames.RECOVERY.value,
               SqlFieldNames.RECOVERY.value, SqlFieldNames.USERNAME.value, SqlFieldNames.EMAIL.value)

    UPDATE_SESSION = """UPDATE {} SET {} = %s WHERE {} = %s AND {} = %s
    """.format(TableNames.SESSION_DATA.value, SqlFieldNames.SESSION_JSON.value, SqlFieldNames.OWNER.value,
               SqlFieldNames.SESSION_NAME.value)

    INSERT_SESSION = """INSERT INTO {} ({}, {}, {}) VALUES (%s, %s, %s) 
    """.format(TableNames.SESSION_DATA.value, SqlFieldNames.OWNER.value, SqlFieldNames.SESSION_NAME.value,
               SqlFieldNames.SESSION_JSON.value)

    RETRIEVE_SESSION = """SELECT * FROM {} WHERE {} = %s
    """.format(TableNames.SESSION_DATA.value, SqlFieldNames.SESSION_PKID.value)

    UPDATE_SESSION_DATE = """UPDATE {} SET {} = %s WHERE {} = %s 
    """.format(TableNames.SESSION_DATA.value, SqlFieldNames.LAST_ACCESS.value, SqlFieldNames.SESSION_PKID.value)

    LIST_SESSIONS = """SELECT {}, {}, {}, {} FROM {} WHERE {} = %s
    """.format(SqlFieldNames.OWNER.value, SqlFieldNames.SESSION_NAME.value, SqlFieldNames.CREATED_DATE.value,
               SqlFieldNames.SESSION_PKID.value, TableNames.SESSION_DATA.value, SqlFieldNames.OWNER.value)

    DELETE_SESSION = """DELETE FROM {} WHERE {} = %s
    """.format(TableNames.SESSION_DATA.value, SqlFieldNames.SESSION_PKID.value)

    SHARE_SESSION = """UPDATE {} SET {} = array_append({}, %s) WHERE {} = %s
    """.format(TableNames.SESSION_DATA.value, SqlFieldNames.SHARED.value, SqlFieldNames.SHARED.value,
               SqlFieldNames.SESSION_PKID.value)

    STOP_SHARE = """UPDATE {} SET {} = array_remove({}, %s) WHERE {} = %s
    """.format(TableNames.SESSION_DATA.value, SqlFieldNames.SHARED.value, SqlFieldNames.SHARED.value,
               SqlFieldNames.SESSION_PKID.value)

    GET_SHARED_SESSIONS = """SELECT {}, {}, {}, {} FROM {} WHERE %s = ANY({})
    """.format(SqlFieldNames.OWNER.value, SqlFieldNames.SESSION_NAME.value, SqlFieldNames.CREATED_DATE.value,
               SqlFieldNames.SESSION_PKID.value, TableNames.SESSION_DATA.value, SqlFieldNames.SHARED.value)

    GET_SESSION_PKID = """SELECT {} FROM {} WHERE {} = %s AND {} = %s
    """.format(SqlFieldNames.SESSION_PKID.value, TableNames.SESSION_DATA.value, SqlFieldNames.OWNER.value,
               SqlFieldNames.SESSION_NAME.value)

    CHECK_SESSION_OWNER = """SELECT {}, {} FROM {} WHERE {} = %s
    """.format(SqlFieldNames.OWNER.value, SqlFieldNames.SESSION_NAME.value, TableNames.SESSION_DATA.value,
               SqlFieldNames.SESSION_PKID.value)


def is_postgres_available(logger=None):
    try:
        connection = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='disable')
        connection.close()
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        if logger is not None:
            logger.error('Cannot establish connection with postgres database! {}'.format(error))
        return False


def initiate_connection():
    connection = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='disable')
    cursor = connection.cursor()
    return connection, cursor


def perform_query(query, args, fetch=False, commit=False, top=False):
    if ';' in query or ';' in args:
        raise SQLInjectionAlert('SQL injection detected with query %s and values %s' % (query, args))

    result = None
    connection, cursor = initiate_connection()
    cursor.execute(query, args)

    if fetch and top:
        result = cursor.fetchone()
    elif fetch:
        result = cursor.fetchall()

    if commit:
        connection.commit()

    cursor.close()
    connection.close()

    return result


def create_user(username, psswrd, email):
    if any(perform_query(SqlQueries.CHECK_USER_EXISTS.value, args=(username,), fetch=True)):
        raise UserExists
    elif any(perform_query(SqlQueries.CHECK_EMAIL_USED.value, args=(email,), fetch=True)):
        raise EmailAlreadyUsed

    try:
        perform_query(SqlQueries.CREATE_USER.value, args=(username, email, psswrd), commit=True)
    except psycopg2.IntegrityError:
        raise IntegrityError


def change_password(username, old_password, new_password):
    if userlogin(username, old_password):
        perform_query(SqlQueries.CHANGE_PASSWORD.value, args=(new_password, username), commit=True)
        return True
    else:
        return False


def userlogin(username, psswrd):
    rslt = perform_query(SqlQueries.USER_LOGIN.value, args=(username, psswrd), fetch=True)
    if rslt:
        perform_query(SqlQueries.UPDATE_LAST_LOGIN.value, args=(datetime.datetime.now().strftime("%Y-%m-%d"), username),
                      commit=True)
        return True
    else:
        return False


def recover_account(username, email, secret, new_password):
    user_id = perform_query(SqlQueries.CHECK_IS_RECOVERY.value, args=(secret, username, email), fetch=True)

    if user_id:
        perform_query(SqlQueries.CHANGE_PASSWORD.value, args=(new_password, username), commit=True)
        perform_query(SqlQueries.RESET_RECOVERY.value, args=(secret, username, email), commit=True)
        return True

    return False


def store_session(username, session_name, session):
    session = prepare_session_storage(session)

    if any(perform_query(SqlQueries.CHECK_SESSION_EXISTS.value, args=(username, session_name), fetch=True)):
        perform_query(SqlQueries.UPDATE_SESSION.value, args=(session, username, session_name), commit=True)
    else:
        perform_query(SqlQueries.INSERT_SESSION.value, args=(username, session_name, session), commit=True)

    session_pkid = perform_query(SqlQueries.GET_SESSION_PKID.value, args=(username, session_name), fetch=True, top=True)

    return session_pkid[0]


def retrieve_session(session_pkid):
    session = None
    username = None
    session_name = None
    session_data = perform_query(SqlQueries.RETRIEVE_SESSION.value, args=(session_pkid,), fetch=True)

    if session_data:
        perform_query(SqlQueries.UPDATE_LAST_ACCESS.value,
                      args=(datetime.datetime.now().strftime("%Y-%m-%d"), session_pkid), commit=True)
        session_data = session_data[0]
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        perform_query(SqlQueries.UPDATE_SESSION_DATE.value, args=(now, session_pkid), commit=False)
        username = session_data[0]
        session_name = session_data[1]
        session = decompress_data(session_data[2])
        for key in session.keys():
            session[key] = compress_data(session[key])

    return username, session_name, session


def list_sessions(username, list_type):
    if list_type == SessionListType.SHARED:
        all_sessions = perform_query(SqlQueries.GET_SHARED_SESSIONS.value, args=(username,), fetch=True)
    else:
        all_sessions = perform_query(SqlQueries.LIST_SESSIONS.value, args=(username,), fetch=True)

    result = []
    for session in all_sessions:
        result.append(SessionData(owner=session[0], name=session[1], date=session[2], pkid=session[3]))

    return sorted(result, key=attrgetter('date'))


def delete_session(session_pkid):
    username, session_name = perform_query(SqlQueries.CHECK_SESSION_OWNER.value, args=(session_pkid,), fetch=True,
                                           top=True)
    perform_query(SqlQueries.DELETE_SESSION.value, args=(session_pkid,), commit=True)
    return username, session_name


def share_session(session_pkid, share_with_username):
    if not any(perform_query(SqlQueries.CHECK_USER_EXISTS.value, args=(share_with_username,), fetch=True)):
        raise UserDoesntExist
    return perform_query(SqlQueries.SHARE_SESSION.value, args=(share_with_username, session_pkid), commit=True)


def stop_sharing_session(session_pkid, stop_sharing_with):
    return perform_query(SqlQueries.STOP_SHARE.value, args=(stop_sharing_with, session_pkid), commit=True)


def prepare_session_storage(session):
    for key in (b'id', b'user', b'session_pkid'):
        if key in session:
            del session[key]

    key_list = list(session.keys())
    for key in key_list:
        session[key.decode()] = decompress_data(session[key])
        del session[key]

    return compress_data(session)
