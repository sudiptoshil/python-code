
# Pyton Guessing Game
# from random import randint

# for i in range(1, 6):
#     guessNumber = int(input("Enter Your Guess Number 1 to 5 :-"))
#     randomNumber = randint(1, 5)
#     if(guessNumber == randomNumber):
#         print("You have won")
#     else:
#         print("you have Lost")
#         print(f"Random Number Was :-{randomNumber}")


# Python Calculator...

firstNumber = float(input("Enter Your First Number:-"))
secondNumber = float(input("Enter Your Second Number:-"))

print("Press: Addition = a,Subtraction = s, Multiplication = m,Division=d")

submit = str(input("Submit Your Key:-"))
addition = firstNumber + secondNumber
subtraction = firstNumber - secondNumber
multiplication = firstNumber * secondNumber
division = firstNumber / secondNumber

if(submit == "a"):
    print(f"Addition is:- {addition}")
elif(submit == "s"):
    print(f"Subtraction is:- {subtraction}")
elif(submit == "m"):
    print(f"Multiplication is:- {multiplication}")
elif(submit == "d"):
    print(f"Division is:- {division}")
else:
    print(f"You have entered a wrong key value:- {submit}")
