import math


def main():
    print("This program finds the real solutions to a quadratic\n")

    try:
        a, b, c = eval(input("Please enter the coefficients (a,b,c): "))
        disc_root = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + disc_root) / (2 / a)
        root2 = (-b - disc_root) / (2 / a)
        print("\n The solutions are: ", root1, root2)

    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("No real roots")
        else:
            print("You didn't give me the right number of coefficients.")

    except NameError:
        print("\n You didn't enter three numbers.")

    except TypeError:
        print("\n Your inputs were not all numbers. ")

    except SyntaxError:
        print("\nYour input was not in the correct form. ")

    except:
        print("\n Something went wrong, sorry!")


main()
