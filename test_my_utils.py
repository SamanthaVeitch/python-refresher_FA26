import array
import os
import random
import statistics
import tempfile
import unittest

import my_utils


class TestMyUtilsCSV(unittest.TestCase):
    """Tests for get_column(file_name, query_column, query_value,
    result_column=1)."""

    def setUp(self):
        self._temp_files = []

    def tearDown(self):
        for path in self._temp_files:
            if os.path.exists(path):
                os.remove(path)

    def _make_csv(self, rows, suffix=".csv"):
        """Write rows (list of comma-strings) to a temp file and
        return its path."""
        handle = tempfile.NamedTemporaryFile(
            mode="w", suffix=suffix, delete=False, newline=""
        )
        for row in rows:
            handle.write(row + "\n")
        handle.close()
        self._temp_files.append(handle.name)
        return handle.name

    def test_type_value_error_case_bad_conversion_returns_fallback(self):
        path = self._make_csv([
            "USA,not_a_number",
        ])
        result = my_utils.get_column(path, 0, "USA", result_column=1)
        self.assertEqual(result, [-1])

    def test_file_not_found_returns_empty_list(self):
        result = my_utils.get_column("does_not_exist.csv", 0, "USA")
        self.assertEqual(result, [])

    def test_non_csv_extension_returns_empty_list(self):
        path = self._make_csv(["USA,10"], suffix=".txt")
        result = my_utils.get_column(path, 0, "USA")
        self.assertEqual(result, [])

    def test_no_matching_rows_returns_empty_list(self):
        path = self._make_csv(["USA,10"])
        result = my_utils.get_column(path, 0, "Mexico")
        self.assertEqual(result, [])

    def test_malformed_row_is_skipped(self):
        path = self._make_csv([
            "USA,10",
            "USA",  # missing result_column, should be skipped
            "USA,20",
        ])
        result = my_utils.get_column(path, 0, "USA", result_column=1)
        self.assertEqual(result, [10, 20])


if __name__ == '__main__':
    unittest.main()
