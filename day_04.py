import random
"""
player_state = input("Rock, paper or scissors? ").lower()

state = random.randint(0,2)

if state == 0:
    state = "rock"
elif state == 1:
    state = "paper"
else:
    state = "scissors"

if player_state == "rock" and state == "scissors"


state = random.randint(0,1)

if state == 0:
    print("Heads")
else:
    print("Tails")


names_input = input("Enter your names? ")

names_list = names_input.split(",")

# names = ["Clarence", "Anton", "Mohana"]

print(random.choice(names_list))

"""

row1 = ["◻️", "◻️", "◻️"]
row2 = ["◻️", "◻️", "◻️"]
row3 = ["◻️", "◻️", "◻️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
#position_list = position.split(" ")
position_list = [position[0], position[1]]
map[int(position_list[1])-1][int(position_list[0])-1] = "X"
print(f"{row1}\n{row2}\n{row3}")
