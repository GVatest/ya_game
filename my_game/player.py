import pygame


class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0

    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert()

        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.prev_x = x
        self.prev_y = y

    # Change the speed of the player
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    # Find a new position for the player
    def update(self, walls, gate):
        # Get the old position, in case we need to go back to it

        old_x = self.rect.left
        new_x = old_x + self.change_x
        old_y = self.rect.top
        new_y = old_y + self.change_y

        if new_y < 0:
            new_y = 559
            new_x = 557

        if new_x > 606:
            new_x = 17
            new_y = 19

        self.rect.left = new_x
        self.rect.top = new_y

        x_collide = pygame.sprite.spritecollide(self, walls, False)

        if x_collide:
            self.rect.left = old_x

        y_collide = pygame.sprite.spritecollide(self, walls, False)

        if y_collide:
            self.rect.top = old_y

        if gate:
            gate_hit = pygame.sprite.spritecollide(self, gate, False)
            if gate_hit:
                self.rect.left = old_x
                self.rect.top = old_y
