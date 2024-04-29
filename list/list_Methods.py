numbers = [10, 22, 32, 64, 128, 256, 323, 44]
# print(len(numbers))
# print(numbers.index(32))
# numbers.insert(7, 7)
# print(numbers)
# print(numbers.reverse())
# print(sum(numbers))

# for num in numbers:
#     print(num, end=' ')

# Copying lists

# list1 = [1,2,3,4]
# list2 = []
# for each_item in list1:
#     list2.append(each_item)
# print(list2)
# list2 = [item for item in list1]
# list3 = [item ** 2 for item in list1]
# print(list2)
# print(list3)


# print(numbers[-1])
# print("List: ", numbers)
# print("Type:", type(numbers))
# print("Length", len(numbers))

#################################################

# List methods

# numbers.append(999)
# print(numbers)

################################################

# Lists are mutable

# print("Before replacing by 100", numbers)
# numbers[2] = 100
# print("After replacing by 100", numbers)

################################################

# Strings are immutable

# s = 'apple'
# s[2] = 'x'
# print(s)


################################################

# Empty lists
#
# l = []
# print(l)
# l.append("Pranjal")
# print(l)
# l.pop()
# print(l)

################################################

# POP methods
#
# print("Before popping out: ", numbers)
# print("POP: ", numbers.pop(0))
# print("After popping out: ", numbers)
# print("POP again: ", numbers.pop())
# print(numbers)
# print("POP ONCE AGAIN: ", numbers.pop(2))
# print(numbers)

##################################################

# List insertion and removal methods

# print(numbers)
# numbers.insert(2, 100)
# print("INSERT at 2: ",  numbers)
#
# print("Before removing: ", numbers)
# numbers.remove(100)
# print("After removing: ", numbers)

###################################################

# List addition

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = list1 + list2
# print(list3)

###################################################

# List append
#
# print("List1 before append: ", list1)
# list1.append(list2)
# print("List1 after append: ", list1)
# print(list1[0])
# print(list1[3])
# #
# print(list1[3][1])

#####################################################

# l = [1, 7, 9, [5, 2, [3, 8]], 6, 0]
# print(l[3][2][1])

######################################################

# List and Strings

# s = "apple-banana"
# print(type(s))
#
# l = list(s)
# print(type(l))
#
# print("S is: ", s)
# print("L is: ", l)
# print("Split list: ", s.split("-"))

# string = "pranjal Khatiwada"
# print(string)
# list_making = list(string)
# print(list_making)
# print(''.join(list_making))
# print("Split list: ", string.split())

######################################################

# String lists split

# s = "pranjal hari sabin"
# l = list(s)
# print(s.split())
# print(len(s.split()))
# print(l)

######################################################

# name = ["pranjal", "is", "my", "name"]
# print("Name: ", name, type(name))
#
# name_str = " ".join(name)
# print("String name: ", name_str, type(name_str))