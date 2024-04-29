something = 2  # This is a global variable


def hero(number):
    # global something
    something1 = number + 4
    print(something1)


hero(5)

print("The number iss :: ", something)
