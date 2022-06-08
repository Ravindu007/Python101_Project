# TODO:
# get user input (rock, paper, scissor)
# generate random outcome
# compare it with the input
# if input == output => user wins
# else repeat untill user wins

import random

# initial values
userInput = input("Input Rock, Paper or Scissor: ")
randomOutput = random.choice(["Rock", "Paper", "Scissor"])

# if values dont match
while userInput != randomOutput:
    print(f"your guess: {userInput} , computer sets {randomOutput} TRY AGAIN")
    userInput = input("Input Rock, Paper or Scissor: ")
    randomOutput = random.choice(["Rock", "Paper", "Scissor"])

# if values match
if userInput == randomOutput:
    print(f"YOU WON! your guess: {userInput} , computer sets {randomOutput}")
