def main():
    total = 0.0
    count = 0
    x = eval(input('Enter a number <negative to quit>: '))
    while x >=0:
        total = total + x
        count = count + 1
        x = eval(input('Enter a number <positive to quit>: '))
    print("Average: ", total / count)


main()