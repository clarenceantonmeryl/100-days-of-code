from turtle import Turtle

FINISH_LINE = 460


class TurtleCrosser(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setheading(90)
        self.penup()
        self.color("white")
        self.shape("turtle")
        self.goto(0, -450)
        self.showturtle()

    def move(self):
        self.forward(10)

    def check_finish_line(self):
        if self.ycor() >= FINISH_LINE:
            self.goto(0, -450)
            return True
        else:
            return False
