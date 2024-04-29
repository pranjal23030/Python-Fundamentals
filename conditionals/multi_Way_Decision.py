_char = input("Enter character: ")


def main():
    print(f"You have entered {_char}")

    if _char[0].isalpha():
        print("Alphabet")
    elif _char[0].isdigit():
        print("Digit")
    else:
        print("Special character.")


main()
