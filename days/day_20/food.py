from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("yellow")
        self.speed(0)
        self.go_to_position()

    def go_to_position(self):
        self.goto(randint(-400, 400), randint(-400, 400))

