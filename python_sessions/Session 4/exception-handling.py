"""
    Demonstrates exception handling
"""

"""----------------------------------------"""
##
##print(5 / 0)
##print("Big code down")

# Division by zero
num1 = 5
num2 = 0
result = 5/0
print(result)

# Exception handled for zero division
num1 = 5
num2 = 2
try:
    result = num1/num2
    print(result)
except FileNotFoundError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception:
    print("Trying to divide by zero.")
##

# print("I was trying to write many more functions below these")
    

"""----------------------------------------"""
# File not found

try:   
    f = open('someexample.txt')
    print(f.read())
    f.close()
    result = 5/0
    print(result)
except FileNotFoundError as e:
    print(e)
except ZeroDivisionError as e:
    print("Attempt to Divide by zero")
except Exception as e:
    print(e)
   

    

