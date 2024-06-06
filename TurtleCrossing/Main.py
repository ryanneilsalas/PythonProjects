import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FONT = ()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.write(f"Level: 1", False, "center", ("Courier", 24, "normal"))
screen.onkeypress(player.move, "w")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.finish():
        scoreboard.level_up()
        car_manager.up_level()

screen.exitonclick()
