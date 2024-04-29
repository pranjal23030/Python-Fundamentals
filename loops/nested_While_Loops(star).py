# i = 1
# n = 5
# while i <= n:
#     j = 1
#     while j <= i:
#         print("*", end='')
#         j += 1  # j = j + 1
#     print("\n")
#     i += 1  # i = i + 1


i = 1
n = 5
while i <= n:
    j = 0
    while j <= n - i:
        print("*", end='')
        j += 1  # j = j + 1
    print("\n")
    i += 1  # i = i + 1
