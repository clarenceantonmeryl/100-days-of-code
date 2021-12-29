from tkinter import *
import csv

# Constants
BACKGROUND_COLOR = "#B1DDC6"

# Variables
language = "French"
word = "trouve"

# CSV


def read_csv():
    with open(file="./data/french_words.csv", mode="r") as data_file:
        words = csv.reader(data_file)
        print(type(words))
        flash_dict = {item[0]: item[1] for item in words if item[0] != "French" and item[1] != "English"}
        return flash_dict


flash_dictionary = read_csv()

# UI
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
photo_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=photo_image)
language_title = canvas.create_text(400, 150, text=language, font=("Ariel", 40, "italic"), fill="black")
language_word = canvas.create_text(400, 263, text=word, font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

photo_image_wrong = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=photo_image_wrong, highlightbackground=BACKGROUND_COLOR)
button_wrong.grid(row=1, column=0)

photo_image_right = PhotoImage(file="./images/right.png")
button_right = Button(image=photo_image_right, highlightbackground=BACKGROUND_COLOR)
button_right.grid(row=1, column=1)

window.mainloop()
