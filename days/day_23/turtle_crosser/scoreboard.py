from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-500, 450)
        self.score = 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Level: {str(self.score)}", align="center", font=('Courier', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.display_score()

    def display_game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over. Your score was: {str(self.score)}", align="center", font=('Courier', 24, 'normal'))