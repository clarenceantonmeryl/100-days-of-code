import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v','w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

NUMBER_OF_LETTERS = random.randint(8, 10)
NUMBER_OF_SYMBOLS = random.randint(2, 4)
NUMBER_OF_NUMBERS = random.randint(2, 4)

FONT = ("Arial", 18, "normal")


def generate_password():

    letters = [random.choice(LETTERS) for _ in range(NUMBER_OF_LETTERS)]
    numbers = [random.choice(NUMBERS) for _ in range(NUMBER_OF_NUMBERS)]
    symbols = [random.choice(SYMBOLS) for _ in range(NUMBER_OF_SYMBOLS)]

    password = []

    password.extend(letters)
    password.extend(numbers)
    password.extend(symbols)

    random.shuffle(password)

    password_final = "".join(password)

    entry_password.delete(0, END)
    entry_password.insert(END, password_final)
    pyperclip.copy(password_final)


def get_data():

    email = entry_email.get()
    password = entry_password.get()
    website = entry_website.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) < 1:
        messagebox.showinfo(title="Invalid website", message="Enter a valid website")

    elif len(email) < 5:
        messagebox.showinfo(title="Invalid email", message="Enter a valid email")

    elif len(password) < 8:
        messagebox.showinfo(title="Invalid password", message="Enter a valid password")

    else:

        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:"
                    f"\nEmail: {email}"
                    f"\nPassword: {password}"
                    f"\nIs it ok to save these details?")
        if is_ok:
            data = None
            try:
                with open(file="data.json", mode="r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data
            finally:
                with open(file="data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)

            entry_website.delete(0, END)
            entry_password.delete(0, END)
            entry_website.focus()


def search():
    website = entry_website.get()

    try:
        with open(file="data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Website not found")
        entry_password.delete(0, END)
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']

            entry_email.delete(0, END)
            entry_password.delete(0, END)
            entry_email.insert(0, email)
            entry_password.insert(0, password)
        else:
            messagebox.showinfo(title="Error", message="Website not found")


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
entry_website = Entry(width=21)
entry_website.focus()
entry_website.grid(row=1, column=1, columnspan=1)

entry_email = Entry(width=39)
entry_email.insert(END, "a@b.com")
entry_email.grid(row=2, column=1, columnspan=2)

entry_password = Entry(width=21)
entry_password.grid(row=3, column=1, columnspan=1)


# Buttons
button_generate = Button(text="Generate Password", width=14, command=generate_password)
button_generate.grid(row=3, column=2, columnspan=1)

button_search = Button(text="Search", width=14, command=search)
button_search.grid(row=1, column=2)

button_add = Button(text="Add", width=36, command=get_data)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
