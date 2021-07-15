from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-260, 260)
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(arg=f"Level : {self.level}", align="left", font=("Arial", 20, "normal"))

    def level_up(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.goto(0,270)
        self.write(arg="Game Over", align="center", font=("Arial", 30, "normal"))