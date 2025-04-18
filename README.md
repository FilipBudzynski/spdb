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

