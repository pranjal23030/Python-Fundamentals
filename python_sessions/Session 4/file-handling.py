
##"""
##    Demonstrates file handling in python    
##"""
##
##### Writing to a file
##fout = open('C:/Users/pradeep/Desktop/output.txt', 'w') # Writes to a file if file doesn't exists creates it.
##print(fout)
##
##line1 = "This here's the wattle, \n"
##fout.write(line1)
##line2 = "the emblem of our land. \n"
##fout.write(line2)
##
##
##print("Done with writing")
##fout.close()


##with open('output.txt', 'w') as f:
##    line1 = "This here's the wattle, \n"
##    f.write(line1)
##    
##    line2 = "the emblem of our land. \n"
##    f.write(line2)
##
##
##    print("Done with writing")


### Reading a file
fread = open('C:/Users/pradeep/Desktop/student.txt', 'r')

##for line in fread:
##    print(line.rstrip())
    
print(fread.name)
print(fread.mode)
##
txt = fread.read()
print(txt)

fread.close()

##
##
####print("\nDone reading complete file\n")
##txt1 = fread.read(30) # First 30 characters
##print(txt1)

######
##txt = fread.readlines()
##print(txt)


##for line in txt:
##    print(line, end="")

#### Removing new line character from every lines
##lines = [] 
##for line in fread:
##    # print(line, end="")
##    lines.append(line.rstrip())
##
##print(lines)
##
####print(lines)
########
##line = fread.readline()
##print(line)
##print(fread.readline())
##
##
##line1 = fread.readline()
##line2 = fread.readline()
##
##print(fread.readline())

##"-------------------------------"
##"""Strip method demo"""
##
##s = "   hello world  "
##print(s.lstrip()) 
##print(s.rstrip()) 
##print(s.strip())
##
##"-------------------------------"
##
### Appending to a file
##f = open('student.txt', 'a')
##line  = "Ashish 40 50 66 77"
##f.write('\n' + line)
##f.close()


##
##"-------------------------------"
### Read and write mode 'w+'
### Append and read mode 'a+'
