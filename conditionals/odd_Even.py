# def main():
#     n = eval(input("Enter a number: "))
#
#     if n % 2 == 0:
#         print(f"The entered number {n} is even.")
#     else:
#         print("Odd")
#
#
# main()


def is_even(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


number = eval(input("Enter a number: "))
is_even(number)
