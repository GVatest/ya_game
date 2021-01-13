import pygame
import sys
import random
from breakout.main import Breakout


def exec_full(filepath):
    import os
    global_namespace = {
        "__file__": filepath,
        "__name__": "__main__",
    }
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), global_namespace)


class MainMenu:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 1000))
        pygame.display.set_caption("ya_game")
        self.screen.fill((0, 0, 0))

        self.links = []

        self.breakout_color = (r, g, b) = random.choices([i for i in range(256)], k=3)
        pygame.draw.rect(self.screen, self.breakout_color, (0, 0, 100, 100))
        pygame.display.flip()

        self.pacman_color = (r, g, b) = random.choices([i for i in range(256)], k=3)
        pygame.draw.rect(self.screen, self.pacman_color, (200, 0, 100, 100))
        pygame.display.flip()

        self.flappy_color = (r, g, b) = random.choices([i for i in range(256)], k=3)
        pygame.draw.rect(self.screen, self.flappy_color, (400, 0, 100, 100))
        pygame.display.flip()

        self.space_color = (r, g, b) = random.choices([i for i in range(256)], k=3)
        pygame.draw.rect(self.screen, self.space_color, (600, 0, 100, 100))
        pygame.display.flip()

        self.doodle_color = (r, g, b) = random.choices([i for i in range(256)], k=3)
        pygame.draw.rect(self.screen, self.doodle_color, (800, 0, 100, 100))
        pygame.display.flip()

        self.snake_color = (r, g, b) = random.choices([i for i in range(256)], k=3)
        pygame.draw.rect(self.screen, self.snake_color, (1000, 0, 100, 100))
        pygame.display.flip()

        self.tetris_color = (r, g, b) = random.choices([i for i in range(256)], k=3)
        pygame.draw.rect(self.screen, self.tetris_color, (0, 100, 100, 100))
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
                    elif 400 <= event.pos[0] <= 500 and 0 <= event.pos[1] <= 100:
                        from flappy_bird.main import run
                        run()
                    elif 600 <= event.pos[0] <= 700 and 0 <= event.pos[1] <= 100:
                        exec_full('SpaceShooter\spaceshooter.py')
                    elif 800 <= event.pos[0] <= 900 and 0 <= event.pos[1] <= 100:
                        from DoodleJumpPyGame.main import Game
                        Game().run()
                    elif 1000 <= event.pos[0] <= 1100 and 0 <= event.pos[1] <= 100:
                        exec_full('Snake/snake.py')
                    elif 0 <= event.pos[0] <= 100 and 100 <= event.pos[1] <= 200:
                        from tetris.Tetris import main, win
                        main(win)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        MainMenu().run()


MainMenu().run()
