FROM postgis/postgis:latest

RUN apt-get update && \
    apt-get install -y osm2pgsql && \
    rm -rf /var/lib/apt/lists/*

# Create directory & copy the .pbf file into the container
RUN mkdir -p /data
COPY warszawa.osm.pbf /data/warszawa.osm.pbf
# COPY spdb_warsaw.sql /docker-entrypoint-initdb.d/

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=gis_db

