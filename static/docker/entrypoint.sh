#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

PGPASSWORD="$POSTGRES_PASSWORD" psql -U $USERNAME -d $DATABASE -h localhost -a -f postgresql/init.sql

exec "$@"