import pygame
import sys
import os
import random

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


def create_pipe(pipe):
    new_pipe = pipe.get_rect(top=random.choice([i for i in range(200, 450)]), left=360)
    return new_pipe, pipe.get_rect(bottom=new_pipe.top - 150, left=360)


def move_pipes(pipes):
    for p in pipes:
        p[0].centerx -= 3
        p[1].centerx -= 3
    return pipes


def draw_pipes(pipes, screen, pipe, pipe_rotated):
    for p in pipes:
        screen.blit(pipe, p[0])
        screen.blit(pipe_rotated, p[1])


def is_collide(pipes, counter, bird_rect, hit, die):
    for i in pipes:
        if bird_rect.colliderect(i[0]) or bird_rect.colliderect(i[1]):
            hit.play()
            return False, counter
        if i[0].right + 2 > bird_rect.left > i[0].right - 2:
            counter += 1
    if bird_rect.bottom >= 570:
        die.play()
        return False, counter
    if bird_rect.top < -200:
        die.play()
        return False, counter
    return True, counter


def run():
    pygame.init()

    score_counter = 0
    highest_score = 0

    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Flappy Bird')
    font = pygame.font.Font(None, 50)
    game_over = font.render('Game Over', True, (64, 47, 3))
    press = font.render('Press Space', True, (64, 47, 3))
    play = font.render('Press Space to play', True, (64, 47, 3))
    game_over_x = SCREEN_SIZE[0] // 2 - game_over.get_width() // 2
    press_x = SCREEN_SIZE[0] // 2 - press.get_width() // 2
    play_x = SCREEN_SIZE[0] // 2 - play.get_width() // 2

    # Clock #################
    clock = pygame.time.Clock()

    # Environment #################
    bg = load_image('bg.png')
    ground = load_image('ground.png')
    ground = pygame.transform.scale(ground, (720, 70))
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

    game_active = False
    game_flag = False

    # Sounds #################
    flapp_sound = pygame.mixer.Sound('data/sounds/sfx_wing.wav')
    hit_sound = pygame.mixer.Sound('data/sounds/sfx_hit.wav')
    die_sound = pygame.mixer.Sound('data/sounds/sfx_die.wav')
    score_sound = pygame.mixer.Sound('data/sounds/sfx_point.wav')

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                flapp_counter = (flapp_counter + 1) % 3

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    bird_movement = 0
                    bird_movement -= 7
                    game_flag = True
                    flapp_sound.play()
            if event.type == PIPESPAWNEVENT and game_active:
                pipes_group.append(create_pipe(pipe))

        screen.fill(BLACK)

        screen.blit(bg, (0, 0))

        if game_active:
            gravity = 0.25

            # pipes #################
            pipes_group = move_pipes(pipes_group)
            draw_pipes(pipes_group, screen, pipe, pipe_rotated)
            colide, score_counter = is_collide(pipes_group, score_counter, bird_rect, hit_sound, die_sound)
            if score_counter > highest_score:
                highest_score = score_counter
            if not colide:
                bird_rect.centery = 320
                bird_movement = 0
                gravity = 0
                pipes_group = []
                game_active = False
                score_counter = 0
            score = font.render(str(score_counter), True, (64, 47, 3))
            score_x = SCREEN_SIZE[0] // 2 - score.get_width() // 2
            screen.blit(score, (score_x, 100))

        # ground movement #################
        ground_rect.left -= 3
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

        if not game_active and game_flag:
            screen.blit(game_over, (game_over_x, 100))
            screen.blit(press, (press_x, 150))
            highest_score_blit = font.render(str(highest_score), True, (64, 47, 3))
            highest_score_blit_x = SCREEN_SIZE[0] // 2 - highest_score_blit.get_width() // 2
            screen.blit(highest_score_blit, (highest_score_blit_x, 200))

        if not game_flag:
            screen.blit(play, (play_x, 100))

        pygame.display.flip()
        clock.tick(100)


run()
