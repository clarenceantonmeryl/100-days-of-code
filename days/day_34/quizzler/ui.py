from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.timer = None

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label_score = Label(text=f"Score: 0")
        self.label_score.config(background=THEME_COLOR, padx=20)
        self.label_score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Question",
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR,
            width=270
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.photo_image_true = PhotoImage(file="images/true.png")
        self.button_true = Button(image=self.photo_image_true)
        self.button_true.config(highlightbackground=THEME_COLOR, highlightthickness=0, command=self.left_button_action)
        self.button_true.grid(row=2, column=0)

        self.photo_image_false = PhotoImage(file="images/false.png")
        self.button_false = Button(image=self.photo_image_false)
        self.button_false.config(highlightbackground=THEME_COLOR, highlightthickness=0, command=self.right_button_action)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.timer = None

        self.button_true.config(state="normal")
        self.button_false.config(state="normal")

        self.canvas.config(bg="white")
        self.label_score.config(text=f"Score: {self.quiz_brain.score} / {self.quiz_brain.question_number}")
        if self.quiz_brain.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz_brain.next_question())
        else:
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")

    def left_button_action(self):
        if not self.timer:
            self.give_feedback(self.quiz_brain.check_answer("True"))

    def right_button_action(self):
        if not self.timer:
            self.give_feedback(self.quiz_brain.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.button_true.config(state="disabled")
        self.button_false.config(state="disabled")

        self.timer = self.window.after(1000, self.get_next_question)

