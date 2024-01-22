from turtle import *


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("arrow")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move_up(self):
        self.setheading(90)
        self.forward(20)

    def move_down(self):
        self.setheading(270)
        self.forward(20)

    def move_left(self):
        self.setheading(180)
        self.forward(20)

    def move_right(self):
        self.setheading(0)
        self.forward(20)
