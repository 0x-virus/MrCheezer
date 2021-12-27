import pygame
from pygame.locals import *


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        if x1 == x2:
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
            self.image = pygame.Surface([1, y2 - y1])
        else:
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)
            self.image = pygame.Surface([x2 - x1, 1])


class Player(pygame.sprite.Sprite):
    image = pygame.image.load('data/afk1.png')
    image2 = pygame.image.load('data/afk2.png')
    image3 = pygame.image.load('data/afk3.png')
    run = pygame.image.load('data/run.png')
    run2 = pygame.image.load('data/run2.png')

    def __init__(self, x, y):
        super().__init__()
        self.size = (55, 85)

        self.image = pygame.transform.scale(Player.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.old_x = self.rect.x
        self.old_y = self.rect.y

        self.direction = True
        self.speed = 4
        self.hp = 100

        self.afk_update_time = 0
        self.direction_update_time = 0

    def update(self):
        if self.old_x == self.rect.x and self.old_y == self.rect.y:
            self.afk_update_time += 1
            if self.direction:
                if self.afk_update_time == 1:
                    self.image = pygame.transform.scale(Player.image2, self.size)
                if self.afk_update_time == 20:
                    self.image = pygame.transform.scale(Player.image, self.size)
                if self.afk_update_time == 40:
                    self.image = pygame.transform.scale(Player.image3, self.size)
                if self.afk_update_time == 60:
                    self.image = pygame.transform.scale(Player.image, self.size)
                    self.afk_update_time = 0
            else:
                if self.afk_update_time == 1:
                    self.image = pygame.transform.flip(pygame.transform.scale(Player.image2, self.size), True, False)
                if self.afk_update_time == 20:
                    self.image = pygame.transform.flip(pygame.transform.scale(Player.image, self.size), True, False)
                if self.afk_update_time == 40:
                    self.image = pygame.transform.flip(pygame.transform.scale(Player.image3, self.size), True, False)
                if self.afk_update_time == 60:
                    self.image = pygame.transform.flip(pygame.transform.scale(Player.image, self.size), True, False)
                    self.afk_update_time = 0
        else:
            self.afk_update_time = 0
            self.direction_update_time += 1
            if self.direction:
                if self.direction_update_time == 1:
                    self.image = pygame.transform.scale(Player.run, self.size)
                if self.direction_update_time == 20:
                    self.image = pygame.transform.scale(Player.run2, self.size)
                if self.direction_update_time == 40:
                    self.image = pygame.transform.scale(Player.image, self.size)
                if self.direction_update_time == 60:
                    self.image = pygame.transform.scale(Player.run2, self.size)
                    self.direction_update_time = 0
            else:
                if self.direction_update_time == 1:
                    self.image = pygame.transform.flip(pygame.transform.scale(Player.run, self.size), True, False)
                if self.direction_update_time == 20:
                    self.image = pygame.transform.flip(pygame.transform.scale(Player.run2, self.size), True, False)
                if self.direction_update_time == 40:
                    self.image = pygame.transform.flip(pygame.transform.scale(Player.image, self.size), True, False)
                if self.direction_update_time == 60:
                    self.image = pygame.transform.flip(pygame.transform.scale(Player.run2, self.size), True, False)
                    self.direction_update_time = 0

        self.old_x = self.rect.x
        self.old_y = self.rect.y
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, coord, key):
        if coord == 'x':
            if key == pygame.K_a and not pygame.sprite.collide_mask(self, border3):
                self.rect.x -= self.speed
                self.direction = False
            if key == pygame.K_d and not pygame.sprite.collide_mask(self, border4):
                self.rect.x += self.speed
                self.direction = True


class Enemy:
    def __init__(self, x, y, hp=10):
        super().__init__()
        self.x = x
        self.y = y
        self.hp = hp


class Block:
    def __init__(self, x, y, enemy=False):
        super().__init__()
        self.x = x
        self.y = y
        self.enemy = enemy


if __name__ == '__main__':
    size = width, height = 1485, 850
    screen = pygame.display.set_mode(size)
    fps = 60
    clock = pygame.time.Clock()

    player = Player(10, 400)

    border1 = Border(0, 0, width, 0)
    border2 = Border(0, height, width, height)
    border3 = Border(0, 0, 0, height)
    border4 = Border(width, 0, width, height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.key.get_pressed()[pygame.K_a]:
            player.move('x', pygame.K_a)
        if pygame.key.get_pressed()[pygame.K_d]:
            player.move('x', pygame.K_d)

        # if pygame.key.get_pressed()[pygame.K_SPACE]:
        #     pass
        screen.fill((107, 102, 176))

        player.update()

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
