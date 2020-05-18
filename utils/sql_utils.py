import os
from enum import Enum
import datetime
import psycopg2


class SqlQueries(Enum):
    INSERT = """ INSERT INTO %s (%s) VALUES (%s)"""
    UPDATE = """UPDATE %s SET %s = '%s' WHERE %s = '%s'"""
    DELETE = """DELETE FROM %s WHERE %s = '%s'"""
    LOGIN = """SELECT id FROM user_data WHERE username = '%s' AND password = crypt('%s', password)"""
    CRYPT = """crypt('%s', gen_salt('bf'))"""


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


def userlogin(username, psswrd):
    query = SqlQueries.LOGIN.value % (username, psswrd)

    rslt = perform_query(query, fetch=True)
    if rslt:
        update_entry('user_data', 'last_login', datetime.datetime.now().strftime("%Y-%m-%d"), 'username', username)
        return True
    else:
        return False


def create_user(username, email, psswrd):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    insert_entry('user_data', ('username', 'email', 'password', 'created_date', 'last_login'),
                 ("'%s'" % username, "'%s'" % email, SqlQueries.CRYPT.value % psswrd, "'%s'" % now, "'%s'" % now))
