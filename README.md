# python-refresher

This file contains utilities and functions to enable the easy reading and searching inside of csv files. While tested and confirmed to run with the Agrofood_co2_emission file, it can easily be applied to csv files of any shape or size. It currently does not ship with any relevant data. Data for analysis should be moved into the same folder as the python scripts.

## Installation

To install the package, please see one of the relevant releases. Download and unzip the file. Then, while inside of the unzipped folder, activate a mamba environment based on the dependencies of the project using 

'''bash
mamba env create -f environment.yml
mamba activate swe4s
'''

Additionally, move any relevant data into the same folder as the python scripts.

## Usage

With python-refresher as your working directory, you can run the following command to use the package:

'''bash
python print_fires.py -file "path/to/my/file" -q_col int_column_to_search \
    -q_val "str_value_to_search" -res_col int_column_to_find(optional)
'''

### Examples

'''bash
python3 print_fires.py -file "Agrofood_co2_emission.csv" -q_col 0 \
    -q_val "United States of America" -res_col 1
'''
returns good output.

'''bash
python3 print_fires.py -file "Agrofood_co2_emission.csv" -q_col "Area" \
    -q_val "United States of America" -res_col 1
'''
returns "Error: Query column ('Area') is not integer."

'''bash
python3 print_fires.py -file "environment.yml" -q_col 0 \
    -q_val "United States of America" -res_col 1
'''
returns "Expected a .csv file, got .yml"

## Summary of Changes:

Updated get_col to correctly handle errors and return only integer output.

Modified print_fires to use argparser.

Updated all code to match PEP 8.

Updated shell script to run examples of the code.

Added mamba environmental file.

Updated README to match changes.