import random
from day_07_hangman_art import stages, logo
from day_07_hangman_words import word_list
chosen_word = random.choice(word_list)

print(logo)
print("_ " * len(chosen_word))

game_over = False

life = len(stages)

final_output = []

for character in chosen_word:
    final_output.append("_")

while not game_over:

    guess_letter = input("\n\nGuess a letter: ").lower()

    index = 0

    lose_life = True

    for character in chosen_word:
        if guess_letter == character:
            final_output[index] = guess_letter
            lose_life = False

        index += 1

    final_string = ""

    for obj in final_output:
        final_string += obj

    print(final_string)

    if lose_life:
        life -= 1
        if life == 1:
            game_over = True
            lose = True

    print(stages[life-1])


    if "_" not in final_output and life > 0:
        game_over = True
        lose = False

if lose:
    print("\n\n\nYou lose.")
else:
    print("\n\n\nYou win.")

print(chosen_word)