##l = [[10,21,32,41],
##     [5,65],
##     [7,84,90]]
##
#### Displaying elements of 2d list
##for i in range(len(l)):
##    for j in range(len(l[i])):
##        print(l[i][j], end=" ")
##    print()
####
####
####
###### Alternate style of displaying
##for i in l:
##    for j in i:
##        print(j, end=" ")
##    print()

    

## Sum of elements in 2d list
##sum_ = 0
##for i in l:
##    for j in i:
##        sum_ += j
##
##print(sum_)

## Input elements

n = int(input("Enter number of rows: ")) 
a = []
for i in range(n):
    row = input().split()

    for j in range(len(row)):
        row[j] = int(row[j])
    a.append(row)

    
print(a)

"""
1 0 0 0
2 1 0 0
2 2 1 0
2 2 2 1
"""

##l = []
##n = 4
##for i in range(n):
##    l.append([0]*4)
##
##print(l)
        

n = 4

l = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            l[i][j] = 1
        elif i > j:
            l[i][j] = 2
        else:
            l[i][j] = 0


##for elem in l:
##    print(elem)
    
print(" ".join([str(i) for i in elem]))
        

"""
0  0  0  0  0  0
0  1  2  3  4  5
0  2  4  6  8 10
0  3  6  9 12 15
0  4  8 12 16 20
"""
##r, c  = 5, 6
##
##l = [[0] * c for i in range(r)]
##
##for i in range(r):
##    for j in range(c):
##        l[i][j] = i*j
##
##for elem in l:
##    print(" ".join([str(i) for i in elem]))
##
