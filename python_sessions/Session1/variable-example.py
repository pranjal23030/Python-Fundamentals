
"""-------------------------------------------------"""
##print("Hello World")  # First program # Alt +3 for comment
##                     # Alt + 4 for uncomment
##msg = "Hello World"
######
####print(msg)
##
####"""-------------------------------------------------"""
### Knowing the type of the variable
##print("Msg is of type: ", type(msg))
##print("1 is of type: ", type(1))
##print("-1 is of type: ", type(-1))
##print("4.2 is of type: ", type(4.2))

##"""-------------------------------------------------"""
### Finding the volume of a sphere
PI = 3.1416 # This is for constant value
radius = 0.8

"""Note: Execution follows pedmas rule which
   is Parenthesis, Exponential, Division,
   Multiplication, Addition and Subtraction"""


volume_sphere = (4/3)*PI*(radius**3)
print("Volume is: ", volume_sphere)
#print("Volume is: {}".format(volume_sphere))

#### Examples with .format  
##
##"""-------------------------------------------------"""
### Use of + operator for number and string
##print("Adding 1 and 2: ",1 + 2)
##first_name = "Bob"
##last_name = "Dylan"
##full_name = first_name + " " + last_name
##print("Adding Bob and Dylan:",full_name) # Use comma if there is only one variable
####
#### Use these if there are multiple variables
####print("Adding Bob and Dylan: {}".format(full_name))
####print(f"Adding Bob and Dylan: {full_name}")
####
#### C style printing old style
####print("Adding Bob and Dylan: %s"%(full_name))
##
### print(1 + 2 + 3)
##
##"""-------------------------------------------------"""
### Printing person name along with dob
### c++ std::cin
### c scanf
##
#### raw_input same as input, was used in Python 2. version 
##
##first_name = input("Enter your first name: ")
##last_name = input("Enter your last name: ")
##
##print("Enter your date of birth: ")
##
##month = input("Month? ")
##day = input("Day? ")
##year = input("Year? ")
##
####print(first_name + " " + last_name + " "
####      + "was born on " + month + " " + day + " " + year)
##
##print("{} {}  was born on {} {} {}".format(first_name, last_name, month, day, year))
##
##print(f"{first_name} {last_name}  was born on {month} {day} {year}")
##
####"""Note: + operator concatenetes two string along with
####   addition of numbers"""
##
##
####
####num1 = float(input("Enter first number: "))
####num2 = float(input("Enter second number: "))
####print(num1 + num2)
##
##
##
##

