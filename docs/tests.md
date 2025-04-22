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
-- TODO

## możliwości złączeń zbiorów danych przestrzennych:
-- TODO

## funkcji agregujących:
-- TODO
