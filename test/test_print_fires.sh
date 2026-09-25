test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run basic_test python3 print_fires.py -file "test/test_file.csv" -q_col 0 \
    -q_val "Afghanistan" -res_col 1
assert_in_stdout "[1990, 1991, 1992, 1993, 1994]"
assert_exit_code 0

run default_test python3 print_fires.py -file "test/test_file.csv" -q_col 0 \
    -q_val "Afghanistan" 
assert_in_stdout "[1990, 1991, 1992, 1993, 1994]"
assert_exit_code 0

run test_space python3 print_fires.py -file "test/test_file.csv" -q_col 0 \
    -q_val "American Samoa" -res_col 1
assert_in_stdout "[1990, 1991, 1992, 1993]"
assert_exit_code 0

run test_noFile python3 print_fires.py -file "test_file.csv" -q_col 0 \
    -q_val "American Samoa" -res_col 1
assert_in_stdout "Error: File 'test_file.csv' not found in current directory."
assert_exit_code 1

run test_noCSV python3 print_fires.py -file "test/test_my_utils.py" -q_col 0 \
    -q_val "American Samoa" -res_col 1
assert_in_stdout "Expected a .csv file, got .py"
assert_exit_code 1

run test_noQInt python3 print_fires.py -file "test/test_file.csv" -q_col 'a' \
    -q_val "American Samoa" -res_col 1
assert_in_stdout "Error: Query column ('a') is not integer."
assert_exit_code 1

run test_QLong python3 print_fires.py -file "test/test_file.csv" -q_col 105 \
    -q_val "American Samoa" -res_col 1
assert_in_stdout "Error: Query column ('105') out of bounds."
assert_exit_code 1

run test_noRInt python3 print_fires.py -file "test/test_file.csv" -q_col 0 \
    -q_val "American Samoa" -res_col 'a'
assert_in_stdout "Error: Result column ('a') is not integer."
assert_exit_code 1

run test_RLong python3 print_fires.py -file "test/test_file.csv" -q_col 0 \
    -q_val "American Samoa" -res_col 105
assert_in_stdout "Error: Result column ('105') out of bounds."

run test_Null python3 print_fires.py -file "test/test_file.csv" -q_col 0 \
    -q_val "Soviet Union" -res_col 1
assert_in_stdout "No results found."
assert_in_stdout '[]'
assert_exit_code 0

run test_NoInt python3 print_fires.py -file "test/test_file.csv" -q_col 0 \
    -q_val "test_val" -res_col 1
assert_in_stdout "Data must be numberic. Found "STRING"."
assert_exit_code 1

run test_mean python3 print_fires.py -file "test/test_file.csv" -q_col 0 \
    -q_val "Afghanistan" -res_col 1 -stat 'mean'
assert_in_stdout "1992"
assert_exit_code 0

run test_median python3 print_fires.py -file "test/test_file.csv" -q_col 0 \
    -q_val "Afghanistan" -res_col 7 -stat 'median'
assert_in_stdout "11"
assert_exit_code 0

run test_sd python3 print_fires.py -file "test/test_file.csv" -q_col 0 \
    -q_val "Afghanistan" -res_col 3 -stat 'sd'
assert_in_stdout "0"
assert_exit_code 0

run test_sd python3 print_fires.py -file "test/test_file.csv" -q_col 0 \
    -q_val "Afghanistan" -res_col 3 -stat 'PERFECT MODEL'
assert_in_stdout "Error: Invalid statistic requested 'PERFECT MODEL'."
assert_exit_code 1

