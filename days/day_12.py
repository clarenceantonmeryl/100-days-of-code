import random
number = random.randint(0, 100)

level = input("What difficulty do you want. Easy or hard (e or h): ").lower()

attempts = 10

if level == "h":
    attempts = 5

print(f"You have {attempts} attempts left.")

while attempts > 0:

    guess = int(input("Guess a number between 1 and 100: "))

    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("Your answer is correct")
        break

    attempts -= 1

    print(f"You have {attempts} attempts left.")

    if attempts == 0:
        print("You lose")
        print(f"The answer was {number}")
