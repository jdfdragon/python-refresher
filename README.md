# python-refresher

## Summary of Changes:

Added get_column as a callable function in my_utils.py.

Modified print_fires to correctly use the get_column function.

Added functionality to get_column so that it accepts query column and result column input in the form of strings.

Modified get_column to ensure backwards compatibility with integer inputs for column indicies.

Added a shell script run.sh to automatically run print_fires.py from the terminal
    NOTE: the shell script was not automatically given execute permission when created. Please run chmod 744 run.sh in order to allow the script to be run from the terminal.