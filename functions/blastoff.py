def countdown(n):
    if n <= 0:
        print("Blastoff")
    else:
        countdown(n - 1)
        print(n)


countdown(3)
