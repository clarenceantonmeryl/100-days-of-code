from turtle import Turtle


STARTING_HEADINGS = [10]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.setheading(220)
        self.displacement = 5
        self.x_move = self.displacement
        self.y_move = self.displacement

    def replay(self):
        self.hideturtle()
        self.goto(0, 0)
        self.x_move *= -1
        self.showturtle()

    def move(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.horizontal_bounce()
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def vertical_bounce(self):
        self.x_move *= -1

    def horizontal_bounce(self):
        self.y_move *= -1
