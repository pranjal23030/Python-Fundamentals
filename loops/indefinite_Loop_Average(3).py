def main():
    sum1 = 0.0
    count = 0

    x_str = input("Enter a number (<Enter> to quit) >> ")
    while x_str != "":  # nothing/empty string not equals जति बेरसम्म इन्टर गर्दैन , तेत्ति बेरसम्म त् चल्नु पर्यो नि त
        # यदी इन्टर थिचे भनि चल्दैन.
        x = eval(x_str)
        sum1 = sum1 + x
        count = count + 1
        x_str = input("Enter a number (<Enter> to quit)>> ")
    print("\nThe average of the number is", sum1 / count)


main()
