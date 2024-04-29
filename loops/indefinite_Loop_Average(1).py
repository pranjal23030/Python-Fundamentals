def main():
    print("This programs find the average of the numbers using an indefinite loop")
    wanna_continue = "yes"
    sum = 0.0
    count = 0
    while wanna_continue[0] == 'y':
        number = eval(input("Enter a number: "))
        sum += number
        count += 1
        wanna_continue = input("Do you want to continue? ").lower()
    print("Average: ", sum / count)


main()
