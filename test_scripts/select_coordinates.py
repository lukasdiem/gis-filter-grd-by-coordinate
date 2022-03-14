import csv

filename = "gis_data.csv"
with open(filename, 'r') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)