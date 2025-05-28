import time
import geopandas as gpd
from sqlalchemy import create_engine
import csv
import sys

# Parametry wejściowe: limit pamięci jako string (opcjonalnie)
mem_limit = sys.argv[1] if len(sys.argv) > 1 else "unknown"

engine = create_engine("postgresql://postgres:postgres@postgis:5432/gis_db")

query = """
SELECT dz.osm_id AS district_id, dz.name AS district_name, ST_Union(bd.way) AS buildings_union
FROM planet_osm_polygon dz
JOIN planet_osm_polygon bd
  ON ST_Within(bd.way, dz.way)
WHERE dz.boundary = 'administrative'
  AND dz.admin_level = '10'
  AND bd.building IS NOT NULL
GROUP BY dz.osm_id, dz.name
"""

result_row = {
    "mem_limit": mem_limit,
    "exec_time": None,
    "districts": None,
    "error": None,
}

try:
    start_time = time.time()
    result = gpd.read_postgis(query, engine, geom_col="buildings_union")
    exec_time = time.time() - start_time
    result_row["exec_time"] = exec_time
    result_row["districts"] = len(result)
    print(
        f"Limit pamięci: {mem_limit} | Czas wykonania: {exec_time:.2f} s | Liczba dzielnic: {len(result)}"
    )
except Exception as e:
    result_row["error"] = str(e)
    print(f"Limit pamięci: {mem_limit} | Błąd: {e}")

# Zapisz wynik do pliku CSV (dopisz wiersz)
with open("stress_test_results.csv", "a", newline="") as f:
    writer = csv.DictWriter(
        f, fieldnames=["mem_limit", "exec_time", "districts", "error"]
    )
    if f.tell() == 0:
        writer.writeheader()
    writer.writerow(result_row)
