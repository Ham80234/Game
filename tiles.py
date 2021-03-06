import pygame
from Settings import * 
class Tile(pygame.sprite.Sprite): 

    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill([255, 255, 255])
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, shift):
        self.rect.x += shift