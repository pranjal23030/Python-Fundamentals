# # # Some methods in dictionary
# # # Key value pair
#
#
birthdays = {
    "ram": ["12-18-1987", "sum_of_Positive_Integers", 12],
    "sita": "7-6-2003",
    "john": "11-5-1992",
    "rita": "5-4-2001"
}
# print(birthdays)
# print(birthdays["ram"])
# del (birthdays["sita"])
# print(birthdays)

# print(birthdays.items())

# Merging dictionaries
# dict1 = {
#     "number": 1
# }
# dict2 = {
#     "number1": "one"
# }
# dict3 = dict1 | dict2
# print(dict3)

# print(type(birthdays))
# print()
# print(birthdays)
# print()
#
# # # Print all names

# for name in birthdays.keys():
#     print(name)
# print()
#
# # # # Print all values
# #
# for date_of_birth in birthdays.values():
#     print("Date of Birth:", date_of_birth)

# print(birthdays.items())
# print(birthdays["ram"][1])
# birthdays["sita"] = "Hello"
# print(birthdays)
# print()
# #
# Print both name and birthdays together

# for name, dob in birthdays.items():
#     print(name, ":", dob)
# print()

# my_dict = {'key1': 'geeks', 'key2': 'for'}
# print("Current Dict is:", my_dict)
#
# # Adding new key-value pairs
# my_dict['key3'] = 'Geeks'
# my_dict['key4'] = 'is'
# my_dict['key5'] = 'portal'
# my_dict['key6'] = 'Computer'
#
# print("Updated Dict is:", my_dict)

# #
# # # clear all items
# # # del birthdays
# # # birthdays.clear()
# #
# # # delete one item
# # birthdays.pop("ram")
# # print(birthdays)
# # print()
# #
# search in dictionary
user = input("Enter a user: ").lower()

while user not in birthdays:
    print("User not found")
    break

if user in birthdays:
    print(user, ":", birthdays[user])
