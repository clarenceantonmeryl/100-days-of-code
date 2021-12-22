from turtle import Turtle
from random import randint

DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


def get_color():
    return 1, randint(0, 255)/255, randint(0, 255)/255


def setup_snake_body(x, y):
    turtle = Turtle(shape="square")
    turtle.color(get_color())
    turtle.penup()
    turtle.speed(0)
    turtle.goto(x, y)
    return turtle


class Snake:

    def __init__(self):
        self.length = 3
        self.angle = RIGHT
        self.turtles = []
        self.setup()
        self.head = self.turtles[0]

    def setup(self):
        x = 0
        y = 0
        for _ in range(self.length):
            self.turtles.append(setup_snake_body(x, y))
            x -= DISTANCE

    def add_length(self):
        self.turtles.append(setup_snake_body(self.turtles[-1].xcor(), self.turtles[-1].ycor()))

    def check_body_collision(self, is_game_on):
        is_game_over = False

        for turtle in self.turtles[2:]:
            if self.head.distance(turtle) < 20:
                is_game_on = False
                is_game_over = True
                break
        return is_game_on, is_game_over

    def move(self):
        for index in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[index - 1].xcor()
            new_y = self.turtles[index - 1].ycor()
            self.turtles[index].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def change_direction(self):
        self.head.setheading(self.angle)

    def turn_right(self):
        if self.angle != LEFT:
            self.angle = RIGHT
            self.change_direction()

    def turn_left(self):
        if self.angle != RIGHT:
            self.angle = LEFT
            self.change_direction()

    def turn_up(self):
        if self.angle != DOWN:
            self.angle = UP
            self.change_direction()

    def turn_down(self):
        if self.angle != UP:
            self.angle = DOWN
            self.change_direction()
