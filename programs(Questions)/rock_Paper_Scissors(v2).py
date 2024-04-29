import random

# Global Variables
player1 = input("\n Enter first player name: ")
player2 = "Computer"


def play_game(player1, player2):
    player1_choice = input(f"Enter your choice {player1}: ").lower()
    player2_choice = random.choice(['rock', 'scissors', 'paper'])

    winner1 = player1 + " wins"
    winner2 = player2 + " wins"

    if player1_choice == player2_choice:
        return "Tie"
    elif player1_choice == "rock":
        if player2_choice == "paper":
            return winner2
        else:
            return winner1
    elif player1_choice == "paper":
        if player2_choice == "scissors":
            return winner2
        else:
            return winner1
    elif player1_choice == "scissors":
        if player2_choice == "rock":
            return winner1
        else:
            return winner2
    else:
        return "Invalid input!! Please choose among rock, paper, and scissors"


def star():
    while True:
        result = play_game(player1, player2)
        print("\n" + result)

        play_again = input("\n Would you like to play again? (yes/no): ").lower()
        if play_again.startswith('y'):
            continue
        else:
            break
            
            
star()
