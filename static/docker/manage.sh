if [ "$1" = "build" ]; then
  docker-compose up -d
  docker-compose exec web psql -U $POSTGRES_USER -d $POSTGRES_DB -h localhost -a -f postgresql/init.sql
  docker-compose exec web redis-cli CONFIG SET maxmemory 256mb ; docker-compose exec web redis-cli CONFIG SET maxmemory-policy volatile-ttl
elif [ "$1" = "stop" ]; then
  docker-compose down -v
elif [ "$1" = "start" ]; then
  docker-compose -f docker-compose.yml up -d --build
  docker-compose -f docker-compose.yml logs -f
fi


