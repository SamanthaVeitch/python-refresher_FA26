import array


def to_int(raw_value, fallback=-1):
    """Convert a string to an integer, with a fallback value."""
    try:
        return int(float(raw_value))
    except (ValueError, TypeError):
        print(
            f"Warning: could not convert "
            f"value '{raw_value}' to an integer, "
            f"replacing with {fallback}.")
        return fallback


def get_column(file_name, query_column, query_value, result_column=1):
    """Extract values from a CSV column based on matching row query.

    Arguments:
        file_name -- String of the file name to be opened
        query_column -- Int for the index of the column to search
        query_value -- String for the row value to search for
        result_column -- Int for the index of the column to return

    Returns:
        List of int values from the result_column
    """
    if not file_name.lower().endswith(".csv"):
        print(f"Error: '{file_name}' is not a CSV file.")
        return []

    results = []

    try:
        with open(file_name, "r") as file:
            for line in file:
                try:
                    values = line.strip().split(",")
                    if values[query_column] == query_value:
                        results.append(to_int(values[result_column], -1))
                except IndexError:
                    print(
                        f"Warning: Skipping incomplete data "
                        f"in line: {line.strip()}")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except PermissionError:
        print(f"Error: Permission to read '{file_name}' denied.")
    except IndexError:
        print(f"Error: Column index out of range in file '{file_name}'.")
    except Exception as e:
        print(f"Error: {e}")

    return results


def array_mean(input_array):
    """Calculate the mean of an array of numbers.
    Truncated to zero decimal places then calculated

    Arguments:
        array -- Array or list of ints

    Returns:
        Float mean value, or None if the array is empty
    """
    if isinstance(input_array, list):
        for i, value in enumerate(input_array):
            if not isinstance(value, (int, float)):
                print(f"Warning: Non-numeric value '{value}' at index {i}.")
                return None
            elif isinstance(value, float):
                print(f"Warning: Float value '{value}' "
                      f"at index {i}.")
                return None
        print("Warning: Input is a list, expected an array. "
              "Converting to array.")
        input_array = array.array('i', input_array)
    if not input_array or len(input_array) == 0:
        print("Warning: Cannot calculate mean of an empty array.")
        return None
    if input_array.typecode != 'i' and input_array.typecode != 'I':
        print("Warning: Array must be of type 'i' or 'I' (integer).")
        return None
    return sum(input_array) / len(input_array)


def array_median(input_array):
    """Calculate the median of an array of numbers.
    Truncated to zero decimal places then calculated

    Arguments:
        array -- Array or list of ints

    Returns:
        Float median value, or None if the array is empty
    """
    if isinstance(input_array, list):
        for i, value in enumerate(input_array):
            if not isinstance(value, (int, float)):
                print(f"Warning: Non-numeric value '{value}' at index {i}.")
                return None
            elif isinstance(value, float):
                print(f"Warning: Float value '{value}' "
                      f"at index {i}.")
                return None
        print("Warning: Input is a list, expected an array. "
              "Converting to array.")
        input_array = array.array('i', input_array)
    if not input_array or len(input_array) == 0:
        print("Warning: Cannot calculate median of an empty array.")
        return None
    if input_array.typecode != 'i' and input_array.typecode != 'I':
        print("Warning: Array must be of type 'i' or 'I' (integer).")
        return None
    sorted_array = sorted(input_array)
    n = len(sorted_array)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_array[mid - 1] + sorted_array[mid]) / 2.0
    else:
        return float(sorted_array[mid])


def array_std_dev(input_array):
    """Calculate the standard deviation of an array of numbers.
    Truncated to zero decimal places then calculated

    Arguments:
        array -- Array or lsit of ints

    Returns:
        Float standard deviation value, or None if the array is empty
    """
    if isinstance(input_array, list):
        for i, value in enumerate(input_array):
            if not isinstance(value, (int, float)):
                print(f"Warning: Non-numeric value '{value}' at index {i}.")
                return None
            elif isinstance(value, float):
                print(f"Warning: Float value '{value}' "
                      f"at index {i}.")
                return None
        print("Warning: Input is a list, expected an array. "
              "Converting to array.")
        input_array = array.array('i', input_array)
    if not input_array or len(input_array) == 0:
        print("Warning: Cannot calculate standard deviation "
              "of an empty array.")
        return None
    if input_array.typecode != 'i' and input_array.typecode != 'I':
        print("Warning: Array must be of type 'i' or 'I' (integer).")
        return None
    if len(input_array) < 2:
        print("Warning: Standard deviation requires at least two data points.")
        return None
    mean = array_mean(input_array)
    variance = sum((x - mean) ** 2 for x in input_array) / \
        (len(input_array) - 1)
    return variance ** 0.5
