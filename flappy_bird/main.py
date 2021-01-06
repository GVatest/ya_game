import pygame
import sys
import os

SCREEN_SIZE = (360, 640)
BLACK = (0, 0, 0)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # if file not found #################
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((15, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Flappy Bird')

# Clock #################
clock = pygame.time.Clock()


# Environment #################
bg = load_image('bg.png')
ground = load_image('ground.png')
ground = pygame.transform.scale(ground, (720, 100))
ground_rect = ground.get_rect()
bg_rect = bg.get_rect()
ground_rect.top = SCREEN_SIZE[1] - ground_rect.bottom


# Bird #################
bird = load_image('bird.png', -1)
bird = pygame.transform.scale(bird, (60, 50))
bird_rect = bird.get_rect(center=(100, 512))
bird_rect.top = SCREEN_SIZE[1] // 2
bird_flappy = load_image('bird_flapp.png')
bird_flappy = pygame.transform.scale(bird_flappy, (60, 50))
bird_fly = load_image('bird_fly.png')
bird_fly = pygame.transform.scale(bird_fly, (60, 50))

# Bird Animation #################
FLAPPEVENT = pygame.USEREVENT
pygame.time.set_timer(FLAPPEVENT, 80)
flapp_counter = 0
gravity = 0
bird_movement = 0


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT:
            flapp_counter = (flapp_counter + 1) % 3

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gravity = 0.25
                bird_movement = 0
                bird_movement -= 9

    screen.fill(BLACK)

    # ground movement #################
    ground_rect.left -= 2
    if ground_rect.right <= SCREEN_SIZE[0]:
        ground_rect.left = 0

    screen.blit(bg, (0, 0))
    screen.blit(ground, ground_rect)

    # bird movement #################
    bird_movement += gravity
    bird_rect.centery += bird_movement
    if flapp_counter == 0:
        screen.blit(bird, bird_rect)
    elif flapp_counter == 1:
        screen.blit(bird_fly, bird_rect)
    else:
        screen.blit(bird_flappy, bird_rect)

    pygame.display.flip()
    clock.tick(100)