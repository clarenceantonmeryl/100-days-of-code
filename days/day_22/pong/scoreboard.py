from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-100, 280)
        self.write(str(self.left_score), align="center", font=('Courier', 80, 'normal'))
        self.goto(100, 280)
        self.write(str(self.right_score), align="center", font=('Courier', 80, 'normal'))

    def increase_left_point(self):
        self.left_score += 1
        self.display_score()

    def increase_right_point(self):
        self.right_score += 1
        self.display_score()
