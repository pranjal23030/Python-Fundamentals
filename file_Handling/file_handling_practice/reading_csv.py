import csv

with open('students.csv', 'r') as file:
    content = csv.reader(file)

    for line in content:
        print(" ".join(line))