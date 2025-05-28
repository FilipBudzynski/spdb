#!/bin/bash
# filepath: /Users/filipbudzynski/Studia/SPDB/spdb/run_all_stress_tests.sh

POSTGIS_CONTAINER="postgis-db"
GEOPANDAS_CONTAINER="python-gis"
MEM_LIMITS_POSTGIS=("2G" "1G" "512M" "256M" "128M" "64M")
MEM_LIMITS_PYTHON=("2G" "1G" "800M" "512M" "256M")
SWAP_MEM="4G"

echo "=== PostGIS tests ==="
for MEM in "${MEM_LIMITS_POSTGIS[@]}"
do
    echo ">> Setting PostGIS container memory to $MEM"
    docker update --memory $MEM --memory-swap $SWAP_MEM $POSTGIS_CONTAINER
    sleep 5
    docker exec $GEOPANDAS_CONTAINER poetry run python3 /workspace/stress_tests/stress_test_postgis.py $MEM
done

echo "=== GeoPandas tests ==="
for MEM in "${MEM_LIMITS_PYTHON[@]}"
do
    echo ">> Setting Python-GIS container memory to $MEM"
    docker update --memory $MEM --memory-swap $SWAP_MEM $GEOPANDAS_CONTAINER
    sleep 5
    docker exec $GEOPANDAS_CONTAINER poetry run python3 /workspace/stress_tests/stress_test_geopandas.py $MEM
done

echo "All tests finished. Check python/stress_test_results_postgis.csv and python/stress_test_results_geopandas.csv"
