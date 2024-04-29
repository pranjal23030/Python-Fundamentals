def main():
    a = eval(input("Please enter number 1: "))
    b = eval(input("Please enter number 2: "))

    try:
        print(a / b)

    except ZeroDivisionError:
        print("The second input shouldn't be zero.")


main()
