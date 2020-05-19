import os
import psycopg2


def initiate_connection():
    connection = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')
    cursor = connection.cursor()
    return connection, cursor


def perform_query(query, all_results=True, commit=False):
    connection, cursor = initiate_connection()
    cursor.execute(query)

    if all_results:
        result = cursor.fetchall()
    else:
        result = cursor.fetchone()

    if commit:
        connection.commit()

    cursor.close()
    connection.close()

    return result


def insert_entry(table_name, fields, values):
    query = """ INSERT INTO %s (%s) VALUES (%s)""" % (table_name, ",".join(fields), ",".join(values))
    perform_query(query, commit=True)


def update_entry(table_name, field, value, id):
    query = """UPDATE %s SET %s = %s WHERE id = %s""" % (table_name, field, value, id)
    perform_query(query, commit=True)


def delete_entry(table_name, id):
    query = """DELETE FROM %s WHERE id = '%s'""" % (table_name, id)
    perform_query(query, commit=True)


def userlogin(username, psswrd, table_name='user_data'):
    query = """SELECT id from %s where username = '%s' AND password = crypt('%s', password)""" % (table_name, username,
                                                                                               psswrd)
    rslt = perform_query(query, all_results=False)

    if rslt:
        return True
    else:
        return False


def create_user(username, email, psswrd, table_name='user_data', fields=('username', 'email', 'password')):

    query = """INSERT INTO %s (%s) VALUES ('%s', '%s', crypt('%s', gen_salt('bf')))""" % (table_name, ",".join(fields),
                                                                                    username, email, psswrd)
    perform_query(query, commit=True)
