from ast import In
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

        try:
            query_column = int(query_column)
            query_column = fieldnames[query_column]
        except (ValueError, TypeError):
            if query_column not in fieldnames:
                print(f"Error: Query ('{query_column}') not found."
                      f" Defaulting to {fieldnames[0]}.")
                query_column = fieldnames[0]
        except IndexError:
            print(f"Error: Query index ({query_column}) out of bounds."
                  f" Defaulting to {fieldnames[0]}.")
            query_column = fieldnames[0]

        try:
            result_column = int(result_column)
            result_column = fieldnames[result_column]
        except (ValueError, TypeError):
            if result_column not in fieldnames:
                print(f"Error: Result ('{result_column}') not found."
                      f" Defaulting to {fieldnames[1]}.")
                result_column = fieldnames[1]
        except IndexError:
            print(f"Error: Result index ({result_column}) out of bounds."
                  f" Defaulting to {fieldnames[1]}.")
            result_column = fieldnames[1]

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

