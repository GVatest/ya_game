import pygame
import sys
import random
from breakout.main import Breakout


class MainMenu:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption("ya_game")
        self.screen.fill((0, 0, 0))

        self.links = []

        self.breakout_color = (r, g, b) = random.choices([i for i in range(256)], k=3)
        pygame.draw.rect(self.screen, self.breakout_color, (0, 0, 100, 100))
        pygame.display.flip()

        self.pacman_color = (r, g, b) = random.choices([i for i in range(256)], k=3)
        pygame.draw.rect(self.screen, self.pacman_color, (200, 0, 100, 100))
        pygame.display.flip()

    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 0 <= event.pos[0] <= 100 and 0 <= event.pos[1] <= 100:
                        Breakout().run()
                    elif 200 <= event.pos[0] <= 300 and 0 <= event.pos[1] <= 100:
                        from my_game.main import startGame
                        startGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        MainMenu().run()


MainMenu().run()
