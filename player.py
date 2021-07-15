from turtle import Turtle

START = (0, -280)
FINISH_LINE = (0, 280)
MOVE_DIST = 10


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.color("green")
        self.penup()
        self.goto(START)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DIST)

    def level_up(self):
        self.goto(START)