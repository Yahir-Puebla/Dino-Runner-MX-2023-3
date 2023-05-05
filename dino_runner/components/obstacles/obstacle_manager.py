import random
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.men import Men 
class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, player, points):
        if len(self.obstacles) == 0:
            type_obstacle = random.randint(1,2)
            if points > 1000:
                self.obstacles.append(Men())
                if points > 1025:
                    pygame.time.delay(628) 
                    player.dino_dead = True
                
            else:

                match type_obstacle:
                    case 1:
                        self.obstacles.append(Cactus())
                    case 2:
                        self.obstacles.append(Bird())
                    case 3:
                        self.obstacles.append(Men())
            
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.remove(obstacle)
            obstacle.update(game_speed, player)

    def obstacle_finaly(self):
        if len(self.obstacles) == 0:
            self.obstacles.append(Men())
        
    def reset_obstacles(self):
        self.obstacles = []

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)


    