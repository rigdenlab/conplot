import os
from enum import Enum
import datetime
import psycopg2
from loaders import DatasetReference
from utils.exceptions import SQLInjectionAlert, UserExists, EmailAlreadyUsed, IntegrityError, UserDoesntExist


class TableNames(Enum):
    USER_DATA = 'user_data'
    SESSION_DATA = 'session_data'


class SqlFieldNames(Enum):
    ID = 'id'
    OWNER = 'owner_username'
    SESSION_NAME = 'session_name'
    USERNAME = 'username'
    EMAIL = 'email'
    PASSWORD = 'password'
    LAST_ACCESS = 'last_access_date'
    CREATED_DATE = 'created_date'
    LAST_LOGIN = 'last_login'
    SHARED = 'shared_with'


class SqlQueries(Enum):
    CREATE_USER = """INSERT INTO {} ({},{},{}) VALUES (%s, %s,crypt(%s, gen_salt('bf')))""".format(
        TableNames.USER_DATA.value, SqlFieldNames.USERNAME.value, SqlFieldNames.EMAIL.value,
        SqlFieldNames.PASSWORD.value)

    USER_LOGIN = """SELECT {} FROM {} WHERE {} = %s AND {} = crypt(%s, {})
    """.format(SqlFieldNames.ID.value, TableNames.USER_DATA.value, SqlFieldNames.USERNAME.value,
               SqlFieldNames.PASSWORD.value, SqlFieldNames.PASSWORD.value)

    UPDATE_LAST_LOGIN = """UPDATE {} SET {} = %s WHERE {} = %s
    """.format(TableNames.USER_DATA.value, SqlFieldNames.LAST_LOGIN.value, SqlFieldNames.USERNAME.value)

    CHECK_SESSION_EXISTS = """SELECT * FROM {} WHERE {} = %s AND {} = %s
    """.format(TableNames.SESSION_DATA.value, SqlFieldNames.OWNER.value, SqlFieldNames.SESSION_NAME.value)

    CHECK_USER_EXISTS = """SELECT * FROM {} WHERE {} = %s
        """.format(TableNames.USER_DATA.value, SqlFieldNames.USERNAME.value)

    CHECK_EMAIL_USED = """SELECT * FROM {} WHERE {} = %s
            """.format(TableNames.USER_DATA.value, SqlFieldNames.EMAIL.value)

    CHANGE_PASSWORD = """UPDATE {} SET {} = crypt(%s, {}) WHERE {} = %s
    """.format(TableNames.USER_DATA.value, SqlFieldNames.PASSWORD.value, SqlFieldNames.PASSWORD.value,
               SqlFieldNames.USERNAME.value)

    UPDATE_SESSION = """UPDATE {} SET {} WHERE {} = %s AND {} = %s
    """.format(TableNames.SESSION_DATA.value,
               ",".join(["{} = %s".format(dataset.value) for dataset in DatasetReference]), SqlFieldNames.OWNER.value,
               SqlFieldNames.SESSION_NAME.value)

    INSERT_SESSION = """INSERT INTO %s (%s) VALUES ({})
    """ % (TableNames.SESSION_DATA.value,
           ",".join([SqlFieldNames.OWNER.value, SqlFieldNames.SESSION_NAME.value] +
                    [dataset.value for dataset in DatasetReference]))

    RETRIEVE_SESSION = """SELECT * FROM {} WHERE {} = %s AND {} = %s
    """.format(TableNames.SESSION_DATA.value, SqlFieldNames.OWNER.value, SqlFieldNames.SESSION_NAME.value)

    UPDATE_SESSION_DATE = """UPDATE {} SET {} = %s WHERE {} = %s AND {} = %s
    """.format(TableNames.SESSION_DATA.value, SqlFieldNames.LAST_ACCESS.value, SqlFieldNames.OWNER.value,
               SqlFieldNames.SESSION_NAME.value)

    LIST_SESSIONS = """SELECT {}, {} FROM {} WHERE {} = %s
    """.format(SqlFieldNames.SESSION_NAME.value, SqlFieldNames.CREATED_DATE.value, TableNames.SESSION_DATA.value,
               SqlFieldNames.OWNER.value)

    DELETE_SESSION = """DELETE FROM {} WHERE {} = %s AND {} = %s
    """.format(TableNames.SESSION_DATA.value, SqlFieldNames.OWNER.value, SqlFieldNames.SESSION_NAME.value)

    SHARE_SESSION = """UPDATE {} SET {} = array_append({}, %s) WHERE {} = %s AND {} = %s
    """.format(TableNames.SESSION_DATA.value, SqlFieldNames.SHARED.value, SqlFieldNames.SHARED.value,
               SqlFieldNames.OWNER.value, SqlFieldNames.SESSION_NAME.value)

    STOP_SHARE = """UPDATE {} SET {} = array_remove({}, %s) WHERE {} = %s AND {} = %s
    """.format(TableNames.SESSION_DATA.value, SqlFieldNames.SHARED.value, SqlFieldNames.SHARED.value,
               SqlFieldNames.OWNER.value, SqlFieldNames.SESSION_NAME.value)

    GET_SHARED_SESSIONS = """SELECT * FROM {} WHERE %s = ANY({})
    """.format(TableNames.SESSION_DATA.value, SqlFieldNames.SHARED.value)


def initiate_connection():
    connection = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')
    cursor = connection.cursor()
    return connection, cursor


def perform_query(query, args, fetch=False, commit=False):
    if ';' in query or ';' in args:
        raise SQLInjectionAlert('SQL injection detected with query %s and values %s' % (query, args))

    result = None
    connection, cursor = initiate_connection()
    cursor.execute(query, args)

    if fetch:
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


def store_session(username, session_name, session):
    values = [username, session_name]
    fields = ['owner_username', 'session_name']

    for dataset in DatasetReference:
        if dataset.value.encode() in session.keys():
            values.append(psycopg2.Binary(session[dataset.value.encode()]))
            fields.append(dataset.value)
        else:
            values.append(None)
            fields.append(dataset.value)

    if any(perform_query(SqlQueries.CHECK_SESSION_EXISTS.value, args=(username, session_name), fetch=True)):
        values = values[2:] + [username, session_name]
        perform_query(SqlQueries.UPDATE_SESSION.value, args=values, commit=True)
    else:
        value_placeholders = ",".join(['%s' for x in range(0, len(values))])
        query = SqlQueries.INSERT_SESSION.value.format(value_placeholders)
        perform_query(query, args=values, commit=True)


def retrieve_session(username, session_name):
    session = None
    session_data = perform_query(SqlQueries.RETRIEVE_SESSION.value, args=(username, session_name), fetch=True)

    if session_data:
        session_data = session_data[0]
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        perform_query(SqlQueries.UPDATE_SESSION_DATE.value, args=(now, username, session_name), fetch=False)
        session = {}
        for idx, dataset in enumerate(DatasetReference, 2):
            if session_data[idx] is not None:
                session[dataset.value] = session_data[idx]

    return session


def list_all_sessions(username):
    return perform_query(SqlQueries.LIST_SESSIONS.value, args=(username,), fetch=True)


def delete_session(username, session_name):
    return perform_query(SqlQueries.DELETE_SESSION.value, args=(username, session_name), commit=True)


def share_session(owner, session_name, share_with_username):
    if not any(perform_query(SqlQueries.CHECK_USER_EXISTS.value, args=(share_with_username,), fetch=True)):
        raise UserDoesntExist
    return perform_query(SqlQueries.SHARE_SESSION.value, args=(share_with_username, owner, session_name), commit=True)


def stop_sharing_session(owner, session_name, stop_sharing_with):
    return perform_query(SqlQueries.STOP_SHARE.value, args=(stop_sharing_with, owner, session_name), commit=True)


def check_shared_sessions(username):
    return perform_query(SqlQueries.GET_SHARED_SESSIONS.value, args=(username,), fetch=True)
