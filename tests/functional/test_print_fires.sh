#!/bin/bash
#


set -uo pipefail

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------

# Using curl instead of wget since curl ships by default with
# Git for Windows, whereas wget often does not.
if [ ! -s ssshtest ]; then
    curl -sSL -o ssshtest \
        https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
fi

#test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

TEST_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PRINT_FIRES="${TEST_DIR}/../../print_fires.py"
TEST_DATA="${TEST_DIR}/test_data/test_data.csv"
PYTHON="${PYTHON:-python}"

# ---------------------------------------------------------------------------
# Exit code tests
# ---------------------------------------------------------------------------

run test_exit_code_success \
    "$PYTHON" "$PRINT_FIRES" \
    --country  "United States of America" --file_name "$TEST_DATA" \
    --county_column 0 --fires_column 3
assert_exit_code 0

run test_exit_code_missing_required_argument \
    "$PYTHON" "$PRINT_FIRES" \
    --file_name "$TEST_DATA" --county_column 0 --fires_column 2
assert_exit_code 2

run test_exit_code_non_integer_column \
    "$PYTHON" "$PRINT_FIRES" \
    --country "United States of America" --file_name "$TEST_DATA" \
    --county_column not_an_int --fires_column 3
assert_exit_code 2

run test_exit_code_missing_file_is_handled_gracefully \
    "$PYTHON" "$PRINT_FIRES" \
    --country "United States of America" --file_name does_not_exist.csv \
    --county_column 0 --fires_column 3
assert_exit_code 0
assert_in_stdout "[]"

run test_exit_code_std_dev_on_single_value_fails \
    "$PYTHON" "$PRINT_FIRES" \
    --country Zero --file_name "$TEST_DATA" \
    --county_column 0 --fires_column 3 --operation std_dev
assert_exit_code 0

# ---------------------------------------------------------------------------
# Default operation (no --operation given): raw list of ints
# ---------------------------------------------------------------------------

run test_default_operation_returns_raw_list \
    "$PYTHON" "$PRINT_FIRES" \
    --country "United States of America" --file_name "$TEST_DATA" \
    --county_column 0 --fires_column 3
assert_equal "[1999, 1999, 1999, 1999, 1999, 1999, 3286, 1553, 3099, 3578, 3687, 534, 1475, 1224, 1201, 915, 1086, 1558, 2068, 1093, 912, 1330, 1173, 1284, 1336, 2235, 1438, 2664, 2457, 1190, 5405]" "$(cat "$STDOUT_FILE")"

run test_default_operation_malformed_value_uses_fallback \
    "$PYTHON" "$PRINT_FIRES" \
    --country "Malformed" --file_name "$TEST_DATA" \
    --county_column 0 --fires_column 3
assert_in_stdout "-1"

run test_default_operation_no_match_returns_empty_list \
    "$PYTHON" "$PRINT_FIRES" \
    --country "Nowhere" --file_name "$TEST_DATA" \
    --county_column 0 --fires_column 3
assert_equal "[]" "$(cat "$STDOUT_FILE")"

# ---------------------------------------------------------------------------
# Operation: mean / Mean
# ---------------------------------------------------------------------------

run test_mean_operation \
    "$PYTHON" "$PRINT_FIRES" \
    --country "Finland" --file_name "$TEST_DATA" \
    --county_column 0 --fires_column 3 --operation mean
assert_exit_code 0
assert_in_stdout "0.29"

run test_mean_operation_case_insensitive \
    "$PYTHON" "$PRINT_FIRES" \
    --country "Finland" --file_name "$TEST_DATA" \
    --county_column 0 --fires_column 3 --operation Mean
assert_exit_code 0
assert_in_stdout "0.29"

# ---------------------------------------------------------------------------
# Operation: median / Median
# ---------------------------------------------------------------------------

run test_median_operation \
    "$PYTHON" "$PRINT_FIRES" \
    --country "Madagascar" --file_name "$TEST_DATA" \
    --county_column 0 --fires_column 3 --operation median
assert_exit_code 0
assert_in_stdout "659"

run test_median_operation_case_insensitive \
    "$PYTHON" "$PRINT_FIRES" \
    --country "Madagascar" --file_name "$TEST_DATA" \
    --county_column 0 --fires_column 3 --operation Median
assert_exit_code 0
assert_in_stdout "659"

# ---------------------------------------------------------------------------
# Operation: std_dev / std / stdev
# ---------------------------------------------------------------------------

run test_std_dev_operation \
    "$PYTHON" "$PRINT_FIRES" \
    --country "United States of America" --file_name "$TEST_DATA" \
    --county_column 0 --fires_column 3 --operation std_dev
assert_exit_code 0
assert_in_stdout "1024.36"

run test_std_dev_operation_alias_std \
    "$PYTHON" "$PRINT_FIRES" \
    --country "United States of America" --file_name "$TEST_DATA" \
    --county_column 0 --fires_column 3 --operation std
assert_exit_code 0
assert_in_stdout "1024.36"

run test_std_dev_operation_alias_stdev \
    "$PYTHON" "$PRINT_FIRES" \
    --country "United States of America" --file_name "$TEST_DATA" \
    --county_column 0 --fires_column 3 --operation stdev
assert_exit_code 0
assert_in_stdout "1024.36"
