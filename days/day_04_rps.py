import random

choices = ["Rock", "Paper", "Scissors"]

playerChoice = int(input("What do you choose? Type 1 for Rock, 2 for paper or 3 for scissors\n"))-1

if 4 > playerChoice > -1:

    computerChoice = int(random.randint(0,2))

    print(f"You chose: {choices[playerChoice]} \nThe computer chose: {choices[computerChoice]}")

    if playerChoice == computerChoice:
        result = "Draw"

    elif playerChoice - computerChoice == -1 or playerChoice - computerChoice == 2:
        result = "Lose"

    else:
        result = "Win"

    print(f"You {result}")

else:
    print("You typed an invalid number")