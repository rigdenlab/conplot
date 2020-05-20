import os
from enum import Enum
import datetime
import psycopg2
from loaders import DatasetReference


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


class SqlQueries(Enum):
    UPDATE = """UPDATE {} SET {} = '{}' WHERE {} = '{}'"""
    DELETE = """DELETE FROM {} WHERE {} = '{}'"""
    CREATE_USER = """INSERT INTO {} ({},{},{}) VALUES ('{}','{}',crypt('{}', gen_salt('bf')))"""
    USER_LOGIN = """SELECT {} FROM {} WHERE {} = '{}' AND {} = crypt('{}', {})"""
    UPDATE_LAST_LOGIN = """UPDATE {} SET {} = '{}' WHERE {} = '{}'"""
    CHECK_SESSION_EXISTS = """SELECT * FROM {} WHERE {} = '{}' AND {} = '{}'"""
    UPDATE_SESSION = """UPDATE {} SET {} WHERE {} = '{}' AND {} = '{}' """
    INSERT_SESSION = """INSERT INTO {} ({}) VALUES ({})"""
    RETRIEVE_SESSION = """SELECT * FROM {} WHERE {} = '{}' AND {} = '{}'"""
    UPDATE_SESSION_DATE = """UPDATE {} SET {} = '{}' WHERE {} = '{}' AND {} = '{}'"""
    LIST_SESSIONS = """SELECT {}, {} FROM {} WHERE {} = '%s'"""
    DELETE_SESSION = """DELETE FROM {} WHERE {} = '{}' AND {} = '{}'"""


def initiate_connection():
    connection = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')
    cursor = connection.cursor()
    return connection, cursor


def perform_query(query, fetch=False, commit=False):
    result = None
    connection, cursor = initiate_connection()
    cursor.execute(query)

    if fetch:
        result = cursor.fetchall()

    if commit:
        connection.commit()

    cursor.close()
    connection.close()

    return result


def update_entry(table_name, field_update, value_update, id_field, id_value):
    query = SqlQueries.UPDATE.value.format(table_name, field_update, value_update, id_field, id_value)
    perform_query(query, commit=True)


def delete_entry(table_name, id_field, id_value):
    query = SqlQueries.DELETE.value.format(table_name, id_field, id_value)
    perform_query(query, commit=True)


def create_user(username, psswrd, email):
    try:
        query = SqlQueries.CREATE_USER.value.format(TableNames.USER_DATA.value, SqlFieldNames.USERNAME.value,
                                                    SqlFieldNames.EMAIL.value, SqlFieldNames.PASSWORD.value, username,
                                                    email, psswrd)
        perform_query(query, commit=True)
        return True
    except psycopg2.IntegrityError:
        return False


def userlogin(username, psswrd):
    query = SqlQueries.USER_LOGIN.value.format(SqlFieldNames.ID.value, TableNames.USER_DATA.value,
                                               SqlFieldNames.USERNAME.value, username, SqlFieldNames.PASSWORD.value,
                                               psswrd, SqlFieldNames.PASSWORD.value)

    rslt = perform_query(query, fetch=True)
    if rslt:
        query = SqlQueries.UPDATE_LAST_LOGIN.value.format(TableNames.USER_DATA.value, SqlFieldNames.LAST_LOGIN.value,
                                                          datetime.datetime.now().strftime("%Y-%m-%d"),
                                                          SqlFieldNames.USERNAME.value, username)
        perform_query(query, commit=True)
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

    query = SqlQueries.CHECK_SESSION_EXISTS.value.format(TableNames.SESSION_DATA.value, SqlFieldNames.OWNER.value,
                                                         username, SqlFieldNames.SESSION_NAME.value, session_name)

    if any(perform_query(query, fetch=True)):
        values = values[2:]
        updates = ",".join(["{} = %s".format(field) for field in fields[2:]])
        query = SqlQueries.UPDATE_SESSION.value.format(TableNames.SESSION_DATA.value, updates,
                                                       SqlFieldNames.OWNER.value, username,
                                                       SqlFieldNames.SESSION_NAME.value, session_name)
    else:
        query = SqlQueries.INSERT_SESSION.value.format(TableNames.SESSION_DATA.value, ",".join(fields),
                                                       ",".join(['%s' for x in range(0, len(values))]))

    connection, cursor = initiate_connection()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()


def retrieve_session(username, session_name):
    session = None

    query = SqlQueries.RETRIEVE_SESSION.value.format(TableNames.SESSION_DATA.value, SqlFieldNames.OWNER.value, username,
                                                     SqlFieldNames.SESSION_NAME.value, session_name)
    session_data = perform_query(query, fetch=True)
    if session_data:
        session_data = session_data[0]
        query = SqlQueries.UPDATE_SESSION_DATE.value.format(TableNames.SESSION_DATA.value,
                                                            SqlFieldNames.LAST_ACCESS.value,
                                                            datetime.datetime.now().strftime("%Y-%m-%d"),
                                                            SqlFieldNames.OWNER.value, username,
                                                            SqlFieldNames.SESSION_NAME.value, session_name)
        perform_query(query, fetch=False)
        session = {}
        for idx, dataset in enumerate(DatasetReference, 2):
            if session_data[idx] is not None:
                session[dataset.value] = session_data[idx]

    return session


def list_all_sessions(username):
    query = SqlQueries.LIST_SESSIONS.value.format(SqlFieldNames.SESSION_NAME.value, SqlFieldNames.CREATED_DATE.value,
                                                  SqlFieldNames.TableNames.SESSION_DATA.value,
                                                  SqlFieldNames.OWNER.value, username)
    return perform_query(query, fetch=True)


def delete_session(username, session_name):
    query = SqlQueries.DELETE_SESSION.valueformat(TableNames.SESSION_DATA.value, SqlFieldNames.OWNER.value, username,
                                                  SqlFieldNames.SESSION_NAME.value, session_name)
    return perform_query(query, commit=True)
