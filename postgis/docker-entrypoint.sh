#!/bin/bash
set -e

psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "CREATE EXTENSION IF NOT EXISTS hstore;"

if ! psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "SELECT 1 FROM planet_osm_point LIMIT 1;" 2>/dev/null; then
  echo "Baza danych jest pusta, ładowanie danych..."

  osm2pgsql -d "$POSTGRES_DB" -U "$POSTGRES_USER" --create --slim --hstore --style /usr/share/osm2pgsql/default.style /data/warszawa.osm.pbf
  
  echo "Dane załadowane do PostGIS."
else
  echo "Baza danych już zawiera dane. Pomijam ładowanie."
fi

exec docker-entrypoint.sh "$@"
