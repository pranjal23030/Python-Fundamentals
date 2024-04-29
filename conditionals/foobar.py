for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(str(i) + ": Foobar")
    elif i % 3 == 0:
        print(str(i) + ": Foo")
    elif i % 5 == 0:
        print(str(i) + ": Bar")
    else:
        print(i)