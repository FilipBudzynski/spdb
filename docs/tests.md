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
| ST_DFullyWithin(A, B, d) | Obie geometrie w odległości d | np. dwa obiekty całkowicie w promieniu d             |
| ST_MaxDistance(A, B)     | Największa odległość punktów  | Najdalszy punkt A od najdalszego punktu B            |
| ST_ClosestPoint(A, B)    | Najbliższy punkt na B do A    | Punkt na B najbliższy A                              |
| ST_LongestLine(A, B)     | Najdłuższy odcinek            | Najdłuższy możliwy odcinek łączący A i B             |
| ST_ShortestLine(A, B)    | Najkrótszy odcinek            | Najkrótszy możliwy odcinek łączący A i B             |
| ST_PointInsideCircle(P, x, y, r) | Punkt w kole         | Czy punkt P leży w kole o środku (x, y) i promieniu r|

Python Shapely / GeoPandas:
| Funkcja w Pythonie                        | Odpowiednik PostGIS      | Co sprawdza?                                                        |
|-------------------------------------------|--------------------------|---------------------------------------------------------------------|
| `geom1.distance(geom2)`                   | ST_Distance              | Odległość między geometriami                                        |
| `geom1.dwithin(geom2, d)`*                | ST_DWithin               | Czy geometrie są w odległości ≤ d (GeoPandas 0.14+, Shapely 2+)     |
| `geom1.relate_pattern(geom2, pattern)`    | ST_DFullyWithin          | Można sprawdzić relację przez wzorzec DE-9IM                         |
| `geom1.hausdorff_distance(geom2)`         | ST_MaxDistance           | Największa odległość między punktami dwóch geometrii                |
| `shapely.ops.nearest_points(a, b)`        | ST_ClosestPoint          | Najbliższe punkty na dwóch geometriach                              |
| `shapely.ops.substring(line, start, end)` | -                        | Fragment linii (odległość względna, podobnie jak ST_LineSubstring)   |
| `point.within(Point(x, y).buffer(r))`     | ST_PointInsideCircle     | Czy punkt leży w kole o środku (x, y) i promieniu r                 |

## możliwości złączeń zbiorów danych przestrzennych:
-- TODO

## funkcji agregujących:
-- TODO
