from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
food = Food()

screen.setup(width=945, height=945)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
screen.tracer(0)

is_game_on = True

is_game_over = False

snake = Snake()

scoreboard = Scoreboard()


def check_wall_collision():
    global is_game_on
    global is_game_over
    if snake.head.xcor() > 460 or snake.head.xcor() < -460 or snake.head.ycor() > 460 or snake.head.ycor() < -460:
        is_game_on = False
        is_game_over = True


def game():
    global is_game_on
    global is_game_over
    while is_game_on:
        screen.update()
        time.sleep(0.120)
        snake.move()

        if snake.head.distance(food) < 20:
            food.go_to_position()
            snake.length += 1
            scoreboard.undo()
            scoreboard.display_score(snake.length - 3)
            snake.add_length()
            snake.add_length()

        is_game_on, is_game_over = snake.check_body_collision(is_game_on)
        check_wall_collision()

    while is_game_over:
        screen.update()
        scoreboard.undo()
        scoreboard.write(f"GAME OVER. YOUR SCORE WAS {snake.length -3}", align="center",  font=('Courier', 24, 'normal'))


def stop():
    global is_game_on
    is_game_on = not is_game_on
    if not is_game_over and is_game_on:
        game()


screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)
screen.onkey(key="Right", fun=snake.turn_right)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="x", fun=stop)

scoreboard.display_score(snake.length - 3)

game()

screen.exitonclick()
