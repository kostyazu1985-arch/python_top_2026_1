import csv

with open("data.csv") as r_file:
    file_reader = csv.reader(r_file, delimiter=';')

    for row in file_reader:
        print(row)