import psycopg2
import geopandas as gpd
import matplotlib.pyplot as plt
import time
from shapely import wkb  

HOST = "postgis"
PORT = "5432"
USER = "postgres"
PASSWORD = "postgres"
DBNAME = "gis_db"

conn = psycopg2.connect(
    host=HOST,
    port=PORT,
    user=USER,
    password=PASSWORD,
    dbname=DBNAME
)

cur = conn.cursor()

query = """
    SELECT p.name, p.amenity, p.shop, p.tourism, p.leisure, a.name AS park_name, p.way
    FROM planet_osm_point p
    JOIN planet_osm_polygon a ON ST_Contains(a.way, p.way)
    WHERE a.leisure = 'park'
    AND p.name IS NOT NULL
    LIMIT 1000;
"""

start_time = time.time()

cur.execute(query)
rows = cur.fetchall()

end_time = time.time()
execution_time = end_time - start_time
print(f"Query time of execution: {execution_time:.4f} sec")

cur.close()

columns = ['name', 'amenity', 'shop', 'tourism', 'leisure', 'park_name', 'geom']
df = gpd.pd.DataFrame(rows, columns=columns)

df['geometry'] = df['geom'].apply(wkb.loads)

gdf = gpd.GeoDataFrame(df, geometry="geometry")
conn.close()

print(gdf.head())

gdf.plot(marker='o', color='red', markersize=5)
plt.title("POI in the parks")
plt.show()
