import math


def main():
    print("This program finds the real solutions to a quadratic equation")

    a, b, c = eval(input("Please enter the coefficients: (a,b,c):  "))
    discrim = b * b - 4 * a * c

    if discrim < 0:
        print("\nThe equation has no real roots. ")

    else:
        disc_root = math.sqrt(discrim)
        root1 = (-b + disc_root) / (2 * a)
        root2 = (-b - disc_root) / (2 * a)
        print("\n The solutions are: ", root1, root2)


main()
