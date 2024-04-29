# for i in range(1, 6):
#     for j in range(0, i):
#         print("*", end="")
#     print()

# for i in range(1, 6):
#     for j in range(0, 6 - i):
#         print("*", end="")
#     print()


number = int(input("Number: "))
pattern = input("Pattern: ")


def pattern_generator(n, p):
    for i in range(1, n + 1):
        for j in range(0, i):
            print(f"{pattern}", end="")
        print()


pattern_generator(number, pattern)
