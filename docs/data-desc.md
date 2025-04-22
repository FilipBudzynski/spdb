# Opis danych
W projekcie wykorzystano dane przestrzenne pochodzące z **OpenStreetMap**, pozyskane z: http://download.geofabrik.de/europe/poland/mazowieckie-latest.osm.pbf .

Dane pobrane zostały dla obszaru Warszawy wskazanym w [dane](./data.md).

## Tabele w bazie danych
Po imporcie danych do bazy PostGIS uzyskano m.in. tabele:
* `planet_osm_point` -- opisującą POI np. pomniki, przystanki, szkoły, sklepy etc.
* `planet_osm_polygon` -- obiekty o zamkniętej geometrii, np. parki, budynki.
* `planet_osm_line` -- linie czyli np. ulice, tory kolejowe, rzeki
* planet_osm_roads` -- główne drogi

## Atrybuty:
Dane zawierają wiele kolumn opisowych, z których najczęściej używane to:
* name – nazwa obiektu
* amenity, shop, tourism, leisure – typ obiektu (np. sklep, atrakcja turystyczna, park)
* way – geometria obiektu w formacie PostGIS (punkt, linia, poligon)
* tags – dodatkowe informacje zakodowane w formacie hstore

## Układ współrzędnych
Dane są zapisane w układzie **EPSG:3857**.
