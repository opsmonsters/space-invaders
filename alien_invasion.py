import pygame
import sys
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):

        self.settings = Settings()

        pygame.init()
        pygame.display.set_caption("My Alien Invasion")
        self.screen = pygame.display.set_mode(self.settings.window_size)

        self.ship = Ship(self)

    def check_events(self):
        for event in pygame.event.get():
            # Quit if closed
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                print(self.ship.image_rect.right)
                print(self.ship.screen_rect.right)
                if(event.key == pygame.K_LEFT and self.ship.image_rect.left > 20):
                   self.ship.move_left = True 
                if(event.key == pygame.K_RIGHT and self.ship.image_rect.right < 1000):
                   self.ship.move_right = True 
  
    
    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.draw_ship()
        self.ship.move_ship()
        pygame.display.flip()

    def run_game(self):
        while True:
            self.check_events();
            self.update_screen();


game = AlienInvasion()
game.run_game()
