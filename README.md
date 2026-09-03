# Changes 09.02.26 SCV

# my_utils.py
Implemented get_column function
    opens a csv file
    makes an array for results
    parses csv for matching query values in a specified colunm
    appends the value in column, index 1, of the row that matches
    returns array of mathcing results

# print_fires.py
Changed tests for my_utils
    imported my_utils
    corrected county_column value
    removed fires_column var
    assigned get_column call to fires var

# run.sh
Created file to run print_fires.py
    searches for print_fires.py script in same directory as run.sh
    downloads data used by py script from google drive
    runs py script
    asks if data file should be deleted