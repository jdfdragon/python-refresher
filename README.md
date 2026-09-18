# python-refresher

This file contains utilities and functions to enable the easy reading and searching inside of csv files. While designed to run with the Agrofood_co2_emission file, it can easily be applied to files of any shape or size. It currently does not ship with any relevant data. Data for analysis should be moved into the same folder as the python scripts.

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
./run.sh "path/to/my/file" int_column_to_search "str_value_to_search" int_column_to_find(optional)
'''

### Examples

'''bash
./run.sh "Agrofood_co2_emission.csv" 0 "United States of America" 1
'''
returns good output.

'''bash
./run.sh "Agrofood_co2_emission.csv" "Area" "United States of America" 1
'''
returns "Error: Query column ('Area') is not integer."

'''bash
./run.sh "example.pdf" 0 "United States of America" 1
'''
returns "Expected a .csv file, got .pdf"

## Summary of Changes:

Added get_column as a callable function in my_utils.py.

Modified print_fires to correctly use the get_column function.


Added a shell script run.sh to automatically run print_fires.py from the terminal
    NOTE: the shell script was not automatically given execute permission when created. Please run chmod 744 run.sh in order to allow the script to be run from the terminal.