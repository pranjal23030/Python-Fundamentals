def main():
    wanna_continue = "yes"
    sum = 0
    while wanna_continue[0] == "y":
        number = eval(input("Enter the number: "))
        sum = sum + number
        wanna_continue = input("Do you want to continue: ").lower()
    print("Sum:",sum)


main()


# def main():
#     print("This program find the sum of the n positive integers")
#     total = 0
#     n = eval(input("How many numbers? : "))
#     for i in range(1, n + 1):
#         total += i
#     print("Sum:", total)
#
#
# main()
