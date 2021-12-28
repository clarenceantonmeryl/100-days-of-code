from turtle import Turtle
import random


def get_color():
    return 1, random.randint(0, 255)/255, random.randint(0, 255)/255


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.hideturtle()
        self.shapesize(stretch_len=2.0)
        self.color(get_color())
        self.setheading(180)
        self.goto(570, random.randint(-400, 430))
        self.showturtle()
        self.is_super_car = False

    def move(self):
        if self.is_super_car:
            self.forward(random.randint(40, 60))
        else:
            self.forward(random.randint(5, 15))
