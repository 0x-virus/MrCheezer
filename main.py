import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    image = pygame.image.load('data/player.png')
    image2 = pygame.image.load('data/player_2.png')

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = pygame.transform.scale(Player.image, (65, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.old_x = self.rect.x
        self.old_y = self.rect.y

        self.speed = 5
        self.hp = 100

        self.update_time = 0

    def update(self):
        if self.old_x == self.rect.x and self.old_y == self.rect.y:
            self.update_time += 1
            if self.update_time == 20:
                self.image = pygame.transform.scale(Player.image2, (65, 100))
            if self.update_time == 40:
                self.image = pygame.transform.scale(Player.image, (65, 100))
                self.update_time = 0
        else:
            self.update_time = 0
            self.image = pygame.transform.scale(Player.image, (65, 100))

        self.old_x = self.rect.x
        self.old_y = self.rect.y


class Enemy:
    def __init__(self, x, y, hp=10):
        super().__init__(all_sprites)
        self.x = x
        self.y = y
        self.hp = hp


class Block:
    def __init__(self, x, y, enemy=False):
        super().__init__(all_sprites)
        self.x = x
        self.y = y
        self.enemy = enemy


if __name__ == '__main__':
    all_sprites = pygame.sprite.Group()

    size = width, height = 1300, 800
    screen = pygame.display.set_mode(size)
    fps = 60
    clock = pygame.time.Clock()

    player = Player(200, 200)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.key.get_pressed()[pygame.K_a]:
            player.rect.x -= player.speed
        if pygame.key.get_pressed()[pygame.K_d]:
            player.rect.x += player.speed
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            pass
        screen.fill((120, 116, 184))

        player.update()
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
