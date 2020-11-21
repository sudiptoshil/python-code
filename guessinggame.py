
# Pyton Guessing Game
from random import randint

for i in range(1, 6):
    guessNumber = int(input("Enter Your Guess Number 1 to 5 :-"))
    randomNumber = randint(1, 5)
    if(guessNumber == randomNumber):
        print("You have won")
    else:
        print("you have Lost")
        print(f"Random Number Was :-{randomNumber}")
