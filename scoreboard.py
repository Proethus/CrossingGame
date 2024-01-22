from turtle import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-240,240)
        self.write(f"Level: {1}", False, "center", ("Arial", 24, "normal"))

    def update_score(self, level):
        self.clear()
        self.goto(-240,240)
        self.write(f"Level: {level}", False, "center", ("Arial", 24, "normal"))
