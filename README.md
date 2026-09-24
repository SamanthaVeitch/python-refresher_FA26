# Agrofood CO2 Emissions Query

This project runs from the command line, reads a CSV file, and searches for rows where a given column matches a given string. It then prints the values from a second requested column, converting them to integers when possible. It can also compute the mean, median, or standard deviation of the returned values directly from the command line.

This project is built around the `my_utils.py` helper and the `print_fires.py` script, and it is designed to make it easy to inspect agricultural and food-sector emissions data from a CSV dataset.

## Installation

### Prerequisites
- Python 3.x
- mamba
- Git

### Steps to Install
Clone the repository:
```sh
git clone git@github.com:SamanthaVeitch/python-refresher_FA26.git
```
Move into the project directory:
```sh
cd python-refresher_FA26
```
Create the mamba environment from the provided environment.yml file:
```sh
mamba env create -f environment.yml
```
Activate the environment:
```sh
mamba activate assignments
```
Verify the environment was set up correctly:
```sh
mamba list
```
### Environment Information
This project uses a dedicated mamba environment named assignments, defined in environment.yml:
```yaml
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
mamba env update -f environment.yml --prune
```
To remove the environment entirely (e.g. to rebuild it from scratch):
```sh
mamba env remove -n assignments
```

## Functions

`my_utils.py` provides the following functions:

- **`to_int(raw_value, fallback=-1)`** — Converts a string to an int, returning `fallback` if conversion fails.
- **`get_column(file_name, query_column, query_value, result_column=1)`** — Searches a CSV file for rows where `query_column` matches `query_value`, and returns the corresponding `result_column` values as a list of integers.
- **`array_mean(values)`** — Returns the mean of an array of integers.
- **`array_median(values)`** — Returns the median of an array of integers.
- **`array_std_dev(values)`** — Returns the standard deviation of an array of integers.

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

### Running an operation on the results

Pass `--operation` to compute a summary statistic on the matched values instead of printing the raw list:

```bash
python print_fires.py --country "United States of America" --file_name "Agrofood_co2_emission.csv" --county_column 0 --fires_column 3 --operation mean
```

Supported values for `--operation`:
- `mean` / `Mean` — average of the matched values
- `median` / `Median` — median of the matched values
- `std_dev` / `std` / `stdev` — standard deviation of the matched values

If `--operation` is omitted, the raw list of matched values is printed instead.

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

## Testing

### Unit tests

Unit tests cover all five functions in `my_utils.py`: `to_int`, `get_column`, `array_mean`, `array_median`, and `array_std_dev`. Each function is tested with a positive case, a zero case, a negative case, a type/value error case, and a randomized case.

Run the unit tests with:

```bash
python -m unittest discover -s tests/unit
```

### Functional tests

Functional tests for `print_fires.py` live in `tests/functional/` and use the [ssshtest](https://github.com/ryanlayer/ssshtest) framework. A small, checked-in test data file (`tests/functional/test_data/fires_test_data.csv`) is used so the tests are self-contained and don't depend on the full emissions dataset. The tests cover exit codes (success, missing arguments, bad input, missing files) and each of the supported operations (default list, mean, median, std_dev).

Run the functional tests with:

```bash
bash tests/functional/test_print_fires.sh
```

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

### v3.0
- Added `array_mean`, `array_median`, and `array_std_dev` functions to `my_utils.py`
- Added `--operation` flag to `print_fires.py` for computing mean, median, and standard deviation from the command line
- Added unit tests for all five functions in `my_utils.py`
- Added functional tests for `print_fires.py` with checked-in test data

## Author info
- Author: Samantha Veitch