# Without recursion

# def factorial(n):
#     total = 1
#     for i in range(1, n + 1):
#         total = total * i
#     return total
#
#
# print(factorial(5))

# With recursion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)
print(result)
