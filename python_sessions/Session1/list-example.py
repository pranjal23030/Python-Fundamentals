
"""-------------------------------------"""
numbers = [10,22,32,44,53,63,78,82,91]
print(numbers[-1])
##
print("List: ", numbers)

print("Type: ", type(numbers))
print("Length: ", len(numbers))


"""-------------------------------------"""
### List methods
numbers.append(104)
print(numbers)
print(type(numbers))

print("Before replacing by 100: ", numbers)
numbers[2] = 100 # Lists are mutable
print("After replacing by 100: ", numbers)
print("Before popping out: ", numbers)
print("POP: ", numbers.pop())
print("After popping out: ", numbers)
print("POP again: ", numbers.pop())
print("List: ", numbers)
print("POP (0): ", numbers.pop(0))
print("List: ", numbers)
print("POP (5): ", numbers.pop(5))
print("List: ", numbers)
##
######print(numbers)
numbers.insert(2, 202)
print("INSERT at 2: ")
print("List: ", numbers)
print("Before removing:", numbers)
numbers.remove(100)
####
print("After removing: ", numbers)
numbers.remove(500)
print("After removing: ", numbers)
##
##"""-------------------------------------"""
### List addition and append
list1 = [1,2,3]
list2 = [4,5,6]

list3 = list1 + list2
print("List3: ", list3)

print("List1 before append: ", list1)
list1.append(list2)
print("List1 after append: ", list1)
print(list1[3])
print(type(list1[3][1]))

##"""-------------------------------------"""
### List and string
s = "apple"
print(type(s))

l = list(s) # Breaking a string into list of characters
print(type(l))
########
print("S is: " ,s)
print("L is: ", l)
print("Splitted list:", s.split())


s = "blowing-in the wind"
l = list(s)   # This result here is not appropriateprint(l)
print(l)
######
l = s.split(" ")   # Breaking a string to list of words
print(l)
print(len(l))
##
##l = ["rato", "tika", "nidhar", "ma"]
##print(l)
##print("L is of type: ", type(l))
##s = " ".join(l) # Joining the words with space in between
##print(s)
##print("s is of type: ", type(s))
##
