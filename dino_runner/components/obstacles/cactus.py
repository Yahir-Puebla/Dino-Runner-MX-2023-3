import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class Cactus(Obstacle):
    Y_POS_CACTUS_SMALL= 325
    Y_POS_CACTUS_LARGE = 310
    COMBINED_CACTUS = []



    def __init__(self):
        self.COMBINED_CACTUS = (SMALL_CACTUS + LARGE_CACTUS)
        self.image = random.choice(self.COMBINED_CACTUS)

        super().__init__(self.image)

        self.rect.y = self.Y_POS_CACTUS_SMALL

        if self.image in SMALL_CACTUS:
            self.rect.y = self.Y_POS_CACTUS_SMALL
        else:
            self.rect.y = self.Y_POS_CACTUS_LARGE
