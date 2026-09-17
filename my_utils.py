def get_column(file_name, query_column, query_value, result_column=1):
    """Extract values from a CSV column based on mathcing row query.

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
                    raw_value = values[result_column]
                    try:
                        results.append(int(float(raw_value)))
                    except ValueError:
                        print(
                            f"Error: could not convert "
                            f"value '{raw_value}' to an integer, "
                            f"replacing with -1.")
                        results.append(-1)

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except PermissionError:
        print(f"Error: Permission to read '{file_name}' denied.")
    except IndexError:
        print(f"Error: Column index out of range in file '{file_name}'.")
    except Exception as e:
        print(f"Error: {e}")

    return results
