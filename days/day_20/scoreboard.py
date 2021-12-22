from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 430)

    def display_score(self, score):
        self.write(f"The score is " + str(score), align="center", font=('Courier', 24, 'normal'))
