from my_utils import get_column
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_name", type=str, help='Name of file')
parser.add_argument("query_column", type=int, help='Column to look down')
parser.add_argument("query_value", help='Value to look for')
parser.add_argument("result_column", help='Column to grab from',
                    nargs='?', default=1)

args = parser.parse_args()

query_value = args.query_value
query_column = args.query_column
result_column = args.result_column
file_name = args.file_name
fires = get_column(file_name, query_column, query_value, result_column)

print(fires)
