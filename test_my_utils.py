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


class TestMyUtilsMath(unittest.TestCase):
    def setUp(self):
        self.test_array = array.array('i', [1, 2, 3, 4, 5])
        self.empty_array = array.array('i')

    def tearDown(self):
        self.test_array = None
        self.empty_array = None

    """Tests for to_int(raw_value, fallback=-1)."""

    def test_to_int_pos(self):
        self.assertEqual(my_utils.to_int("42"), 42)

    def test_to_int_zero(self):
        self.assertEqual(my_utils.to_int("0"), 0)

    def test_to_int_neg(self):
        self.assertEqual(my_utils.to_int("-17"), -17)

    def test_to_int_value_error_fallback(self):
        self.assertEqual(my_utils.to_int("not_a_number"), -1)

    def test_to_int_type_error_custom_fallback(self):
        self.assertEqual(my_utils.to_int("not_a_number", fallback=99), 99)

    def test_to_int_float_string_truncation(self):
        # int(float("3.7")) truncates rather than rounds.
        self.assertEqual(my_utils.to_int("3.7"), 3)

    def test_to_int_empty_string(self):
        self.assertEqual(my_utils.to_int(""), -1)

    """Tests for array_mean(values)."""

    def test_array_mean_pos(self):
        self.assertAlmostEqual(my_utils.array_mean(self.test_array), 3.0)

    def test_array_mean_zero(self):
        self.assertAlmostEqual(my_utils.array_mean(
            array.array('i', [0, 0, 0])), 0.0)

    def test_array_mean_neg(self):
        self.assertAlmostEqual(my_utils.array_mean(
            array.array('i', [-5, -10, -15])), -10.0)

    def test_array_mean_mixed_signs(self):
        self.assertAlmostEqual(my_utils.array_mean(
            array.array('i', [-5, 0, 5])), 0.0)

    def test_array_mean_non_numeric_value(self):
        self.assertIsNone(my_utils.array_mean([1, 2, 3, "four", 5]))

    def test_array_mean_empty_array(self):
        self.assertIsNone(my_utils.array_mean(self.empty_array))

    def test_array_mean_list(self):
        with self.assertRaises(AttributeError):
            my_utils.array_mean([1, 2, 3])

    def test_array_mean_unsigned_int_array(self):
        unsigned_array = array.array('I', [1, 2, 3])
        self.assertAlmostEqual(my_utils.array_mean(unsigned_array), 2.0)

    def test_array_mean_single_value(self):
        self.assertAlmostEqual(my_utils.array_mean(
            array.array('i', [7])), 7.0)

    def test_array_mean_random_values(self):
        for _ in range(1000):
            values = [random.randint(-1000, 1000) for _ in range(50)]
            expected = statistics.mean(values)
            self.assertAlmostEqual(my_utils.array_mean(
                array.array('i', values)), expected)

    """Tests for array_median(values)."""

    def test_array_median_pos(self):
        self.assertAlmostEqual(my_utils.array_median(self.test_array), 3.0)

    def test_array_median_zero(self):
        self.assertAlmostEqual(my_utils.array_median(
            array.array('i', [0, 0, 0])), 0.0)

    def test_array_median_neg(self):
        self.assertAlmostEqual(my_utils.array_median(
            array.array('i', [-5, -10, -15])), -10.0)

    def test_array_median_mixed_signs(self):
        self.assertAlmostEqual(my_utils.array_median(
            array.array('i', [-5, 0, 5])), 0.0)

    def test_array_median_non_numeric_value(self):
        self.assertIsNone(my_utils.array_median([1, 2, 3, "four", 5]))

    def test_array_median_empty_array(self):
        self.assertIsNone(my_utils.array_median(self.empty_array))

    def test_array_median_list(self):
        with self.assertRaises(AttributeError):
            my_utils.array_median([1, 2, 3])

    def test_array_median_unsigned_int_array(self):
        unsigned_array = array.array('I', [1, 2, 3])
        self.assertAlmostEqual(my_utils.array_median(unsigned_array), 2.0)

    def test_array_median_single_value(self):
        self.assertAlmostEqual(my_utils.array_median(
            array.array('i', [7])), 7.0)

    def test_array_median_random_values(self):
        for _ in range(1000):
            values = [random.randint(-1000, 1000) for _ in range(50)]
            expected = statistics.median(values)
            self.assertAlmostEqual(my_utils.array_median(
                array.array('i', values)), expected)

    """Tests for array_std_dev(values)."""

    def test_array_std_dev_pos(self):
        expected = statistics.stdev([2, 4, 4, 4, 5, 5, 7, 9])
        result = my_utils.array_std_dev(
            array.array('i', [2, 4, 4, 4, 5, 5, 7, 9]))
        self.assertAlmostEqual(result, expected)

    def test_array_std_dev_identical_values(self):
        self.assertAlmostEqual(my_utils.array_std_dev(
            array.array('i', [5, 5, 5, 5])), 0.0)

    def test_array_std_dev_neg(self):
        expected = statistics.stdev([-5, -10, -15])
        result = my_utils.array_std_dev(array.array('i', [-5, -10, -15]))
        self.assertAlmostEqual(result, expected)

    def test_array_std_dev_mixed_signs(self):
        expected = statistics.stdev([-5, 0, 5])
        result = my_utils.array_std_dev(array.array('i', [-5, 0, 5]))
        self.assertAlmostEqual(result, expected)

    def test_array_std_dev_single_value(self):
        self.assertIsNone(my_utils.array_std_dev(
            array.array('i', [7])))

    def test_array_std_dev_non_numeric_value(self):
        self.assertIsNone(my_utils.array_std_dev([1, 2, 3, "four", 5]))

    def test_array_std_dev_empty_array(self):
        self.assertIsNone(my_utils.array_std_dev(self.empty_array))

    def test_array_std_dev_list(self):
        with self.assertRaises(AttributeError):
            my_utils.array_std_dev([1, 2, 3])

    def test_array_std_dev_unsigned_int_array(self):
        unsigned_array = array.array('I', [1, 2, 3])
        self.assertAlmostEqual(my_utils.array_std_dev(unsigned_array), 1.0)

    def test_array_std_dev_random_values(self):
        for _ in range(1000):
            values = [random.randint(-1000, 1000) for _ in range(50)]
            expected = statistics.stdev(values)
            self.assertAlmostEqual(my_utils.array_std_dev(
                array.array('i', values)), expected)


if __name__ == '__main__':
    unittest.main()
