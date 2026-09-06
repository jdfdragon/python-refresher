from pathlib import Path
import csv


def get_column(file_name, query_column, query_value, result_column=1):

    with open(file_name, mode='r', encoding='utf-8', newline='') as file:

        file_path = Path(file_name)

        if not file_path.is_file():
            print(f"Error: File '{file_name}' not found.")
            return []

        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames

        if not fieldnames:
            print("Error: File is empty or does not contain a header row.")

        if isinstance(query_column, str):
            if query_column not in reader.fieldnames:
                print(f"Error: Query ('{query_column}') not found."
                      f" Defaulting to {reader.fieldnames[0]}.")
                query_column = reader.fieldnames[0]
        elif isinstance(query_column, int):
            if 0 <= query_column < len(reader.fieldnames):
                query_column = reader.fieldnames[query_column]
            else:
                print(f"Error: Query index ({query_column}) out of bounds."
                      f" Defaulting to {reader.fieldnames[0]}.")
                query_column = reader.fieldnames[0]

        if type(result_column) is str:
            if result_column not in reader.fieldnames:
                print(f"Error: Result ('{result_column}') not found."
                      f" Defaulting to {reader.fieldnames[1]}.")
                result_column = reader.fieldnames[1]
        elif isinstance(result_column, int):
            if 0 <= result_column < len(reader.fieldnames):
                result_column = reader.fieldnames[result_column]
            else:
                print(f"Error: Result index ({result_column}) out of bounds."
                      f" Defaulting to {reader.fieldnames[1]}.")
                result_column = reader.fieldnames[1]

        results = []

        for row in reader:
            if row[query_column] == query_value:
                val = row[result_column]
                val = val.replace(',', '')
                val.replace(' ', '')
                decimal = float(val)
                integer = int(decimal)
                results.append(integer)

    return results
