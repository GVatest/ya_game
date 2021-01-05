import pygame
import sys

SCREEN_SIZE = (360, 640)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Flappy Bird')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()