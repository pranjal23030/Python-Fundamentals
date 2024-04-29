"""
    File: rps.py
    @Brief: Demonstrates the game of rock, paper and scissors
            This is a very simple version for educational purpose.
            Students are expected to modify and make it better.
            
            Game rules:
            Rock beats scissors,
            Scissors beat paper
            Paper beats rock
    
    @Author: Pradeep Aryal(Keep your name here afterwards)
    Python Version: 3.6.1 
"""
##
##import random
##
### Globals 
##player1 = input("\nEnter first player name: ")
##player2 = "Computer"
### player2 = input("Enter second player name: ")
##
##def play_game(choice1, choice2):
##    """Compares between choices of two players
##       and returns the winner"""
##
##    # global player1, player2
##
##    winner1 = player1 + " wins"
##    winner2 = player2 + " wins"
##    
##    if choice1 == choice2:
##        return "Tie"
##
##    elif choice1 == "rock":
##        if choice2 == "paper":
##            return winner2
##        else:
##            return winner1 
##
##    elif choice1 == "paper":
##        if choice2 == "scissors":
##            return winner2
##        else:
##            return winner1
##
##    elif choice1 == "scissors":
##        if choice2 == "rock":
##            return winner2
##        else:
##            return winner1
##    else:
##        return("Invalid input!!! Please choose among rock, paper or scissors ") # Invalid choice
##        
##def main():
##    while True:
##        player1_choice = input(f"Enter your choice {player1}: ").lower()
##        # player2_choice = input(f"Enter your choice {player2}: ").lower()
##        player2_choice = random.choice(['rock', 'paper', 'scissors'])
##        print(f"Computer chooses {player2_choice}")
##        
##
##        result = play_game(player1_choice, player2_choice)
##        print("\n" + result)
##
##   
##        play_again = input("\nWould you like to play again yes/no: ").lower()
##        if play_again[0] == "y":
##            continue
##        else:
##            break
##
##
##if __name__ == "__main__":
##    print("\nPlease choose among rock, paper or scissors\n")
##    
##    print("""Game rules:\n\
##            Rock beats scissors \n\
##            Scissors beat paper \n\
##            Paper beats rock\n""")
##    
##    main()
##
##    
##    
