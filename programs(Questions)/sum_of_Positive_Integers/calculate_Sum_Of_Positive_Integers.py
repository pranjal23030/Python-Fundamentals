def main():
    print("Program to calculate the sum of first n positive numbers")
    n = eval(input("Enter a integer:"))
    total = 0
    for i in range(1, n + 1):
        total = total + i
    print("Sum of first", n, "positive integers is", total, "!")


main()

print("Calculation done")

# Logic behind this code

# 1,5

# for i = 1
# total = 0 + 1 = 1

# for i = 2
# total = 1 + 2 = 3

# for i = 3
# total = 3 + 3 = 6

# for i = 4
# total = 6 + 4 = 10

# for i = 5
# total = 10 + 5 = 15
