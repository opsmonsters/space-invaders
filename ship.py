import pygame

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("images/ship-1.bmp")
        self.image_rect = self.image.get_rect()

        self.image_rect.midbottom = self.screen_rect.midbottom

    def draw_ship(self):
        self.screen.blit(self.image, self.image_rect)
