import time
from turtle import *

from obstacle_manager import ObstacleManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
player = Player()
scoreboard = Scoreboard()
obstacle_manager = ObstacleManager()

screen.setup(600, 600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

obstacle_manager.create_obstacles("Start")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    obstacle_manager.create_obstacles(None)
    collided = obstacle_manager.move_obstacles(player)
    if collided:
        obstacle_manager.difficulty = 0
        time.sleep(1)
        player.goto(0, -280)
        scoreboard.update_score(obstacle_manager.difficulty+1)

    if game_is_on and player.ycor() > 280:
        obstacle_manager.difficulty += 1
        scoreboard.update_score(obstacle_manager.difficulty+1)
        player.goto(0, -280)

screen.exitonclick()
