import csv

def get_column(file_name, query_column, query_value, result_column):

    file = open(file_name, mode='r', encoding='utf-8', newline='')

    reader = csv.DictReader(file)

    if type(query_column) == str:
        if query_column not in reader.fieldnames:
            print(f"Error: Query ('{query_column}') not found. Defaulting to {reader.fieldnames[0]}.")
            query_column = reader.fieldnames[0]
    else:
        query_column = reader.fieldnames[query_column]
        


    if type(result_column) == str:
        if result_column not in reader.fieldnames:
            print(f"Error: Result ('{result_column}') not found. Defaulting to {reader.fieldnames[1]}.")
            result_column = reader.fieldnames[1]
    else:
        result_column = reader.fieldnames[result_column]


    results = []

    for row in reader:
        if row[query_column] == query_value:
            results.append(row[result_column])

    file.close()

    return results

