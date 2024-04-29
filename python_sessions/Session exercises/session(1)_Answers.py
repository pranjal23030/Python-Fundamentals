# Exercise 1:
# width//2 = 8 (type: int)
# width/2.0 = 8.5 (type: float)
# height/3 = 4.0 (type: float)
# 1 + 2 * 5 = 11 (type: int)
# delimiter * 5 = '.....' (type: str)

# Exercise 2:
# fahrenheit = float(input("Enter temperature in Fahrenheit: "))
# celsius = (fahrenheit - 32) * (5/9)
# print(f"{fahrenheit} Fahrenheit is {celsius:.2f} Celsius")

# Exercise 3:
# total_seconds = int(input("Enter time in seconds: "))
# minutes = total_seconds // 60
# seconds = total_seconds % 60
# print(f"{total_seconds} seconds is equal to {minutes} minutes and {seconds} seconds.")

# Exercise 4:
# my_list = [10, 20, 30, 40, 50, 60, 70]
# print("Length of the list:", len(my_list))
# print("First element:", my_list[0])
# print("Fourth element:", my_list[3])

# Exercise 5:

fruits = ['apple', 'banana', 'orange', 'kiwi', 'mango']

print("Original list:", fruits)
popped_fruit = fruits.pop(2)  # Removes and returns the element at index 2
print("Popped element:", popped_fruit)
print("List after pop():", fruits)

fruits.insert(2, 'grape')  # Inserts 'grape' at index 2
print("List after insert():", fruits)

fruits.remove('kiwi')  # Removes the first occurrence of 'kiwi'
print("List after remove():", fruits)
