from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Global Variables

repetition = 0

timer = None

# ---------------------------- TIMER RESET ------------------------------ #


def reset_timer():
    if timer:
        window.after_cancel(timer)

    global repetition
    repetition = 0
    label_title.config(text="Timer", fg=GREEN)
    label_tick.config(text="✔" * math.floor(repetition / 2))
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM -------------------------- #


def start_timer():

    global repetition
    repetition += 1

    if repetition == 9:
        reset_timer()
    else:
        if repetition % 8 == 0:
            count_down(LONG_BREAK_MIN * 60)
            label_title.config(text="LONG BREAK", fg=RED)
        elif repetition % 2 == 0:
            count_down(SHORT_BREAK_MIN * 60)
            label_title.config(text="SHORT BREAK", fg=PINK)
        else:
            count_down(WORK_MIN * 60)
            label_title.config(text="WORK", fg=GREEN)

        label_tick.config(text="✔" * math.floor(repetition / 2))

# ---------------------------- COUNTDOWN MECHANISM ---------------------- #

# ---------------------------- BUTTON ACTIONS --------------------------- #


def start_timer_action():
    reset_timer()
    start_timer()


def reset_timer_action():
    reset_timer()


def count_down(count):
    global repetition
    minutes = math.floor(count / 60)
    minutes_text = str(minutes)
    seconds = count % 60
    seconds_text = str(seconds)
    if minutes < 10:
        minutes_text = "0" + minutes_text

    if seconds < 10:
        seconds_text = "0" + seconds_text

    canvas.itemconfig(timer_text, text=f"{minutes_text}:{seconds_text}")
    if count > 0:
        global timer
        timer = window.after(1, count_down, count - 1)

    else:
        start_timer()

# ---------------------------- UI SETUP --------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=30, pady=30, bg=YELLOW)


# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo_image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 36, "bold"))
canvas.grid(row=1, column=1)

# Labels
label_title = Label(text="TIMER", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 36, "bold"))
label_title.grid(row=0, column=1)

label_tick = Label(text="✔" * math.floor(repetition/2), fg=GREEN, bg=YELLOW, highlightthickness=0)
label_tick.grid(row=3, column=1)

# Buttons
button_start = Button(text="START", command=start_timer_action, highlightbackground=YELLOW)
button_start.grid(row=2, column=0)

button_reset = Button(text="RESET", command=reset_timer_action, highlightbackground=YELLOW)
button_reset.grid(row=2, column=2)


window.mainloop()
