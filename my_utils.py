from pathlib import Path
import csv
import sys


def get_column(file_name, query_column, query_value, result_column=1):

    """
    Read a csv file and returns a list of values from a specified column [result_column],
    based on a value [query_value] in a different column [query_column].
    """

    file_path = Path(file_name)

    if not file_path.is_file():
        print(f"Error: File '{file_name}' not found in current directory.")
        sys.exit(1)

    if file_path.suffix.lower() != ".csv":
        print(f"Expected a .csv file, got {file_path.suffix}")
        sys.exit(1)

    with open(file_name, mode='r', encoding='utf-8', newline='') as file:

        reader = csv.reader(file)

        first_row = next(reader)
        num_columns = len(first_row)

        reader = csv.reader(file)

        try:
            query_column = int(query_column)
        except (ValueError, TypeError):
            print(f"Error: Query column ('{query_column}') is not an integer.")
            sys.exit(1)

        if query_column >= num_columns:
            print(f"Error: Query column ('{query_column}') out of bounds.")
            sys.exit(1)

        try:
            result_column = int(result_column)
        except (ValueError, TypeError):
            print(f"Error: Result column ('{result_column}') is not an integer.")
            sys.exit(1)

        if result_column >= num_columns:
            print(f"Error: Result column ('{result_column}') out of bounds.")
            sys.exit(1)

        results = []

        for row in reader:
            if row[query_column] == query_value:
                val = row[result_column]
                val = val.replace(',', '')
                val = val.replace(' ', '')
                decimal = float(val)
                integer = int(decimal)
                results.append(integer)

        if len(results) == 0:
            print("No results found.")

    return results
