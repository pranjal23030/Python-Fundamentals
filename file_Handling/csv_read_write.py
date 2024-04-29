import csv

# with open("student_marks.csv") as f:
#     csv_reader = csv.reader(f)
#
#     for line in csv_reader:
#         print(line)
#         # print(",".join(line))

with open("student_marks.csv", 'a', newline='') as f:
    csv_writer = csv.writer(f)

    data1 = ['Sandeep', 'M', '2/9/1985', 59, 95, 73, 42, 98, 72, 81, 56]
    csv_writer.writerow(data1)

    # datas = [['Anushkar', 'F', '12/8/1990', 78, 55, 86, 63, 54, 89, 75, 45],
    #          ['Hari', 'F', '2/9/1989', 58, 96, 78, 46, 96, 77, 83, 53],
    #          ['Ramu', 'M', '2/9/1985', 59, 95, 73, 42, 98, 72, 81, 56]]
    #
    # csv_writer.writerows(datas)
    print("Done with writing")
