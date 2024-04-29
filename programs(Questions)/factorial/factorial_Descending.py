def main():
    n = eval(input("Enter an integer: "))
    fact = 1
    for factor in range(n, 1, -1):
        fact = fact * factor

    print("The factorial of", n, "is", fact)


main()

# logicBehindThisCode

# fact = 1
# (5,1,-1)

# factor = 5
# fact= 1 * 5 = 5

# factor = 4
# fact = 5  * 4 = 20

# factor = 3
# fact = 20 * 3 = 60

# factor = 2
# fact = 60 * 2 = 120

# factor = 1
# fact = 120 * 1 = 120
