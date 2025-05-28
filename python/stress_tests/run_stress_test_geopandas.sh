#!/bin/bash

CONTAINER_NAME="python-gis"
MEM_LIMITS=("2G" "1G" "800M" "512M" "256M")
SWAP_MEM="4G"

for MEM in "${MEM_LIMITS[@]}"
do
    echo "=== Test dla limitu pamięci: $MEM ==="
    docker update --memory $MEM --memory-swap $SWAP_MEM $CONTAINER_NAME
    sleep 5
    docker exec $CONTAINER_NAME poetry run python3 /workspace/stress_tests/stres_test_geopandas.py $MEM
done

echo "Wyniki w pliku stress_test_results_geopandas.csv"
