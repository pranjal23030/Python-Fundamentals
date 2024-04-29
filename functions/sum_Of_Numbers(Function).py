def sum_finder(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print("The factorial of a given number is:", total)


number = eval(input('Enter a number of which you want to find the factorial of: '))
sum_finder(number)
