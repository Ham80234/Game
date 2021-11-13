import pygame
from Settings import *
from level import Level

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

level = Level(LEVEL, screen)
Clock = pygame.time.Clock()



while RUN: 
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    screen.fill([0,0,0])
    level.run()

    pygame.display.update()
    Clock.tick(60)
