import random
from turtle import *

COLORS = ["red", "blue", "yellow", "orange", "green", "purple", "brown"]


class Obstacle(Turtle):
    def __init__(self, start):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.penup()
        if start is not None:
            self.goto(random.randint(-300, 300), random.randint(-250, 250))
        else:
            self.goto(300, random.randint(-250, 250))
        self.setheading(180)

    def move(self, pace):
        self.forward(pace)

    def __del__(self):
        print("Obstacle destroyed")
