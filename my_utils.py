def get_column(file_name, query_column, query_value, result_column):
    with open(file_name, 'r') as file:
        results = []
        for line in file:
            values = line.strip().split(',')
            if values[query_column] == query_value:
                results.append(values[result_column])
    return results
