import os
from enum import Enum
import datetime
import psycopg2
from loaders import DatasetReference


class TableNames(Enum):
    USER_DATA = 'user_data'
    SESSION_DATA = 'session_data'


class SqlQueries(Enum):
    INSERT = """ INSERT INTO %s (%s) VALUES (%s)"""
    INSERT_SESSION = """INSERT INTO {} ({}) VALUES ({})"""
    UPDATE = """UPDATE %s SET %s = '%s' WHERE %s = '%s'"""
    DELETE = """DELETE FROM %s WHERE %s = '%s'"""
    CRYPT = """crypt('%s', gen_salt('bf'))"""
    LOGIN = """SELECT id FROM {} WHERE username = '%s' AND password = crypt('%s', password)
    """.format(TableNames.USER_DATA.value)
    RETRIEVE_SESSION = """SELECT * FROM {} WHERE owner_username = '%s' AND session_name = '%s'
    """.format(TableNames.SESSION_DATA.value)
    UPDATE_SESSION_DATE = """UPDATE {} SET {} = '%s' WHERE {} = '%s' AND {} = '%s'
    """.format(TableNames.SESSION_DATA.value, 'last_access_date', 'owner_username', 'session_name')


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


def insert_entry(table_name, fields, values):
    query = SqlQueries.INSERT.value % (table_name, ",".join(fields), ",".join(values))
    perform_query(query, commit=True)


def update_entry(table_name, field_update, value_update, id_field, id_value):
    query = SqlQueries.UPDATE.value % (table_name, field_update, value_update, id_field, id_value)
    perform_query(query, commit=True)


def delete_entry(table_name, id_field, id_value):
    query = SqlQueries.DELETE.value % (table_name, id_field, id_value)
    perform_query(query, commit=True)


def create_user(username, psswrd, email=None):
    insert_entry(TableNames.USER_DATA.value, ('username', 'email', 'password'),
                 ("'%s'" % username, "'%s'" % email, SqlQueries.CRYPT.value % psswrd))


def userlogin(username, psswrd):
    query = SqlQueries.LOGIN.value % (username, psswrd)

    rslt = perform_query(query, fetch=True)
    if rslt:
        update_entry(TableNames.USER_DATA.value, 'last_login',
                     datetime.datetime.now().strftime("%Y-%m-%d"), 'username', username)
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

    query = SqlQueries.INSERT_SESSION.value.format(TableNames.SESSION_DATA.value, ",".join(fields),
                                                   ",".join(['%s' for x in range(0, len(values))]))

    connection, cursor = initiate_connection()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()


def retrieve_session(username, session_name):
    session = None
    query = SqlQueries.RETRIEVE_SESSION.value % (username, session_name)
    session_data = perform_query(query, fetch=True)
    if session_data:
        session_data = session_data[0]
        query = SqlQueries.UPDATE_SESSION_DATE.value % (datetime.datetime.now().strftime("%Y-%m-%d"),
                                                        username, session_name)
        perform_query(query, fetch=False)
        session = {}
        for idx, dataset in enumerate(DatasetReference, 2):
            session[dataset.value] = session_data[idx]

    return session
