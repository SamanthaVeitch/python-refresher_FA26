import my_utils

country = 'United States of America'
county_column = 0
file_name = 'Agrofood_co2_emission.csv'
fires = my_utils.get_column(file_name, county_column, country)

print(fires)
