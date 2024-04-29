
"""
    Demonstrates the use of break and continue
"""


"""-------------------------------------------"""
# User pressed quit
###while True:
##    user_typed = input("Enter your choice: ")
##    if user_typed == "Quit":
##        break        
##    else:
##        print("You typed ", user_typed)



        
"""-------------------------------------------"""

for i in range(1, 11):
    if i == 7:
        continue
    else:
        print(i**3, end=" ")






        
"""-------------------------------------------"""
# Find a random guessed number

##import random
##
###random.seed(100)
##guess = random.randint(1, 10)


##print(guess)
##
#guessed = 1
##for i in range(1, 4):
##    num = int(input("Guess a number between 1 to 10: "))
##    if num == guess:
##        print("Number found is {} in {} guesses" .format(num, guessed))
##        break
####    else:
####        guessed += 1
##
##
##print("Out of move")
##print("The correct number is:", guess)    
