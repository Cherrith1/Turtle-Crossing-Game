from turtle import Turtle
from random import choice,randint

colors = ["violet", "blue", "cyan", "yellow", "red", "green", "black", "pink"]
MOVE = 5
MOVE_INC = 10


class Car:
    def __init__(self):
        self.all_cars = []
        self.move_speed = MOVE
        
    def create_car(self):
        number = randint(1,6)
        if number == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(choice(colors))
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(300, randint(-250,250))
            self.all_cars.append(new_car)

    def move_forward(self):
        for cars in self.all_cars:
            cars.forward(self.move_speed)

    def level_up(self):
        self.move_speed += MOVE_INC
