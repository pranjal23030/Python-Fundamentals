import csv

with open('students.csv', 'a', newline='') as file:
    content = csv.writer(file)

    data1 = ["Sangita", 12, 14]
    content.writerow(data1)

    print("Done with writing")
