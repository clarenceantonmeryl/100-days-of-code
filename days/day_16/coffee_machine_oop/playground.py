from turtle import Turtle, Screen

turtle = Turtle()
print(turtle)

screen = Screen()

print(screen.canvheight)
turtle.shape("turtle")
turtle.color("DarkOliveGreen", "yellow")
turtle.begin_fill()
for i in range(210):
    turtle.forward(200)
    turtle.backward(200)
    turtle.circle(5.2)
    turtle.right(45)
    turtle.forward(50)
    turtle.left(79)
    turtle.forward(23)
    turtle.circle(4.3)
turtle.end_fill()
screen.exitonclick()


# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()