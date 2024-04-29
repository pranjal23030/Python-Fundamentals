outer = 5


def total():
    inner_in = 4
    # global outer
    # global outer
    outer = 7
    return inner_in + outer


inner = total()
print("Inner: ", inner)
print("Outer: ", outer)
