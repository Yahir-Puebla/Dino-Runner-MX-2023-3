import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
class ObstacleManager:
    #COMBINED_OBSTACLES = []
    def __init__(self):
        self.obstacles = []
        #self.OBSTACLES = (Bird + Cactus)
        #self.obstacle = random.choice(self.COMBINED_OBSTACLES)

    def update(self, game_speed, player):
        if len(self.obstacles) == 0:
            #self.obstacles.append(self.obstacle())
            #self.obstacles.append(random.choice(Bird(), Cactus()))
            self.obstacles.append(Cactus())
            #self.obstacles.append(Bird())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.remove(obstacle)
            obstacle.update(game_speed, player)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
