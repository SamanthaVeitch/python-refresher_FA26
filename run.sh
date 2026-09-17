#!/bin/bash

#For Windows Mamba users, tools can be installed under ...Library\bin\ folder not the .../bin/bash folder.
# Automatically inject the Mamba path IF the user is running Windows native (Git Bash/MSYS)
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    if [ -n "$CONDA_PREFIX" ]; then
        export PATH="$CONDA_PREFIX/Library/bin:$PATH"
    fi
fi

#You may need to run this script to bypass a not found error
#$env:PATH = "$env:CONDA_PREFIX\Library\bin;$env:PATH"; bash ./run.sh

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

# Ask the user for the file path
echo "Please enter the path to your data file:"
read -r FILE_PATH
if [ ! -f "$FILE_PATH" ]; then
    #if file does not exist, replace with google drive link
    echo "Error: File '$FILE_PATH' does not exist."
    echo "Downloading from Google Drive..."
    curl -L "https://docs.google.com/uc?export=download&id=1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr" -o Agrofood_co2_emission.csv
    FILE_PATH="Agrofood_co2_emission.csv"
fi
echo "----------------------------------------------"
echo

echo "-----------------Success Run------------------"
python -u print_fires.py --country "United States of America" --file_name "Agrofood_co2_emission.csv" --county_column 0 --fires_column 3
echo

echo "-----------------Index Error------------------"
python -u print_fires.py --country "United States of America" --file_name "Agrofood_co2_emission.csv" --county_column 0 --fires_column 33
echo

echo "------------------File Error------------------"
python -u print_fires.py --country "United States of America" --file_name "data.csv" --county_column 0 --fires_column 3
echo

#Ask to remove data file
if [ -f "Agrofood_co2_emission.csv" ]; then
    echo
    echo "----------------------------------------------"
    echo "Would you like to delete the data file?"
    rm -i Agrofood_co2_emission.csv
fi