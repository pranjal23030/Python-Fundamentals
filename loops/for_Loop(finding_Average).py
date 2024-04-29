def main():
    print("This program find the average of the given number by using for loop")
    sum = 0.0
    n = eval(input("How many numbers: "))
    for i in range(n):
        num_count = eval(input("Number: "))
        sum += num_count
    print("Average", sum / n)


main()
