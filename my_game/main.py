import pygame
import sys
import os
from my_game.player import Player
from my_game.ghost import Ghost
from my_game.point import Point
from my_game.wall import Wall


black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
purple = (255, 0, 255)
yellow = (255, 255, 0)


def load_image(name, colorkey=None):
    fullname = os.path.join('my_game\images', name)
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


def setupRoomOne(all_sprites_list):
    wall_list = pygame.sprite.Group()
    walls = [[0, 0, 6, 6],
             [60, 0, 600, 6],
             [0, 0, 6, 600],
             [0, 600, 606, 6],
             [600, 0, 6, 546],
             [300, 0, 6, 66],
             [60, 60, 186, 6],
             [360, 60, 186, 6],
             [60, 120, 66, 6],
             [60, 120, 6, 126],
             [180, 120, 246, 6],
             [300, 120, 6, 66],
             [480, 120, 66, 6],
             [540, 120, 6, 126],
             [120, 180, 126, 6],
             [120, 180, 6, 126],
             [360, 180, 126, 6],
             [480, 180, 6, 126],
             [180, 240, 6, 126],
             [180, 360, 246, 6],
             [420, 240, 6, 126],
             [240, 240, 42, 6],
             [324, 240, 42, 6],
             [240, 240, 6, 66],
             [240, 300, 126, 6],
             [360, 240, 6, 66],
             [0, 300, 66, 6],
             [540, 300, 66, 6],
             [60, 360, 66, 6],
             [60, 360, 6, 186],
             [480, 360, 66, 6],
             [540, 360, 6, 186],
             [120, 420, 366, 6],
             [120, 420, 6, 66],
             [480, 420, 6, 66],
             [180, 480, 246, 6],
             [300, 480, 6, 66],
             [120, 540, 126, 6],
             [360, 540, 126, 6]
             ]

    for item in walls:
        wall = Wall(item[0], item[1], item[2], item[3], blue)
        wall_list.add(wall)
        all_sprites_list.add(wall)

    return wall_list


def setupGate(all_sprites_list):
    gate = pygame.sprite.RenderPlain()
    gate.add(Wall(282, 242, 42, 2, white))
    all_sprites_list.add(gate)
    return gate


Pinky_directions = [
    [0, -30, 4],
    [15, 0, 9],
    [0, 15, 11],
    [-15, 0, 23],
    [0, 15, 7],
    [15, 0, 3],
    [0, -15, 3],
    [15, 0, 19],
    [0, 15, 3],
    [15, 0, 3],
    [0, 15, 3],
    [15, 0, 3],
    [0, -15, 15],
    [-15, 0, 7],
    [0, 15, 3],
    [-15, 0, 19],
    [0, -15, 11],
    [15, 0, 9]
]

Blinky_directions = [
    [0, -15, 4],
    [15, 0, 9],
    [0, 15, 11],
    [15, 0, 3],
    [0, 15, 7],
    [-15, 0, 11],
    [0, 15, 3],
    [15, 0, 15],
    [0, -15, 15],
    [15, 0, 3],
    [0, -15, 11],
    [-15, 0, 3],
    [0, -15, 11],
    [-15, 0, 3],
    [0, -15, 3],
    [-15, 0, 7],
    [0, -15, 3],
    [15, 0, 15],
    [0, 15, 15],
    [-15, 0, 3],
    [0, 15, 3],
    [-15, 0, 3],
    [0, -15, 7],
    [-15, 0, 3],
    [0, 15, 7],
    [-15, 0, 11],
    [0, -15, 7],
    [15, 0, 5]
]

Inky_directions = [
    [30, 0, 2],
    [0, -15, 4],
    [15, 0, 10],
    [0, 15, 7],
    [15, 0, 3],
    [0, -15, 3],
    [15, 0, 3],
    [0, -15, 15],
    [-15, 0, 15],
    [0, 15, 3],
    [15, 0, 15],
    [0, 15, 11],
    [-15, 0, 3],
    [0, -15, 7],
    [-15, 0, 11],
    [0, 15, 3],
    [-15, 0, 11],
    [0, 15, 7],
    [-15, 0, 3],
    [0, -15, 3],
    [-15, 0, 3],
    [0, -15, 15],
    [15, 0, 15],
    [0, 15, 3],
    [-15, 0, 15],
    [0, 15, 11],
    [15, 0, 3],
    [0, -15, 11],
    [15, 0, 11],
    [0, 15, 3],
    [15, 0, 1],
]

Clyde_directions = [
    [-30, 0, 2],
    [0, -15, 4],
    [15, 0, 5],
    [0, 15, 7],
    [-15, 0, 11],
    [0, -15, 7],
    [-15, 0, 3],
    [0, 15, 7],
    [-15, 0, 7],
    [0, 15, 15],
    [15, 0, 15],
    [0, -15, 3],
    [-15, 0, 11],
    [0, -15, 7],
    [15, 0, 3],
    [0, -15, 11],
    [15, 0, 9],
]

pl = len(Pinky_directions) - 1
bl = len(Blinky_directions) - 1
il = len(Inky_directions) - 1
cl = len(Clyde_directions) - 1

pygame.init()

screen = pygame.display.set_mode([606, 606])
pygame.display.set_caption('Pacman')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(black)

clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 24)

w = 303 - 16
p_h = (7 * 60) + 19
m_h = (4 * 60) + 19
b_h = (3 * 60) + 19
i_w = 303 - 16 - 32
c_w = 303 + (32 - 16)


def startGame():
    all_sprites_list = pygame.sprite.Group()

    point_list = pygame.sprite.Group()

    monsta_list = pygame.sprite.Group()

    pacman_collide = pygame.sprite.Group()

    wall_list = setupRoomOne(all_sprites_list)

    gate = setupGate(all_sprites_list)

    p_turn = 0
    p_steps = 0

    b_turn = 0
    b_steps = 0

    i_turn = 0
    i_steps = 0

    c_turn = 0
    c_steps = 0

    #Visuality
        #pacman
    stage3 = load_image('stage3.png', colorkey=-1)
    stage3 = pygame.transform.scale(stage3, (32, 32))

    stage2 = load_image('stage2.png', colorkey=-1)
    stage2r = pygame.transform.scale(stage2, (32, 32))
    stage2l = pygame.transform.rotate(stage2r, 180)
    stage2u = pygame.transform.rotate(stage2r, 90)
    stage2d = pygame.transform.rotate(stage2r, -90)

    stage = load_image('stage1.png', colorkey=-1)
    stager = pygame.transform.scale(stage, (32, 32))
    stagel = pygame.transform.rotate(stager, 180)
    stageu = pygame.transform.rotate(stager, 90)
    staged = pygame.transform.rotate(stager, -90)

    Pacman = Player(w, p_h, stage3)
    all_sprites_list.add(Pacman)
    pacman_collide.add(Pacman)

    image = load_image('Blinky.png', colorkey=-1)
    image = pygame.transform.scale(image, (32, 32))
    Blinky = Ghost(w, b_h, image)
    monsta_list.add(Blinky)
    all_sprites_list.add(Blinky)

    image = load_image('Pinky.png', colorkey=-1)
    image = pygame.transform.scale(image, (32, 32))
    Pinky = Ghost(w, m_h, image)
    monsta_list.add(Pinky)
    all_sprites_list.add(Pinky)

    image = load_image('Inky.png', colorkey=-1)
    image = pygame.transform.scale(image, (32, 32))
    Inky = Ghost(i_w, m_h, image)
    monsta_list.add(Inky)
    all_sprites_list.add(Inky)

    image = load_image('Clyde.png', colorkey=-1)
    image = pygame.transform.scale(image, (32, 32))
    Clyde = Ghost(c_w, m_h, image)
    monsta_list.add(Clyde)
    all_sprites_list.add(Clyde)

    for row in range(19):
        for column in range(19):
            if (row == 7 or row == 8) and (column == 8 or column == 9 or column == 10):
                continue
            else:
                point = Point(yellow, 4, 4)

                point.rect.x = (30 * column + 6) + 25
                point.rect.y = (30 * row + 6) + 25

                b_collide = pygame.sprite.spritecollide(point, wall_list, False)
                p_collide = pygame.sprite.spritecollide(point, pacman_collide, False)

                if not b_collide and not p_collide:
                    point_list.add(point)
                    all_sprites_list.add(point)

    bll = len(point_list)

    score = 0
    stage_counter = 0
    flag = ''
    STAGEEVENT = pygame.USEREVENT
    pygame.time.set_timer(STAGEEVENT, 200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    MainMenu().run()
                if event.key == pygame.K_LEFT:
                    Pacman.changespeed(-30, 0)
                    # Counter variant
                    # if stage_counter == 0:
                    #     Pacman.image = stage2l
                    #     stage_counter += 1
                    # else:
                    #     Pacman.image = stagel
                    #     stage_counter = 0
                    flag = 'l'

                if event.key == pygame.K_RIGHT:
                    Pacman.changespeed(30, 0)
                    flag = 'r'

                if event.key == pygame.K_UP:
                    Pacman.changespeed(0, -30)
                    flag = 'u'

                if event.key == pygame.K_DOWN:
                    Pacman.changespeed(0, 30)
                    flag = 'd'

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    Pacman.changespeed(30, 0)
                if event.key == pygame.K_RIGHT:
                    Pacman.changespeed(-30, 0)
                if event.key == pygame.K_UP:
                    Pacman.changespeed(0, 30)
                if event.key == pygame.K_DOWN:
                    Pacman.changespeed(0, -30)

            if event.type == STAGEEVENT and flag == 'r':
                if stage_counter == 0:
                    Pacman.image = stage2r
                    stage_counter += 1
                else:
                    Pacman.image = stager
                    stage_counter = 0
            elif event.type == STAGEEVENT and flag == 'l':
                if stage_counter == 0:
                    Pacman.image = stage2l
                    stage_counter += 1
                else:
                    Pacman.image = stagel
                    stage_counter = 0
            elif event.type == STAGEEVENT and flag == 'u':
                if stage_counter == 0:
                    Pacman.image = stage2u
                    stage_counter += 1
                else:
                    Pacman.image = stageu
                    stage_counter = 0
            elif event.type == STAGEEVENT and flag == 'd':
                if stage_counter == 0:
                    Pacman.image = stage2d
                    stage_counter += 1
                else:
                    Pacman.image = staged
                    stage_counter = 0

        Pacman.update(wall_list, gate)

        returned = Pinky.changespeed(Pinky_directions, False, p_turn, p_steps, pl)
        p_turn = returned[0]
        p_steps = returned[1]
        Pinky.changespeed(Pinky_directions, False, p_turn, p_steps, pl)
        Pinky.update(wall_list, False)

        returned = Blinky.changespeed(Blinky_directions, False, b_turn, b_steps, bl)
        b_turn = returned[0]
        b_steps = returned[1]
        Blinky.changespeed(Blinky_directions, False, b_turn, b_steps, bl)
        Blinky.update(wall_list, False)

        returned = Inky.changespeed(Inky_directions, False, i_turn, i_steps, il)
        i_turn = returned[0]
        i_steps = returned[1]
        Inky.changespeed(Inky_directions, False, i_turn, i_steps, il)
        Inky.update(wall_list, False)

        returned = Clyde.changespeed(Clyde_directions, "clyde", c_turn, c_steps, cl)
        c_turn = returned[0]
        c_steps = returned[1]
        Clyde.changespeed(Clyde_directions, "clyde", c_turn, c_steps, cl)
        Clyde.update(wall_list, False)

        points_hit_list = pygame.sprite.spritecollide(Pacman, point_list, True)

        if points_hit_list:
            score += 1

        screen.fill(black)

        wall_list.draw(screen)
        gate.draw(screen)
        all_sprites_list.draw(screen)
        monsta_list.draw(screen)

        text = font.render("Score: " + str(score) + "/" + str(bll), True, red)
        screen.blit(text, [10, 10])

        if score == bll:
            doNext("Congratulations, you won!", 145, all_sprites_list, point_list, monsta_list, pacman_collide,
                wall_list, gate)

        monsta_hit_list = pygame.sprite.spritecollide(Pacman, monsta_list, False)

        if monsta_hit_list:
            doNext("Game Over", 235, all_sprites_list, point_list, monsta_list, pacman_collide, wall_list, gate)

        pygame.display.flip()

        clock.tick(10)


def doNext(message, left, all_sprites_list, point_list, monsta_list, pacman_collide, wall_list, gate):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    del all_sprites_list
                    del point_list
                    del monsta_list
                    del pacman_collide
                    del wall_list
                    del gate
                    startGame()

        w = pygame.Surface((400, 200))
        w.set_alpha(10)
        w.fill((128, 128, 128))
        screen.blit(w, (100, 200))

        text1 = font.render(message, True, white)
        screen.blit(text1, [left, 233])

        text2 = font.render("To play again, press ENTER.", True, white)
        screen.blit(text2, [135, 303])
        text3 = font.render("To quit, press ESCAPE.", True, white)
        screen.blit(text3, [165, 333])

        pygame.display.flip()

        clock.tick(10)


startGame()
