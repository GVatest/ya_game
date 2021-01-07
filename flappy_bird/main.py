import pygame
import sys
import os
import random

SCREEN_SIZE = (360, 640)
BLACK = (0, 0, 0)


def create_pipe():
    new_pipe = pipe.get_rect(top=random.choice([i for i in range(200, 480)]), left=360)
    return new_pipe, pipe.get_rect(bottom=new_pipe.top - 150, left=360)


def move_pipes(pipes):
    for p in pipes:
        p[0].centerx -= 4
        p[1].centerx -= 4
    return pipes


def draw_pipes(pipes):
    for p in pipes:
        screen.blit(pipe, p[0])
        screen.blit(pipe_rotated, p[1])


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
bird = pygame.transform.scale(bird, (50, 40))
bird_rect = bird.get_rect(center=(100, 320))
bird_flappy = load_image('bird_flapp.png')
bird_flappy = pygame.transform.scale(bird_flappy, (50, 40))
bird_fly = load_image('bird_fly.png')
bird_fly = pygame.transform.scale(bird_fly, (50, 40))

# Bird Animation #################
FLAPPEVENT = pygame.USEREVENT
pygame.time.set_timer(FLAPPEVENT, 100)
flapp_counter = 0
gravity = 0
bird_movement = 0

# Pipes #################
pipe = load_image('pipe.png', -1)
pipe = pygame.transform.scale(pipe, (50, 500))
pipe_rotated = pygame.transform.rotate(pipe, 180)


PIPESPAWNEVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PIPESPAWNEVENT, 1500)
pipes_group = []


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
        if event.type == PIPESPAWNEVENT:
            pipes_group.append(create_pipe())

    screen.fill(BLACK)

    screen.blit(bg, (0, 0))

    # pipes
    pipes_group = move_pipes(pipes_group)
    draw_pipes(pipes_group)


    # ground movement #################
    ground_rect.left -= 4
    if ground_rect.right <= SCREEN_SIZE[0]:
        ground_rect.left = 0

    screen.blit(ground, ground_rect)

    # bird movement #################
    bird_movement += gravity
    bird_rect.centery += bird_movement

    # bird animation
    bird_rotated = pygame.transform.rotate(bird, -bird_movement * 3)
    bird_fly_rotated = pygame.transform.rotate(bird_fly, -bird_movement * 3)
    bird_flappy_rotated = pygame.transform.rotate(bird_flappy, -bird_movement * 3)

    if flapp_counter == 0:
        screen.blit(bird_rotated, bird_rect)
    elif flapp_counter == 1:
        screen.blit(bird_fly_rotated, bird_rect)
    else:
        screen.blit(bird_flappy_rotated, bird_rect)

    pygame.display.flip()
    clock.tick(100)
