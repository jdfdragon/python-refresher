from my_utils import get_column
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_name")
parser.add_argument("query_column")
parser.add_argument("query_value")
parser.add_argument("result_column", default=1)

args = parser.parse_args()

country = args.query_value
country_column = args.query_column
fires_column = args.result_column
file_name = args.file_name
fires = get_column(file_name, country_column, country, fires_column)

print(fires)
