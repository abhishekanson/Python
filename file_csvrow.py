import csv

filename = "data.csv"

with open(filename, "r", newline="") as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)
