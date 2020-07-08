import os
import psycopg2

connection = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')
cursor = connection.cursor()
cursor.execute(open("init.sql", "r").read())
