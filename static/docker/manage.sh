if [ "$1" = "build" ]; then
  docker-compose up -d
  docker-compose exec web psql -U $POSTGRES_USER -d $POSTGRES_DB -h postgres_db -a -f postgresql/init.sql
elif [ "$1" = "stop" ]; then
  docker-compose down -v
elif [ "$1" = "start" ]; then
  docker-compose -f docker-compose.yml up -d --build
  docker-compose -f docker-compose.yml logs -f
fi


