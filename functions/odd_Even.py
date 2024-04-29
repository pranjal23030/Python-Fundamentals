# def main():
#     num1 = eval(input("Number1: "))
#     num2 = eval(input("Number2: "))
#     sum_diff(num1, num2)
#
#
# def sum_diff(a, b):
#     sum = a + b
#     diff = a - b
#     print("The sum is:", sum)
#     print("The difference is:", diff)
#
#
# main()

number = eval(input("Enter a number to check whether it is even or odd: "))


def odd_even_finder(n):
    if n % 2 == 0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")


odd_even_finder(number)
