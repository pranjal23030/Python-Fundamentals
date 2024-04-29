num1 = eval(input("Enter Number 1: "))
num2 = eval(input("Enter Number 2: "))

try:
    result = num1 / num2
    print(result)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)