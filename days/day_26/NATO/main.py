import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

word = input("Enter a word: ").upper()

letters_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

nato_list = [letters_dict[letter] for letter in word if letter != " "]

print(nato_list)
