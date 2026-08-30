from my_utils import get_column

country= 'United States of America'
country_column = 'Area'
fires_column = 'Forest fires'
file_name = 'Agrofood_co2_emission.csv'
fires = get_column(file_name, country_column, country, fires_column)

print(fires)
