import my_utils
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-file", type=str, help='Name of file')
parser.add_argument("-q_col", help='Column to look down')
parser.add_argument("-q_val", help='Value to look for')
parser.add_argument("-res_col", help='Column to grab from',
                    nargs='?', default=1)
parser.add_argument('-stat', type=str, help="Statistic to generate")

args = parser.parse_args()

query_value = args.q_val
query_column = args.q_col
result_column = args.res_col
file_name = args.file
fires = my_utils.get_column(file_name, query_column, query_value, result_column)

if args.stat:
    if args.stat == "mean":
        mean = my_utils.get_mean(fires)
        print(mean)
    elif args.stat == "median":
        median = my_utils.get_median(fires)
        print(median)
    elif args.stat == "sd":
        sd = my_utils.get_sd(fires)
        print(sd)
    else:
        print(f"Error: Invalid statistic requested '{args.stat}'.")
        sys.exit(1)
else:
    print(fires)
