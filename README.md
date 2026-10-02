# Agrofood CO2 Emissions Query

This project runs from the command line, reads a CSV file, and searches for rows where a given column matches a requested string. It then returns values from another column, converting them to integers when possible.

The program can also calculate the mean, median, or standard deviation of the returned values directly from the command line.

The project is built around the `my_utils.py` helper module and the `print_fires.py` command-line program. Automated unit tests, functional tests, style checks, and GitHub Actions workflows are included.

## Installation

### Prerequisites

- Python 3.x
- Mamba
- Git

### Clone the repository

```powershell
git clone git@github.com:SamanthaVeitch/python-refresher_FA26.git
```

Move into the project directory:

```powershell
cd python-refresher_FA26
```

### Create the Mamba environment

Create the environment from `environment.yml`:

```powershell
mamba env create -f environment.yml
```

Activate the environment:

```powershell
mamba activate assignments
```

Verify that the environment was created successfully:

```powershell
mamba list
```

### Environment information

The project uses a Mamba environment named `assignments`.

The environment is defined in `environment.yml`:

```yaml
name: assignments
channels:
  - conda-forge
dependencies:
  - pycodestyle
```

`pycodestyle` is used to check Python files for PEP 8 style violations.

The Python version is not pinned in `environment.yml`, so Mamba will use the Python version resolved by the environment.

If the environment file changes, update the existing environment with:

```powershell
mamba env update -f environment.yml --prune
```

To remove the environment:

```powershell
mamba env remove -n assignments
```

## Functions

`my_utils.py` provides five helper functions.

### `to_int(raw_value, fallback=-1)`

Converts a value to an integer.

If the value cannot be converted because of a `ValueError` or `TypeError`, the function prints a warning and returns the fallback value.

Example:

```python
to_int("42")
```

returns:

```text
42
```

### `get_column(file_name, query_column, query_value, result_column=1)`

Reads a CSV file and searches each row for a value matching `query_value` in the specified `query_column`.

When a match is found, the value in `result_column` is converted to an integer and added to the returned list.

The function also handles:

- non-CSV filenames
- missing files
- permission errors
- incomplete rows
- values that cannot be converted to integers

### `array_mean(input_array)`

Calculates the mean of an integer array or integer list.

Python lists containing integers are automatically converted to an integer `array.array`.

The function returns `None` for:

- empty inputs
- lists containing floating-point values
- lists containing non-numeric values
- arrays that are not integer arrays

### `array_median(input_array)`

Calculates the median of an integer array or integer list.

Python integer lists are automatically converted to integer arrays before the calculation.

The function supports both odd-length and even-length data and sorts the values before calculating the median.

### `array_std_dev(input_array)`

Calculates the sample standard deviation of an integer array or integer list.

The function requires at least two values.

Python integer lists are automatically converted to integer arrays before the calculation.

## Command-line usage

Run the program with Python:

```powershell
python print_fires.py --country "United States of America" --file_name "Agrofood_co2_emission.csv" --county_column 0 --fires_column 3
```

This command:

- searches column `0` for `United States of America`
- returns values from column `3`
- converts the returned values to integers
- prints the resulting list

Example output:

```python
[123, 456, 789]
```

## Statistical operations

Use the optional `--operation` argument to calculate a statistic instead of printing the raw list.

### Mean

```powershell
python print_fires.py --country "United States of America" --file_name "Agrofood_co2_emission.csv" --county_column 0 --fires_column 3 --operation mean
```

Accepted mean operations:

```text
mean
Mean
```

### Median

```powershell
python print_fires.py --country "United States of America" --file_name "Agrofood_co2_emission.csv" --county_column 0 --fires_column 3 --operation median
```

Accepted median operations:

```text
median
Median
```

### Standard deviation

```powershell
python print_fires.py --country "United States of America" --file_name "Agrofood_co2_emission.csv" --county_column 0 --fires_column 3 --operation std_dev
```

Accepted standard deviation operations:

```text
std_dev
std
stdev
```

If `--operation` is omitted, the raw list of matching values is printed.

## Testing

The project contains unit tests, functional tests, and automated style checking.

### Unit tests

Unit tests are contained in:

```text
test_my_utils.py
```

The unit tests cover all five functions in `my_utils.py`:

- `to_int`
- `get_column`
- `array_mean`
- `array_median`
- `array_std_dev`

Test coverage includes:

- successful CSV queries
- multiple matching rows
- missing files
- non-CSV files
- malformed CSV rows
- no matching rows
- failed numeric conversions
- `None` values
- positive values
- negative values
- zero values
- mixed-sign values
- empty arrays
- integer lists
- unsigned integer arrays
- non-numeric list values
- floating-point list values
- single-value arrays
- unsorted arrays
- randomized values compared against Python's `statistics` module

Run the unit tests from PowerShell:

```powershell
python -m unittest test_my_utils.py
```

## Functional tests

Functional tests exercise `print_fires.py` as a complete command-line program.

The functional test script is:

```text
tests/functional/test_print_fires.sh
```

The tests use the `ssshtest` framework and a checked-in test CSV file so that the tests do not depend on the full emissions dataset.

The functional tests cover:

- successful command execution
- missing required arguments
- non-integer column arguments
- missing input files
- unsupported operations
- default raw-list output
- malformed numeric values
- fallback conversion to `-1`
- no matching country
- mean
- `Mean`
- median
- `Median`
- `std_dev`
- `std`
- `stdev`
- standard deviation with only one matching value

Because the functional test file is a shell script, run it from Git Bash:

```bash
bash tests/functional/test_print_fires.sh
```

The test script downloads `ssshtest` automatically with `curl` if it is not already available.

## Windows and Git Bash

When using Mamba on Windows, some executable files may be located in:

```text
Library\bin
```

rather than a standard Unix-style `bin` directory.

If Git Bash cannot find a program from the active Mamba environment, run the following from PowerShell:

```powershell
$env:PATH = "$env:CONDA_PREFIX\Library\bin;$env:PATH"
```

Then run the required `.sh` file using Git Bash.

## Style checking

The project uses `pycodestyle` to check Python code for PEP 8 style violations.

Run the style check locally from PowerShell:

```powershell
pycodestyle .
```

A successful style check produces no output and exits with status code `0`.

## Continuous Integration

Continuous integration is implemented with GitHub Actions.

The workflows run on Linux using:

```yaml
runs-on: ubuntu-latest
```

Three separate workflow files are stored in:

```text
.github/workflows/
```

### Style workflow

```text
.github/workflows/style_check.yml
```

This workflow:

- checks out the repository
- sets up Python
- installs `pycodestyle`
- runs `pycodestyle .`

### Unit test workflow

```text
.github/workflows/unit_tests.yml
```

This workflow:

- checks out the repository
- sets up Python
- runs the unit tests with:

```text
python -m unittest test_my_utils.py
```

### Functional test workflow

```text
.github/workflows/functional_tests.yml
```

This workflow:

- checks out the repository
- sets up Python
- runs the functional tests with:

```text
bash tests/functional/test_print_fires.sh
```

## GitHub Actions triggers

All three workflows run whenever any branch is pushed:

```yaml
on:
  push:
```

They also run whenever a pull request targets the `master` branch:

```yaml
pull_request:
  branches:
    - master
```

The complete trigger configuration is:

```yaml
on:
  push:
  pull_request:
    branches:
      - master
```

This means continuous integration runs:

- whenever any branch is pushed
- whenever a pull request is opened against `master`
- whenever additional commits are pushed to a pull request targeting `master`

The three workflows run independently so style errors, unit-test failures, and functional-test failures can be identified separately.

## Continuous integration development workflow

A typical development workflow for this project is:

1. Update the local `master` branch.

```powershell
git checkout master
git pull origin master
```

2. Create a feature branch.

```powershell
git checkout -b feature_branch_name
```

3. Make the required changes.

4. Run the appropriate tests locally.

For Python changes:

```powershell
python -m unittest test_my_utils.py
pycodestyle .
```

For functional changes, run from Git Bash:

```bash
bash tests/functional/test_print_fires.sh
```

5. Commit the changes.

```powershell
git add .
git commit -m "Description of change"
```

6. Push the feature branch.

```powershell
git push -u origin feature_branch_name
```

7. Verify that the GitHub Actions workflows pass.

8. Open a pull request from the feature branch into `master`.

9. Merge the pull request after the automated checks pass.

10. Update the local `master` branch before beginning the next feature.

```powershell
git checkout master
git pull origin master
```

## Change log

### v1.0

- Initial project version
- Added CSV search helper in `my_utils.py`
- Added simple test in `print_fires.py`
- Added example runner in `run.sh`

### v2.0

- Added command-line interface in `print_fires.py`
- Added exception handling in `my_utils.py`
- Added environment configuration with `environment.yml`
- Added example runner with successful and failing cases

### v3.0

- Added `array_mean`
- Added `array_median`
- Added `array_std_dev`
- Added the `--operation` command-line argument
- Added unit tests for all five helper functions
- Added functional tests for `print_fires.py`
- Added checked-in functional test data

### v4.0

- Added integer-list handling to the statistical helper functions
- Fixed list handling by preventing the function argument from shadowing the Python `array` module
- Expanded unit-test coverage
- Added successful `get_column` testing
- Added additional type-error testing
- Added list-handling tests
- Added unsorted-data tests
- Added randomized statistical tests
- Added an unsupported-operation functional test
- Added GitHub Actions continuous integration
- Added a dedicated style-check workflow
- Added a dedicated unit-test workflow
- Added a dedicated functional-test workflow
- Configured workflows to run on every branch push
- Configured workflows to run on pull requests targeting `master`

## Author

Samantha Veitch