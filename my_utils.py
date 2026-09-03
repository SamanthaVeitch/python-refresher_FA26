def get_column(file_name, query_column, query_value, result_column=1):
    """Extract values from a CSV column based on mathcing row query.

    Arguments:
        file_name -- String of the file name to be opened
        query_column -- Integer representing the index of the column to search
        query_value -- String representing the row value to search for
        result_column -- Integer representing the index of the column to return, defaults to 1

    Returns:
        List of values from the result_column where the query_column element matches the query_value
    """
    with open(file_name, 'r') as file:
        results = []
        for line in file:
            values = line.strip().split(',')
            if values[query_column] == query_value:
                results.append(values[result_column])
    return results
