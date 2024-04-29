import math


def main():
    print("This program find the real solutions of a quadratic equation")

    a = eval(input("Please enter a: "))
    b = eval(input("Please enter b: "))
    c = eval(input("Please enter c: "))

    disc_root = math.sqrt((b * b) - (4 * a * c))

    root1 = (-b + disc_root) / (2 * a)
    root2 = (-b - disc_root) / (2 * a)

    print("The solutions are: ", root1, root2)


main()
