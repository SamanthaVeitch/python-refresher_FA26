#!/bin/bash

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

#Download data file from Google Drive
curl -L "https://docs.google.com/uc?export=download&id=1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr" -o Agrofood_co2_emission.csv
echo "-----------------------------------------------"

#runs py script
python3 -u print_fires.py

#asks to remove data file
if [ -f "Agrofood_co2_emission.csv" ]; then
    echo "-----------------------------------------------"
    echo "Would you like to delete the temporary downloaded file?"
    rm -i Agrofood_co2_emission.csv
fi