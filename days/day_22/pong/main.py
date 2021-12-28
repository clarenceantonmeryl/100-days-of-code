from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(1000, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()

paddle_left = Paddle(-500, 0)

paddle_right = Paddle(500, 0)

ball = Ball()

scoreboard = Scoreboard()


is_game_on = True


def detect_paddle_collision():
    if ball.xcor() > 480 and ball.distance(paddle_right) < 50:
        ball.vertical_bounce()
    elif ball.xcor() < -480 and ball.distance(paddle_left) < 50:
        ball.vertical_bounce()


def game():
    global is_game_on
    while is_game_on:
        ball.move()
        if ball.xcor() < -500:
            scoreboard.increase_right_point()
            ball.replay()
        elif ball.xcor() > 500:
            scoreboard.increase_left_point()
            ball.replay()
        else:
            detect_paddle_collision()


def stop():
    global is_game_on
    is_game_on = not is_game_on
    if is_game_on:
        game()


screen.onkey(key="w", fun=paddle_left.move_up)
screen.onkey(key="s", fun=paddle_left.move_down)
screen.onkey(key="Up", fun=paddle_right.move_up)
screen.onkey(key="Down", fun=paddle_right.move_down)
screen.onkey(key="x", fun=stop)

game()

screen.exitonclick()
