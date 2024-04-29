# def pattern_generator(n, pattern):
#     for i in range(1, n + 1):
#         for j in range(0, i):
#             print(pattern, end='')
#         print("\n")
#
#
# pattern_generator(5, "%")


def pattern_generator(n, pattern):
    for i in range(n):
        for j in range(0, n-i):
            print(pattern, end='')
        print("\n")


pattern_generator(5, "#")
