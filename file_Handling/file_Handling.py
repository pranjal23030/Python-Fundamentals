# File Handling in python

# Writing a file

# fout = open('C:\\Users\\Dell\\PycharmProjects\\pythonProject\\pythonFundamentals\\file_Handling\\output.txt', 'w')
# print(fout)
#
# line1 = "Hey!! \n"
# fout.write(line1)
# line2 = "How are you. \n"
# fout.write(line2)
# line3 = "Hope everything is well. \n"
# fout.write(line3)
#
# print("Done with writing")
# fout.close()

# New Style

# with open('output.txt', 'w') as f:
#     line1 = "Hello, Pranjal. \n"
#     f.write(line1)
#
#     line2 = "Another one. \n"
#     f.write(line2)

###########################################################################################################

# Reading a file

# fread = open('C:\\Users\\Dell\\PycharmProjects\\pythonProject\\pythonFundamentals\\file_Handling\\reading.txt', 'r')
#
# for line in fread:
#     print(line)
#
# fread.close()

# New Style

# with open('C:\\Users\\Dell\\PycharmProjects\\pythonProject\\pythonFundamentals\\file_Handling\\reading.txt',
#           'r') as fread:
#     # print(fread.name)
#     # print(fread.mode)
#     print()
#     # txt = fread.read(22)
#     txt1 = fread
#     print(fread.read())

################################################################################################################

# Strip method

# s = "          hello world              "
# print(s.lstrip())
# print(s.rstrip())
# print(s.strip())

#############################################################################################################

# Appending to a file

# f = open('C:\\Users\\Dell\\PycharmProjects\\pythonProject\\pythonFundamentals\\file_Handling\\kohli.txt', 'a')
# line = "I like kohli's bat."
# f.write('\n' + line)
# f.close()

# New style

with open('C:\\Users\\Dell\\PycharmProjects\\pythonProject\\pythonFundamentals\\file_Handling\\ipl.txt', 'a') as f:
    line = "What do you mean?"
    f.write("\n" + line)

