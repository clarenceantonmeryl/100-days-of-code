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
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'exit' to exit :\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_shift(direction=direction, text=text, shift=shift)

    if direction == "exit":
        break



