
"""------------------------------------"""
# Some dictionaries

#


expenses_item = ['Waiwai', 'Lays', 'Cocacola', 'Helmet', 'Shampoo', 'Cylinder', 'Dove']
expenses = [20, 45, 210, 2500, 340, 1500, 320.50]

kharcha = {'Waiwai': 20, 'Lays': 45, 'Coke': 210, 'Helmet': 2500}
# print(kharcha['Coke'])
for key,val in kharcha.items():
    print(key, val)



student = {} # Creates an empty dictionary

##print(student)
##print(type(student))

##student = dict() # Creates an empty dictionary
##print(student)
##print(type(student))
##
##student = {"name": "Harry Potter", "age": 22}
####print(student["location"])
##
####
##print(student["name"])
##print(student["age"])
##student["age"] = 18
##print(student["age"])
####
##student["class"] = 12
##print(student)
######
##student["address"] = "Manchester"
##print(student)

"""------------------------------------"""

# Some sets
##set_a = {9, 2, 3, 4, 5, 6, 7}
##set_b = {2, 2, 2, 4}
##
####print("SET A: ", set_a)
####print("SET B: ", set_b)
########
#####print(set_a[0])     # Doesn't support indexing
########
##set_b.add(6)
##print("SET B after addition of 6 ", set_b)
########
##set_b.remove(2)
##print("SET B after removal of 2 ", set_b) 
####
##print("Intersection: ", set_a.intersection(set_b))
##print("Union: ", set_a.union(set_b))
######
####### bitwise operator & | -
####"""
####And operation:
####inputs  output
####0 0     0
####0 1     0
####1 0     0
####1 1     1
##
####Or opeartion:
####inputs output
####0 0     0
####0 1     1
####1 0     1   
####1 1     1            
####"""
##print("Set A intesection set b ", set_a & set_b)
##print("Set A minus set b ", set_a - set_b)
##print("Set A union set b ", set_a | set_b)
##
