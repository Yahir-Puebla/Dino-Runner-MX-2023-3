import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
class Bird(Obstacle):
    #Y_POS_BIRD = [100, 150, 200, 250, 300]

    def __init__(self):
        self.step_index = 0 
        self.Y_POS_BIRD = random.randint(100, 250)
        self.image = random.choice(BIRD)
        super().__init__(self.image)
        self.rect.y = self.Y_POS_BIRD

