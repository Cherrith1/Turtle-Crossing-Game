from turtle import Screen
import time
from player import Player
from car import Car
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(n=0)

game_is_on = True

player = Player()
car_manager = Car()
score_board = ScoreBoard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")


while game_is_on :
    screen.update()
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move_forward()

    screen.update()

    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            score_board.game_over()
            game_is_on = False

    screen.update()

    if player.ycor() > 260 :
        player.level_up()
        car_manager.level_up()
        score_board.level_up()


screen.exitonclick()