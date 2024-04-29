def main():
    print("This program calculates the future value of a 10 year investment.")

    principal = eval(input("Enter the initial principal: "))
    i = eval(input("Enter the annual interest rate: "))

    for _ in range(10):
        principal = principal * (1 + i)

    print('The value in 10 years is: ', principal)


main()

