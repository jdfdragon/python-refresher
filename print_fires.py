from my_utils import get_column
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-file", type=str, help='Name of file')
parser.add_argument("-q_col", type=int, help='Column to look down')
parser.add_argument("-q_val", help='Value to look for')
parser.add_argument("-res_col", help='Column to grab from',
                    nargs='?', default=1)

args = parser.parse_args()

query_value = args.q_val
query_column = args.q_col
result_column = args.res_col
file_name = args.file
fires = get_column(file_name, query_column, query_value, result_column)

print(fires)
