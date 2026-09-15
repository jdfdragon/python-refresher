from pathlib import Path
import csv
import sys


def get_column(file_name, query_column, query_value, result_column=1):

    with open(file_name, mode='r', encoding='utf-8', newline='') as file:

        # test file path
        file_path = Path(file_name)

        if not file_path.is_file():
            print(f"Error: File '{file_name}' not found.")
            return []

        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames

        # Since argparse passes strings, we need to interpret as integers
        # Or we can test them and then shove them through

        if query_column not in fieldnames:
            try:
                query_column = int(query_column)
            except (ValueError, TypeError):
                print(f"Error: Query ('{query_column}') not found.")
                sys.exit(1)
                return 

        if result_column not in fieldnames:
            try:
                result_column = int(result_column)
            except (ValueError, TypeError):
                print(f"Error: Result ('{result_column}') not found.")
                sys.exit(1)
                return

        if not isinstance(query_column, int) and not isinstance(result_column, int):
            reader = csv.Reader(file)

        results = []

        for row in reader:
            if row[query_column] == query_value:
                val = row[result_column]
                val = val.replace(',', '')
                val = val.replace(' ', '')
                decimal = float(val)
                integer = int(decimal)
                results.append(integer)

    print(f"Column '{result_column}' by '{query_column}:")
    
    return results
