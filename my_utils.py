import array


def to_int(raw_value, fallback=-1):
    """Convert a string to an integer, with a fallback value."""
    try:
        return int(float(raw_value))
    except (ValueError, TypeError):
        print(
            f"Error: could not convert "
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
                values = line.strip().split(",")
                if values[query_column] == query_value:
                    results.append(to_int(values[result_column], -1))

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except PermissionError:
        print(f"Error: Permission to read '{file_name}' denied.")
    except IndexError:
        print(f"Error: Column index out of range in file '{file_name}'.")
    except Exception as e:
        print(f"Error: {e}")

    return results


def array_mean(array):
    """Calculate the mean of an array of numbers.

    Arguments:
        array -- Array of ints

    Returns:
        Float mean value, or None if the array is empty
    """
    if not array:
        print("Error: Cannot calculate mean of an empty array.")
        return None
    if array.typecode != 'i' and array.typecode != 'I':
        print("Error: Array must be of type 'i' or 'I' (integer).")
        return None
    return sum(array) / len(array)


def array_median(array):
    """Calculate the median of an array of numbers.

    Arguments:
        array -- Array of ints

    Returns:
        Float median value, or None if the array is empty
    """
    if not array:
        print("Error: Cannot calculate median of an empty array.")
        return None
    if array.typecode != 'i' and array.typecode != 'I':
        print("Error: Array must be of type 'i' or 'I' (integer).")
        return None
    sorted_array = sorted(array)
    n = len(sorted_array)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_array[mid - 1] + sorted_array[mid]) / 2.0
    else:
        return float(sorted_array[mid])


def array_std_dev(array):
    """Calculate the standard deviation of an array of numbers.

    Arguments:
        array -- Array of ints

    Returns:
        Float standard deviation value, or None if the array is empty
    """
    if not array:
        print("Error: Cannot calculate standard deviation of an empty array.")
        return None
    if array.typecode != 'i' and array.typecode != 'I':
        print("Error: Array must be of type 'i' or 'I' (integer).")
        return None
    mean = array_mean(array)
    variance = sum((x - mean) ** 2 for x in array) / len(array)
    return variance ** 0.5
