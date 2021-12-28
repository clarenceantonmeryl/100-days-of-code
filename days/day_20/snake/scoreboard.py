from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 430)
        with open("../../../../data/highscore.txt") as highscore:
            self.high_score = int(highscore.read())
        self.score = 0

    def display_score(self):
        self.write(
            f"The score is " + str(self.score) + " High score: " + str(self.high_score),
            align="center",
            font=('Courier', 24, 'normal')
        )

    def reset_score_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="../../../../data/highscore.txt", mode="w") as highscore:
                highscore.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.display_score()
