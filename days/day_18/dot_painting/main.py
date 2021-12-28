from turtle import Turtle, Screen

import random

turtle = Turtle()

screen = Screen()

screen_width = screen.window_width()
screen_height = screen.window_height()

print(screen_width)
print(screen_height)


turtle.shape("circle")
turtle.color("white")
#
# for _ in range(15):
#     turtle.pendown()
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#
# turtle.circle(3)

colours = [
    "green",
    "salmon",
    "peru",
    "cornflower blue",
    "medium slate blue",
    "sandy brown",
    "pale violet red",
    "royal blue",
    "light slate gray",
    "gold",
    "firebrick",
    "olive drab",
    "slate gray",
    "tomato",
]

# for side in range(3, 11):
#     angle = 360/side
#     turtle.color(random.choice(colours))
#     for _ in range(side):
#         turtle.forward(100)
#         turtle.left(angle)



# turtle.pensize(9)
turtle.speed(0)


def get_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

directions = [
    0,
    90,
    180,
    270
]

distances = [25, 50, 75, 100]
screen.colormode(255)

# for _ in range(50000):
#     # colour = (random.randint(0, 255)/255, random.randint(0, 255)/255, random.randint(0, 255)/255)
#     colour = get_color()
#     turtle.pencolor(get_color())
#     turtle.setheading(random.choice(directions))
#     turtle.forward(random.choice(distances))

# turn = 5
#
# for _ in range(int(360 / turn)):
#     turtle.pencolor(get_color())
#     turtle.circle(100)
#     turtle.left(turn)

turtle.hideturtle()

turtle.penup()

dot_diameter = 100

x = -((screen_width - dot_diameter)/2)
y = -((screen_height - dot_diameter)/2)
turtle.setposition(x, y)

for _ in range(int(screen_height/dot_diameter)):
    for _ in range(int(screen_width/dot_diameter)):
        turtle.pendown()
        turtle.dot(int(dot_diameter / 2), get_color())
        turtle.penup()
        turtle.forward(dot_diameter)
    y += dot_diameter
    turtle.setposition(x, y)

screen.exitonclick()