import time
from turtle import Screen
from player import Player
from car_manager import CarManager

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
