from tkinter import *
import csv
import random
from tkinter import messagebox

# Constants
BACKGROUND_COLOR = "#B1DDC6"

# timer
timer = None

# CSV


def read_csv():
    with open(file="./data/french_words_all.csv", mode="r") as data_file:
        words = csv.reader(data_file)
        print(type(words))
        flash_dict = {item[0]: item[1] for item in words if item[0] != "French" and item[1] != "English"}
        return flash_dict


flash_dictionary = read_csv()
flash_keys = list(flash_dictionary.keys())


new_key = None

def get_random_word():
    global flash_keys, new_key, timer
    canvas.itemconfig(language_title, text="French")
    if len(flash_keys) > 0:
        new_key = random.choice(flash_keys)
        canvas.itemconfig(language_word, text=new_key)
        return new_key
    else:
        if timer:
            window.after_cancel(timer)
        new_key = None
        if messagebox.askyesno(title="Reset", message="Do you want to reset"):
            flash_keys = list(flash_dictionary.keys())
            right_button_action()
        else:
            pass


def translate(key):
    if key:
        canvas.itemconfig(language_title, text="English", fill="#FFFFFF")
        canvas.itemconfig(canvas_image, image=photo_image_card_back)
        canvas.itemconfig(language_word, text=flash_dictionary[key], fill="#FFFFFF")


def next_card():
    global timer
    if timer:
        window.after_cancel(timer)

    canvas.itemconfig(canvas_image, image=photo_image_card_front)
    canvas.itemconfig(language_title, fill="#000000")
    canvas.itemconfig(language_word, fill="#000000")
    french_word = get_random_word()
    timer = window.after(3000, translate, french_word)


def right_button_action():
    global new_key
    if new_key:
        flash_keys.remove(new_key)
        print(new_key, "removed")
    next_card()


def wrong_button_action():
    next_card()


# UI
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
photo_image_card_front = PhotoImage(file="./images/card_front.png")
photo_image_card_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=photo_image_card_front)
language_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
language_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

photo_image_wrong = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=photo_image_wrong, highlightbackground=BACKGROUND_COLOR, command=wrong_button_action)
button_wrong.grid(row=1, column=0)

photo_image_right = PhotoImage(file="./images/right.png")
button_right = Button(image=photo_image_right, highlightbackground=BACKGROUND_COLOR, command=right_button_action)
button_right.grid(row=1, column=1)

next_card()

window.mainloop()
