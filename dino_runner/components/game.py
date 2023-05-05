import pygame
from dino_runner.components import text_utils
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


class Game:
    hig_scores = []

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.runnig = True
        self.death_count = 0
        self.letras_validas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.gamertag = []
        
    def execute(self):
        while self.runnig:
            if not self.playing:
                self.show_menu()
                #self.menu_name_player()

    def show_menu(self):
        self.runnig = True
        while_color = (255, 255, 255)
        self.screen.fill(while_color)
        self.print_menu_elemt()
        

        pygame.display.update()

        self.handle_key_events_on_menu()
        

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runnig = False
                self.player = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()
                

    def print_menu_elemt(self):
        if self.death_count == 0:
            text, text_rect = text_utils.get_center_message(
                'press any Key to Start')
            self.screen.blit(text, text_rect)
        if self.death_count > 0:
            pygame.time.delay(1000)
            text, text_rect = text_utils.get_center_message(
                'press any Key to Restart')
            self.screen.blit(text, text_rect)
           
            


    def menu_name_player(self):
        while True:
            entrada = input("What is your Gamerttag?: ")
            if len(entrada) == 3:
                entrada = entrada.lower()
                self.hig_scores.append({"nombre": entrada, "puntos": self.points})
                self.execute()
                print(self.hig_scores)
                break
            else:
                print("La entrada no es válida. Solo se admiten las letras a, b y c, y no se admiten números.")
            

    
    def reset(self):
        self.player = False
        self.game_speed = 20
        self.points = 0
        self.runnig = True
        self.death_count = 0
        self.player = Dinosaur()
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_Power()
      

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        #pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.points += 1
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self.player, self.points)
        self.power_up_manager.update(self.game_speed, self.points, self.player)
        if self.player.dino_dead:
            self.playing = False
            self.death_count += 1

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.score()
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            # increse game_speed
            self.game_speed +=1

        text, text_rect = text_utils.get_score_element(self.points)
        self.screen.blit(text, text_rect)
        
    