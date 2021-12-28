#Password Generator Project
import random
from tkinter import *

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

NUMBER_OF_LETTERS = 5
NUMBER_OF_SYMBOLS = 5
NUMBER_OF_NUMBERS = 5

FONT = ("Arial", 21, "normal")

# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))


def generate_password():

    password = []

    for _ in range(1, NUMBER_OF_LETTERS + 1):
        password.append(random.choice(LETTERS))

    for _ in range(1, NUMBER_OF_NUMBERS + 1):
        password.append(random.choice(NUMBERS))

    for _ in range(1, NUMBER_OF_SYMBOLS + 1):
        password.append(random.choice(SYMBOLS))

    random.shuffle(password)

    password_final = ""

    for obj in password:
        password_final += obj

    return password_final


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
photo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_image)
canvas.grid(row=0, column=1)

# Labels
label_website = Label(text="Website:", highlightthickness=0, font=FONT)
label_website.grid(row=1, column=0)

label_email = Label(text="Email/Username:", highlightthickness=0, font=FONT)
label_email.grid(row=2, column=0)

label_password = Label(text="Password:", highlightthickness=0, font=FONT)
label_password.grid(row=3, column=0)

# Entries
entry_website = Entry()
entry_website.grid(row=1, column=1, columnspan=2)

entry_email = Entry()
entry_email.grid(row=2, column=1, columnspan=2)

entry_password = Entry()
entry_password.grid(row=3, column=1, columnspan=1)


# Buttons
button_generate = Button(text="Generate Password")
button_generate.grid(row=3, column=2, columnspan=1)

button_reset = Button(text="Add")
button_reset.grid(row=4, column=1, columnspan=2)

window.mainloop()


