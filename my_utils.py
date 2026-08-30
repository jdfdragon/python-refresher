import csv

def get_column(file_name, query_column, query_value, result_column):

    file = open(file_name, mode='r', encoding='utf-8', newline='')

    if type(query_column) == str:
        reader = csv.DictReader(file)
        if query_column not in reader.fieldnames:
            print(f"Error: Query ('{query_column}') not found. Defaulting to {reader.fieldnames[0]}.")
        if result_column not in reader.fieldnames:
            print(f"Error: Result ('{result_column}') not found. Defaulting to {reader.fieldnames[1]}.")
    else:
        reader = csv.reader(file)

    results = []

    for row in reader:
        if row[query_column] == query_value:
            results.append(row[result_column])

    file.close()

    return results

