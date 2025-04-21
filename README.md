# SPDB
spatial databases - comparison of spatial data query capabilities

## Środowisko testowe: 
Testy zostały przeprowadzone w środowisku Docker, które umożliwia uruchomienie kontenerów z bazą danych PostgreSQL rozszerzoną o PostGIS oraz kontenera z Pythonem. Systemy te umożliwiają przechowywanie i manipulację danymi przestrzennymi. W projekcie zastosowano następujące technologie:

Docker – do uruchomienia środowisk bazy danych i aplikacji.

PostGIS – rozszerzenie dla **PostgreSQL** umożliwiające przechowywanie, analizowanie i zapytania przestrzenne.

Python – w którym przeprowadzono analizę danych przestrzennych, wykorzystując bibliotekę **GeoPandas** do manipulacji danymi przestrzennymi oraz **psycopg2**do interakcji z bazą danych.

Wersje używanych narzędzi:
- PostgreSQL: 16.4
- PostGIS: 3.4
- Python: 3.11
- GeoPandas: 0.10.0

## Wykorzystane dane
```
http://download.geofabrik.de/europe/poland/mazowieckie-latest.osm.pbf
```

Z geofabrik pobrano dane z województwa mazowieckiego. Następnie dane te okrojono za pomoca **osmosis** w celu zmieniejszenia zajmowanego miejsca. 
Wyborano obszar obszar Warszawy, dokładniej:
```bash
osmosis --read-pbf mazowieckie-latest.osm.pbf \
        --bounding-box top=52.4 left=20.9 bottom=52.2 right=21.2 \
        --write-pbf warszawa.osm.pbf
```

## Sposób załadowania danych do postGIS
Do załadowania danych do postgreSQL z postGIS wykorzystano **osm2pgsql**. Pobrane dane załadowano przy użyciu komendy:
```bash
osm2pgsql -d gis_db --create --slim -G --hstore -C 2048 --number-processes 4 -U user mazowieckie-latest.osm.pbf
```

Aby dane zostały poprawnie zaimportowane dodano rozszerzenie **hstore** poprzez: 
```sql
CREATE EXTENSION hstore;
```
