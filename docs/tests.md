# Testy dostępnych możliwości
W zadaniu należy wskazać dostępne możliwości wyszukiwania: 

## na podstawie relacji topologicznych: 
PostGIS:
| Funkcja             | Relacja                          | Oznacza, że…                                     |
|---------------------|----------------------------------|--------------------------------------------------|
| ST_Within(A, B)     | A wewnątrz B                     | np. punkt wewnątrz gminy                         |
| ST_Contains(A, B)   | A zawiera B                      | np. park zawiera ścieżkę                         |
| ST_Intersects(A, B) | A przecina się z B               | np. droga przecina działkę                       |
| ST_Touches(A, B)    | A styka się z B                  | np. sąsiadujące działki                          |
| ST_Overlaps(A, B)   | A i B się częściowo nakładają    | np. dwie strefy ochronne                         |
| ST_Disjoint(A, B)   | A i B są rozłączne               | np. dwa obszary, które się nie stykają           |
| ST_Equals(A, B)     | A i B są identyczne geometrycznie| np. dwa identyczne zbiory punktów                |
| ST_Crosses(A, B)    | A i B przecinają się             | np. rzeka przecina dizałkę                       |

Python Shapely from GeoPandas:
| Funkcja w Pythonie        | Odpowiednik PostGIS | Co sprawdza?                                                               |
|---------------------------|---------------------|----------------------------------------------------------------------------|
| `geom1.intersects(geom2)` | `ST_Intersects`     | Czy geometrie się przecinają                                               |
| `geom1.within(geom2)`     | `ST_Within`         | Czy `geom1` jest wewnątrz `geom2`                                          |
| `geom1.contains(geom2)`   | `ST_Contains`       | Czy `geom1` zawiera `geom2`                                                |
| `geom1.touches(geom2)`    | `ST_Touches`        | Czy geometrie stykają się                                                  |
| `geom1.overlaps(geom2)`   | `ST_Overlaps`       | Czy geometrie częściowo się nakładają                                     |
| `geom1.equals(geom2)`     | `ST_Equals`         | Czy geometrie są identyczne geometrycznie                                  |
| `geom1.disjoint(geom2)`   | `ST_Disjoint`       | Czy geometrie są rozłączne (nie mają żadnych wspólnych punktów)           |
| `geom1.crosses(geom2)`    | `ST_Crosses`        | Czy geometrie się przecinają, **przecinając granice**, np. linia przez poligon |

## relacji odległościowych: 
PostGIS:
| Funkcja                  | Relacja                       | Oznacza, że…                                         |
|--------------------------|-------------------------------|------------------------------------------------------|
| ST_DWithin(A, B, d)      | A w odległości ≤ d od B       | np. sklep w promieniu 500 m od szkoły                |
| ST_Distance(A, B)        | Odległość między A i B        | np. ile metrów dzieli dwa punkty                     |
| ST_MaxDistance(A, B)     | Największa odległość punktów  | Najdalszy punkt A od najdalszego punktu B            |
| ST_ClosestPoint(A, B)    | Najbliższy punkt na B do A    | Punkt na B najbliższy A                              |
| ST_LongestLine(A, B)     | Najdłuższy odcinek            | Najdłuższy możliwy odcinek łączący A i B             |
| ST_ShortestLine(A, B)    | Najkrótszy odcinek            | Najkrótszy możliwy odcinek łączący A i B             |
| ST_PointInsideCircle(P, x, y, r) | Punkt w kole         | Czy punkt P leży w kole o środku (x, y) i promieniu r|

Python Shapely / GeoPandas:
| Funkcja w Pythonie                        | Odpowiednik PostGIS      | Co sprawdza?                                                        |
|-------------------------------------------|--------------------------|---------------------------------------------------------------------|
| `geom1.dwithin(geom2, d)`*                | ST_DWithin               | Czy geometrie są w odległości ≤ d (GeoPandas 0.14+, Shapely 2+)     |
| `geom1.distance(geom2)`                   | ST_Distance              | Odległość między geometriami                                        |
| `geom1.hausdorff_distance(geom2)`         | ST_MaxDistance           | Największa odległość między punktami dwóch geometrii                |
| `shapely.ops.nearest_points(a, b)`        | ST_ClosestPoint          | Najbliższe punkty na dwóch geometriach                              |
| `point.within(Point(x, y).buffer(r))`     | ST_PointInsideCircle     | **walkaround** Czy punkt leży w kole o środku (x, y) i promieniu r                 |

## możliwości złączeń zbiorów danych przestrzennych:
Najczęściej wykonywane złączenie przestrzenne w **PostGIS** wykorzystują funkcję:
- ST_Intersects,
- ST_Contains,
- ST_DWithin

Eksperymenty dla zapytań typu:
- `JOIN ON ST_Intersects(a.geom, b.geom)`
- `LEFT JOIN ... WHERE ST_DWithin(...)`

Aktualnie PostGIS w wersji **3.5** wspiera następujące typy złączeń:

| JOIN SQL            | Opis                                                          | Typowe użycie z funkcją PostGIS              |
| ------------------- | ------------------------------------------------------------- | -------------------------------------------- |
| **INNER JOIN**      | Zwraca rekordy, które mają dopasowanie w obu tabelach         | `ON ST_Intersects(a.geom, b.geom)`           |
| **LEFT JOIN**       | Zwraca wszystkie rekordy z lewej tabeli + dopasowane z prawej | np. znajdź obiekty bez przecięcia            |
| **RIGHT JOIN**      | Wszystkie z prawej + dopasowane z lewej                       | rzadziej stosowane                           |
| **FULL OUTER JOIN** | Wszystkie z obu tabel, dopasowane lub nie                     | rzadko w analizie przestrzennej              |
| **CROSS JOIN**      | Iloczyn kartezjański – każda kombinacja                       | nieefektywne bez ograniczenia przestrzennego |
| **LATERAL JOIN**    | Złączenie z podzapytaniem zależnym od wiersza                 | np. znajdź **najbliższy punkt**              |


[ref](https://postgis.net/workshops/postgis-intro/joins.html)
---

W celu porównania molzliwosci, zapytania PostGIS zostały odwzorowane dla GeoPandas za pomocą funkcji **sjoin**:
```
gpd.sjoin(gdf1, gdf2, how="inner", predicate="intersects")
```

Aktualnie wspierane sposoby złączeń przestrzennych dla Geopandas to:
- Left Outer Join
- Right Outer Join
- Inner Join

[ref](https://geopandas.org/en/stable/gallery/spatial_joins.html)

## funkcji agregujących:

### PostGIS

PostGIS oferuje szeroki zakres funkcji agregujących, które pozwalają na podsumowanie, łączenie i analizę zbiorów geometrii:

| Funkcja PostGIS           | Opis                                                        | Przykład użycia/testu                                      |
|---------------------------|-------------------------------------------------------------|------------------------------------------------------------|
| `ST_Union(geom)`          | Łączy wiele geometrii w jedną (multi/polygon)               | Zbiorcza granica wszystkich parków w mieście               |
| `ST_Collect(geom)`        | Tworzy kolekcję geometrii                                   | Zbiór punktów stacji metra jako MultiPoint                 |
| `ST_Extent(geom)`         | Zwraca prostokąt ograniczający (bounding box)               | Bounding box wszystkich budynków                           |
| `ST_MakeLine(geom)`       | Tworzy linię z punktów                                      | Trasa przez kolejne przystanki                             |
| `ST_MakePolygon(geom)`    | Tworzy poligon z linii                                      | Obwiednia z linii granicznych                              |
| `ST_Centroid(geom)`       | Centroid zbioru geometrii                                   | Środek ciężkości wszystkich parków                         |
| `ST_Envelope(geom)`       | Prostokąt ograniczający dla każdej geometrii                | Bounding box dla każdego budynku                           |

**Testowanie dla PostGIS:**  
Każda z tych funkcji może być przetestowana przez wykonanie odpowiedniego zapytania SQL, np.:
```sql
SELECT ST_Union(way) FROM planet_osm_polygon WHERE leisure = 'park';
SELECT COUNT(*) FROM planet_osm_point WHERE railway = 'station';
SELECT AVG(ST_Area(way)) FROM planet_osm_polygon WHERE building IS NOT NULL;
```
Wyniki będą porównywane z analogicznymi operacjami w GeoPandas.

---

### GeoPandas

GeoPandas również umożliwia agregacje przestrzenne, choć zakres funkcji jest nieco bardziej ograniczony niż w PostGIS:

| Funkcja GeoPandas / Shapely         | Odpowiednik PostGIS | Opis/testowanie                                      |
|-------------------------------------|---------------------|------------------------------------------------------|
| `gdf.unary_union`                   | ST_Union            | Łączy wszystkie geometrie w jedną                    |
| `gpd.tools.collect(geom)`           | ST_Collect          | Tworzy kolekcję geometrii                            |
| `gdf.total_bounds`                  | ST_Extent           | Bounding box całego zbioru (minx, miny, maxx, maxy)  |
| `shapely.ops.linemerge`             | ST_MakeLine         | Łączy linie w jedną linię                            |
| `gdf.centroid`                      | ST_Centroid         | Centroid każdej geometrii                            |
| `gdf.envelope`                      | ST_Envelope         | Bounding box dla każdej geometrii                    |

**Testowanie w GeoPandas:**  
Każda funkcja zostanie przetestowana na analogicznym zbiorze danych jak w PostGIS, np.:
```python
parks_union = gp_polygons[gp_polygons['leisure'] == 'park'].unary_union
stations_count = gp_points[gp_points['railway'] == 'station'].shape[0]
avg_building_area = gp_polygons[gp_polygons['building'].notnull()].area.mean()
```
Wyniki będą porównywane z wynikami zapytań SQL z PostGIS.

---

### Jak będą testowane możliwości?

1. **Przygotowanie tych samych zbiorów danych** w PostGIS i GeoPandas (np. wszystkie parki, budynki, stacje metra).
2. **Wykonanie tych samych operacji agregujących** (np. union, count, avg, extent) w obu środowiskach.
3. **Porównanie wyników** – czy są zgodne, czy występują różnice (np. w dokładności, typie geometrii).
4. **Pomiar czasu wykonania** – dla większych zbiorów porównanie wydajności.
5. **Opis ograniczeń** – np. brak ST_Extent w GeoPandas (zastępowane przez total_bounds), brak ST_MakePolygon, itp.

Do testów wybrano tylko te funkcje agregujące, które można wykonać zarówno w PostGIS, jak i w GeoPandas/Shapely na typowych danych wektorowych. Funkcje typowo rasterowe, 3D, klastrowania czy eksportu do formatów specjalnych nie będą testowane, bo nie mają odpowiedników w GeoPandas lub nie są typowe dla analiz 2D. Niemniej we wnioskach zostaną opisane wszystkie funkcje dostępne w PostGIS oraz wskazane względem nich braki w bibliotece GeoPandas.


## Eksperymenty z ograniczoną pamięcią operacyjną

1. Ograniczenie pamięci operacyjnej dla kontenera Docker z PostGIS

```bash
docker run --name postgis-test --rm -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 --memory=1g postgis/postgis
```
Testowane operacje:
- ST_Union na dużym zbiorze poligonów (np. wszystkie budynki)
- ST_Intersects na dużym zbiorze punktów i poligonów (np. wszystkie budynki i parki)
- ST_DWithin 

Obserwacje:
- Czy zapytania kończą się sukcesem?
- Czy pojawiają się błędy OOM (Out Of Memory)?
- Czas wykonania zapytań

2. Ograniczenie pamięci operacyjnej dla kontenera Python/GeoPandas

```bash
```

