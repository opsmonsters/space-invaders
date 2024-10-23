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

    def run_game(self):
        print("Game Running")
        while True:
            for event in pygame.event.get():
                #close login
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.draw_ship()

            
            pygame.display.flip()


game = AlienInvasion()
game.run_game()
