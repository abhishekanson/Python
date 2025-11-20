import csv

data = [
    {"name": "John", "age": 25, "city": "London"},
    {"name": "Sara", "age": 30, "city": "Paris"},
    {"name": "Mike", "age": 22, "city": "New York"}
]

filename = "output.csv"

with open(filename, "w", newline="") as csvfile:
    fieldnames = ["name", "age", "city"]
    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for row in data:
        writer.writerow(row)

print(f"Data written to {filename} successfully!")

with open(filename, "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        print(row)
