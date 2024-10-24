import pygame
from settings import Settings

class Ship:
    def __init__(self, game):

        self.settings = Settings()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("images/ship-1.bmp")
        self.image_rect = self.image.get_rect()

        self.image_rect.midbottom = self.screen_rect.midbottom

        self.move_right = False
        self.move_left = False

    def draw_ship(self):
        self.screen.blit(self.image, self.image_rect)
    
    def move_ship(self):
        if(self.move_left):
            self.image_rect.x -= self.settings.ship_speed
            self.move_left = False
        if(self.move_right):
            self.image_rect.x += self.settings.ship_speed 
            self.move_right = False

