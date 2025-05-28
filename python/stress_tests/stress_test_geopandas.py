import time
import geopandas as gpd
import pandas as pd
import sys
import csv
from sqlalchemy import create_engine

mem_limit = sys.argv[1] if len(sys.argv) > 1 else "unknown"

engine = create_engine("postgresql://postgres:postgres@postgis:5432/gis_db")

result_row = {
    "mem_limit": mem_limit,
    "exec_time": None,
    "districts": None,
    "error": None,
}

try:
    start_time = time.time()
    gp_polygons = gpd.read_postgis(
        "SELECT * FROM planet_osm_polygon;", engine, geom_col="way"
    )
    districts = gp_polygons[
        (gp_polygons["boundary"] == "administrative")
        & (gp_polygons["admin_level"] == "10")
    ]
    buildings = gp_polygons[gp_polygons["building"].notnull()]

    joined = gpd.sjoin(buildings, districts, predicate="within", how="inner")
    grouped = (
        joined.groupby("osm_id_right")
        .agg({"way": lambda x: x.unary_union, "name_right": "first"})
        .reset_index()
    )
    exec_time = time.time() - start_time
    result_row["exec_time"] = exec_time
    result_row["districts"] = len(grouped)
    print(
        f"Limit pamięci: {mem_limit} | Czas wykonania: {exec_time:.2f} s | Liczba dzielnic: {len(grouped)}"
    )
except Exception as e:
    result_row["error"] = str(e)
    print(f"Limit pamięci: {mem_limit} | Błąd: {e}")

with open("stress_test_results_geopandas.csv", "a", newline="") as f:
    writer = csv.DictWriter(
        f, fieldnames=["mem_limit", "exec_time", "districts", "error"]
    )
    if f.tell() == 0:
        writer.writeheader()
    writer.writerow(result_row)
