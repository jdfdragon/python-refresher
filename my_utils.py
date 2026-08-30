import csv

def get_column(file_name, query_column, query_value, result_column):
    file = open(file_name, mode='r', encoding='utf-8', newline='')
    
    reader = csv.reader(file)

    results = []

    for row in reader:

        if row[query_column] == query_value:
            results.append(row[result_column])

    file.close()

    return results
