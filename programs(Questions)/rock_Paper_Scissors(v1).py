print(" ROCK, PAPER AND SCISSORS \n")
player1 = input("Enter your name: ")
player2 = input("Enter your name: ")
print()

while True:
    choice1 = input(f"{player1}, Enter your choice: ")[0].lower()
    choice2 = input(f"{player2}, Enter your choice: ")[0].lower()

    if choice1 == choice2:
        print("It's a draw!!! ")

    elif choice1 == "r":
        if choice2 == "p":
            print(f"{player2}, You win")
        else:
            print(f"{player1}, You win")

    elif choice1 == "p":
        if choice2 == "s":
            print(f"{player2}, You win")
        else:
            print(f"{player1}, You win")

    elif choice1 == "s":
        if choice2 == "r":
            print(f"{player2}, You win")
        else:
            print(f"{player1}, You win")

    else:
        print("Invalid input")

    play_again = input("Do you want to play again (y/n): ")[0].lower()

    if play_again != "y":
        break

