import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
    
    def update(self, game_speed, points, player):
        if len(self.power_ups) == 0: #0 and points % 200 == 0
            type_power_ups = random.randint(1, 2)
            
            match type_power_ups:
                    case 1:
                        self.power_ups.append(Shield())
                        print("Power up")
                    case 2:
                        self.power_ups.append(Hammer())
                        print("Power up")


        for power_up in self.power_ups:
            if power_up.used or power_up.rect.x < -power_up.rect.width:
                self.power_ups.remove(power_up)
            if power_up.used:
                player.set_power_up(power_up)
            power_up.update(game_speed, player)  
    
    def reset_Power(self):
        self.power_ups = []

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
