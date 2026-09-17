# Agrofood CO2 Emissions Query

This project runs from the command line reads a CSV file and searches for rows where a given column matches a given string. It then prints the values from a second requested column, converting them to integers when possible.

This project is built around the `my_utils.py` helper and the `print_fires.py` script, and it is designed to make it easy to inspect agricultural and food-sector emissions data from a CSV dataset.

## Installation

### Prerequisites
- Python 3.x
- mamba
- Git

### Steps to Install
Clone the repository:
```sh
bash git clone git@github.com:SamanthaVeitch/python-refresher_FA26.git
```
Move into the project directory:
```sh
bash cd repository-name
```
Create the mamba environment from the provided environment.yml file:
```sh
bash mamba env create -f environment.yml
```
Activate the environment:
```sh
bash mamba activate assignments
```
Verify the environment was set up correctly:
```sh
bash mamba list
```
### Environment Information
This project uses a dedicated mamba environment named assignments, defined in environment.yml:
```sh
yaml
channels:
  - conda-forge
dependencies:
  - pycodestyle
```
Channel: conda-forge
Dependencies: pycodestyle (used for PEP 8 style checking)
Python version: not pinned in the environment file — the environment will use whichever Python 3.x version mamba/conda-forge resolves by default. If you need a specific version, add it explicitly to environment.yml (e.g. - python=3.11).

If the environment file changes in the future, update your local environment with:
```sh
bash mamba env update -f environment.yml --prune
```
To remove the environment entirely (e.g. to rebuild it from scratch):
```sh
bash mamba env remove -n assignments
```


## Example usage

Run the script directly with Python:

```bash
python print_fires.py --country "United States of America" --file_name "Agrofood_co2_emission.csv" --county_column 0 --fires_column 3
```

This command does the following:
- Looks for rows where column `0` matches `United States of America`
- Returns values from column `3`
- Prints the result list to the terminal

Example output:

```python
[123, 456, 789]
```

You can also use the included helper script:

```bash
bash run.sh
```
For Windows Mamba users, tools can be installed under ...Library\bin\ folder not the .../bin/bash folder.
You may need to run this script to bypass a not found error
```sh
$env:PATH = "$env:CONDA_PREFIX\Library\bin;$env:PATH"; bash ./run.sh
```

That script runs a few example queries, including success, index error, and missing-file cases.


## Change log

### v1.0
- Initial project version
- Added CSV search helper in `my_utils.py`
- Added simple test in `print_fires.py`
- Added example runner in `run.sh`

### v2.0
- Added CLI interface in `print_fires.py`
- Added exeption handling in `my_utils.py`
- Added environment configuration via `environment.yml`
- Added example runner with success and failures in `run.sh`


## Author info
- Author: Samantha Veitch