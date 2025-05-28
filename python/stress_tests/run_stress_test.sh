#!/bin/bash

CONTAINER_NAME="postgis-db"
MEM_LIMITS=("2G" "1G" "512M" "256M" "128M" "64M")
SWAP_MEM="4G"

for MEM in "${MEM_LIMITS[@]}"
do
    echo "=== Test dla limitu pamięci: $MEM ==="
    docker update --memory $MEM --memory-swap $SWAP_MEM $CONTAINER_NAME
    sleep 5
    python3 stres_test.py $MEM
done

echo "Wyniki w pliku stress_test_results_postgis.csv"