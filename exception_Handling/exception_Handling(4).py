import math


def main():
    print("This program finds the solutions of a quadratic equation")

    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        print("\nThe equation has no real roots.")

    elif discriminant == 0:
        root = -b / (2 * a)
        print("\nThere is a double root at", root)

    else:
        disc_root = math.sqrt(discriminant)
        root1 = (-b + disc_root) / (2 * a)
        root2 = (-b - disc_root) / (2 * a)
        print("\nThe solutions are:", root1, root2)


main()
