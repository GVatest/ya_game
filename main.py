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


coords_breakout = []
coords_pacman = []
coords_flappy = []
coords_space = []
coords_doodle = []
coords_snake = []
coords_tetris = []
count = 401
count2 = 0
count3 = 0

# breakout
for i in range(0, 401):
    for j in range(0, count):
        coords_breakout.append((j, i))
    count3 += 1
    if count3 == 2:
        count -= 1
        count3 = 0

# pacman
count2 = 400
count = 601
count3 = 0
for i in range(0, 401):
    for j in range(count2, count):
        coords_pacman.append((j, i))
    count3 += 1
    if count3 == 2:
        count += 1
        count2 -= 1
        count3 = 0

# flappy_bird
count = 600
count3 = 0
for i in range(0, 401):
    for j in range(count, 1000):
        coords_flappy.append((j, i))
    count3 += 1
    if count3 == 2:
        count += 1
        count3 = 0

# space
count = 201
count2 = 0
count3 = 0
for i in range(400, 801):
    for j in range(0, count):
        coords_space.append((j, i))
    count3 += 1
    if count3 == 2:
        count += 1
        count3 = 0

# doodle
count2 = 200
count = 801
count3 = 0
for i in range(400, 801):
    for j in range(count2, count):
        coords_doodle.append((j, i))
    count3 += 1
    if count3 == 2:
        count -= 1
        count2 += 1
        count3 = 0

# snake
count = 800
count3 = 0
for i in range(400, 801):
    for j in range(count, 1000):
        coords_snake.append((j, i))
    count3 += 1
    if count3 == 2:
        count -= 1
        count3 = 0


class MainMenu:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 1000))
        pygame.display.set_caption("ya_game")
        pygame.display.set_icon(pygame.image.load('Y.ico'))
        self.screen.fill((0, 0, 0))

        self.links = []

        self.breakout_color = (r, g, b) = random.choices([i for i in range(256)], k=3)
        pygame.draw.polygon(self.screen, self.breakout_color, ((0, 0), (0, 400), (200, 400), (400, 0)))
        pygame.display.flip()

        self.pacman_color = (r, g, b) = random.choices([i for i in range(256)], k=3)
        pygame.draw.polygon(self.screen, self.pacman_color, ((400, 0), (200, 400), (800, 400), (600, 0)))
        pygame.display.flip()

        self.flappy_color = (r, g, b) = random.choices([i for i in range(256)], k=3)
        pygame.draw.polygon(self.screen, self.flappy_color, ((600, 0), (800, 400), (1000, 400), (1000, 0)))
        pygame.display.flip()

        self.space_color = (r, g, b) = random.choices([i for i in range(256)], k=3)
        pygame.draw.polygon(self.screen, self.space_color, ((0, 400), (200, 400), (400, 800), (0, 800)))
        pygame.display.flip()

        self.doodle_color = (r, g, b) = random.choices([i for i in range(256)], k=3)
        pygame.draw.polygon(self.screen, self.doodle_color, ((200, 400), (400, 800), (600, 800), (800, 400)))
        pygame.display.flip()

        self.snake_color = (r, g, b) = random.choices([i for i in range(256)], k=3)
        pygame.draw.polygon(self.screen, self.snake_color, ((800, 400), (1000, 400), (1000, 800), (600, 800)))
        pygame.display.flip()

        self.tetris_color = (r, g, b) = random.choices([i for i in range(256)], k=3)
        pygame.draw.rect(self.screen, self.tetris_color, (0, 800, 1000, 1000))
        pygame.display.flip()


    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos in coords_breakout:
                        Breakout().run()
                    elif event.pos in coords_pacman:
                        from my_game.main import startGame
                        startGame()
                    elif event.pos in coords_flappy:
                        from flappy_bird.main import run
                        run()
                    elif event.pos in coords_space:
                        exec_full('SpaceShooter\spaceshooter.py')
                    elif event.pos in coords_doodle:
                        from DoodleJumpPyGame.main import Game
                        Game().run()
                    elif event.pos in coords_snake:
                        exec_full('Snake/snake.py')
                    elif 0 <= event.pos[0] <= 1000 and 800 <= event.pos[1] <= 1000:
                        exec_full('tetris_pygame/tetris3.py')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        MainMenu().run()


MainMenu().run()
