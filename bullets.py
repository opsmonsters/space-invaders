import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.color = self.settings.bullet_color
        self.bullet_rect = pygame.Rect(0, 0, 10, 10)
        self.bullet_rect.midtop = game.ship.image_rect.midtop

        self.y = float(self.bullet_rect.y)
    

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)
    
    def update(self):
        self.y -= self.settings.bullet_speed 
        self.bullet_rect.y = self.y
        print(self.y)

