import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")


letters_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}


def get_nato():
    word = input("Enter a word: ").upper()
    try:
        nato_list = [letters_dict[letter] for letter in word if letter != " "]
    except KeyError:
        print("Enter a valid word.")
        get_nato()
    else:
        print(" ".join(nato_list))


get_nato()