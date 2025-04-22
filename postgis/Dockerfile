FROM postgis/postgis:latest

RUN apt-get update && \
    apt-get install -y osm2pgsql && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /data
COPY /data/warszawa.osm.pbf /data/warszawa.osm.pbf
COPY docker-entrypoint.sh /docker-entrypoint-initdb.d/init.sh

# COPY spdb_warsaw.sql /docker-entrypoint-initdb.d/

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=gis_db

RUN chmod +x /docker-entrypoint-initdb.d/init.sh


