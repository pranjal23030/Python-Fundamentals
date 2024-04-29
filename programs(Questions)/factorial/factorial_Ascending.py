def main():
    print("Program to calculate the factorial of a number")
    n = eval(input("Enter a integer: "))
    total = 1
    for i in range(1, n + 1):
        total = total * i
    print(f"The factorial of {n} is: ", total)


main()

# logicBehindTheCode
# 1,5

# for i = 1
# total  = 1 * 1 = 1


# for i = 2
# total = 1 * 2 = 2

# for i = 3
# total = 2  * 3 = 6

# for i = 4
# total = 6 * 4 = 24


# for i = 5
# total = 24 * 5 = 120
