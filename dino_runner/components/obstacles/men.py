from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import MEN

class Men(Obstacle):
    Y_POS_MEN = 30
    def __init__(self):
        self.image = MEN

        super().__init__(self.image)

        self.rect.y = self.Y_POS_MEN