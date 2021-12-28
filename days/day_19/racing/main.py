from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race. Enter a colour: ")


attributes = [
    {"color": "red", "y": -75},
    {"color": "blue", "y": -45},
    {"color": "green", "y": -15},
    {"color": "indigo", "y": 15},
    {"color": "orange", "y": 45},
    {"color": "purple", "y": 75}
]

turtles = []

is_finished = False


def setup_turtle(attribute):
    turtle = Turtle(shape="turtle")
    turtle.color(attribute["color"])
    turtle.penup()
    turtle.goto(x=-230, y=attribute["y"])
    return turtle


for attribute in attributes:
    turtles.append(setup_turtle(attribute))


while not is_finished:

    for turtle in turtles:
        turtle.forward(randint(5, 15))
        if turtle.xcor() >= 225:
            is_finished = True

highest_x = 0
winner = ""

for turtle in turtles:
    if turtle.xcor() > highest_x:
        highest_x = turtle.xcor()
        winner = turtle.color()[0]

if bet == winner:
    print("You won the bet")
else:
    print(f"The winner is {winner}. You bet on {bet}.")

#
#
# def move_forward():
#     turtle.forward(10)
#
#
# def move_left():
#     turtle.left(10)
#
#
# def move_backward():
#     turtle.backward(10)
#
#
# def move_right():
#     turtle.right(10)
#
#
# def clear():
#     turtle.clear()
#     turtle.penup()
#     turtle.home()
#     turtle.pendown()
#
#
# screen.listen()
# screen.onkey(key="Right", fun=move_right)
# screen.onkey(key="Left", fun=move_left)
# screen.onkey(key="Up", fun=move_forward)
# screen.onkey(key="Down", fun=move_backward)
# screen.onkey(key="c", fun=clear)
#
screen.exitonclick()
