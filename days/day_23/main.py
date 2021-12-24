from turtle import Screen
from turtle_crosser import TurtleCrosser
from scoreboard import Scoreboard
from car_manager import CarManager
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()

player = TurtleCrosser()

car_manager = CarManager()

scoreboard = Scoreboard()

is_game_on = True

screen.onkey(key="Up", fun=player.move)

car_manager.create_cars()

index = 11


def game():
    global index
    global is_game_on
    while is_game_on:
        time.sleep(0.1)
        screen.update()
        if player.check_finish_line():
            scoreboard.increase_score()
            car_manager.maximum_car_production += 1
        for car in car_manager.cars:
            car.move()
        if index % 20 == 0:
            car_manager.create_cars()
        for car in car_manager.cars:
            if car.distance(player) < 20:
                scoreboard.display_game_over()
                is_game_on = False
        index += 1


game()

screen.exitonclick()
