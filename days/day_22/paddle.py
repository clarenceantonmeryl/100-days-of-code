from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.speed(0)
        self.width = 5.0
        self.goto(x, y)
        self.penup()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_len=self.width, stretch_wid=1.0)

    def move_up(self):
        self.forward(40)

    def move_down(self):
        self.backward(40)
