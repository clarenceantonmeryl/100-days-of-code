alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def character_shifter(shift, character):
    index = alphabet.index(character) + shift
    if index > 25:
        index -= 26
    return alphabet[index]


def caesar_shift(direction, text, shift):
    if direction == "decode":
        shift = shift * -1

    output = ""

    for char in text:
        if char.isalpha():
            output += character_shifter(shift=shift, character=char)
        else:
            output += char

    print(output)


while True:
    direction_input = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'exit' to exit :\n")
    text_input = input("Type your message:\n").lower()
    shift_input = int(input("Type the shift number:\n"))

    if direction_input == "exit":
        break
    else:
        caesar_shift(direction=direction_input, text=text_input, shift=shift_input)




