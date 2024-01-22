from obstacle import Obstacle


class ObstacleManager:
    def __init__(self):
        self.obstacles = list[Obstacle]()
        self.difficulty = 0

    def create_obstacles(self, start):
        while len(self.obstacles) < 25:
            if start is not None:
                new_obstacle = Obstacle(start)
            else:
                new_obstacle = Obstacle(None)
            self.obstacles.append(new_obstacle)

    def move_obstacles(self, arg_player):
        collided = False
        for obs in self.obstacles:
            obs.move(5+self.difficulty*3)
            col = self.collided(arg_player)
            if obs.xcor() < -320:
                self.obstacles.remove(obs)
                del obs
            if col:
                collided = col
        return collided

    def collided(self, arg_player):
        collided = False
        for arg_obstacle in self.obstacles:
            if (25 > arg_obstacle.xcor() - arg_player.xcor() > -25 and 20 > arg_obstacle.ycor() - arg_player.ycor() > -20
                    or 25 > arg_obstacle.xcor() - arg_player.xcor() > -25 and 20 > arg_obstacle.ycor() - arg_player.ycor() > -20):
                collided = True
        return collided
