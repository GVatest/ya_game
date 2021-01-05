import pygame
import sys
import os

SCREEN_SIZE = (360, 640)
BLACK = (0, 0, 0)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Flappy Bird')

# Clock
clock = pygame.time.Clock()


# Environment
bg = load_image('bg.png')
ground = load_image('ground.png')
ground = pygame.transform.scale(ground, (720, 100))
ground_rect = ground.get_rect()
bg_rect = bg.get_rect()
ground_rect.top = SCREEN_SIZE[1] - ground_rect.bottom


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BLACK)
    ground_rect.left -= 2
    if ground_rect.right <= SCREEN_SIZE[0]:
        ground_rect.left = 0

    screen.blit(bg, (0, 0))
    screen.blit(ground, (ground_rect.left, ground_rect.top))

    pygame.display.flip()
    clock.tick(100)