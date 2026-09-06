from my_utils import get_column
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_name")
parser.add_argument("query_column")
parser.add_argument("query_value")
parser.add_argument("result_column", nargs='?', default=1)

args = parser.parse_args()

query_value = args.query_value
query_column = args.query_column
result_column = args.result_column
file_name = args.file_name
fires = get_column(file_name, query_column, query_value, result_column)

print(fires)
