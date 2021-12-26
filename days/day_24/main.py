with open(file="./Input/Names/invited_names.txt", mode="r") as names:
    name_list = names.readlines()

with open(file="./Input/Letters/starting_letter.txt", mode="r") as letter:
    template = letter.read()

for name in name_list:
    new_letter = template.replace("[name]", name.strip())
    with open(file=f"./Output/ReadyToSend/letter_for_{name.strip().lower()}.txt", mode="w") as letter:
        letter.write(new_letter)