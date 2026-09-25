from pathlib import Path
import csv
import sys


def get_mean(array):
    """Calculate the mean value of a list of numbers.

    Parameters
    ----------
    array (list): A list of numbers. Intended for use with int.

    Returns
    -------
    mean (float): The mean value of the list.

    """

    mean = sum(array) / len(array)

    return mean


def get_median(array):
    """Find the median value of a list.

    Parameters
    ----------
    array (list): A list of numbers. Intended for use with int.

    Returns
    -------
    float: The median of the array.

    """

    array.sort()

    n = len(array)
    mid = n // 2

    if n % 2 == 0:
        # If even, average the two middle elements
        median = (array[mid - 1] + array[mid]) / 2
    else:
        median = array[mid]

    return median


def get_sd(array):
    """Calculate the standard deviation of a list of numbers.

    Parameters
    ----------
    array (list): The list of numbers. Intended for use with int.

    Returns
    -------
    sd (float): The standard deviation of the list.
    """

    mean = get_mean(array)
    n = len(array)

    sse = sum((x - mean)**2 for x in array)

    var = sse / n
    sd = var**0.5

    return sd


def get_column(file_name, query_column, query_value, result_column=1):

    """Read a csv file and returns a list of values from a specified column,
    based on a value [query_value] in a different column.

    Parameters
    ----------
    file_name : str
        The name of the csv

    query_column : int
        The column to check for query_value

    query_value : Any type
        The value to look for down query_column

    result_column : int
        The column to return values from, matching query_value

    Returns
    -------
    results
        List of int matching query_value, from result_column

    """

    file_path = Path(file_name)

    # Check if file exists and is a csv file.
    if not file_path.is_file():
        print(f"Error: File '{file_name}' not found in current directory.")
        sys.exit(1)

    if file_path.suffix.lower() != ".csv":
        print(f"Expected a .csv file, got {file_path.suffix}")
        sys.exit(1)

    with open(file_name, mode='r', encoding='utf-8', newline='') as file:

        reader = csv.reader(file)

        # Need to check to see how many columns reader has, so grab first
        # line and then reset the reader
        first_row = next(reader)
        num_columns = len(first_row)

        reader = csv.reader(file)

        # Only accept indices that can be transformed cleanly to int
        try:
            query_column = int(query_column)
        except (ValueError, TypeError):
            print(f"Error: Query column ('{query_column}') is not integer.")
            sys.exit(1)

        if query_column >= num_columns:
            print(f"Error: Query column ('{query_column}') out of bounds.")
            sys.exit(1)

        # 2 logic sets for 2 error messages, result and query
        try:
            result_column = int(result_column)
        except (ValueError, TypeError):
            print(f"Error: Result column ('{result_column}') is not integer.")
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
                try:
                    decimal = float(val)
                except (ValueError, TypeError):
                    print(f"Data must be numberic. Found {val}.")
                    sys.exit(1)
                    return results
                integer = int(decimal)
                results.append(integer)

        # Give user feedback if misspelled query_value or similar
        if len(results) == 0:
            print("No results found.")

    return results
