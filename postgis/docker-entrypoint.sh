#!/bin/bash
set -e

if ! psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "SELECT 1 FROM planet_osm_point LIMIT 1;" 2>/dev/null; then
  echo "Database is empty, loading data..."

  # Run osm2pgsql to load the data into PostGIS
  osm2pgsql -d "$POSTGRES_DB" -U "$POSTGRES_USER" -H localhost -P 5432 --create --slim --hstore --style /usr/share/osm2pgsql/default.style /data/warszawa.osm.pbf
  
  echo "Data loaded into PostGIS."
else
  echo "Database already populated. Skipping data load."
fi

exec docker-entrypoint.sh "$@"
