import math


def main():
    print("This program finds the real solutions to a quadratic\n")

    try:
        a, b, c = eval(input("Please enter the coefficients (a,b,c): "))
        disc_root = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + disc_root) / (2 / a)
        root2 = (-b - disc_root) / (2 / a)
        print("\n The solutions are: ", root1, root2)

    except ValueError as e:
        print(e)

    except ZeroDivisionError as e:
        print(e)


main()
