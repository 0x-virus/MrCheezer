import pygame
import os
from pygame.locals import *
import random


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
        self.size = (75, 105)

        self.image = pygame.transform.scale(Player.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.old_x = self.rect.x
        self.old_y = self.rect.y

        self.direction = True
        self.jump = False
        self.in_air = False
        self.speed = 4
        self.fall_speed = 8
        self.hp = 5
        self.collect_coins = 0

        self.afk_update_time = 0
        self.direction_update_time = 0
        self.jump_update_time = 0

    def update(self):
        if pygame.sprite.spritecollideany(self, enemy_blocks):
            self.hp -= 1
            self.rect.x = spawn_coords[0]
            self.rect.y = spawn_coords[1]

        if pygame.sprite.spritecollide(self, coins, True):
            self.collect_coins += 1

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

        if not pygame.sprite.spritecollideany(self, blocks) and not self.jump and \
                not pygame.sprite.collide_mask(self, border2):
            self.rect.y += self.fall_speed
            self.in_air = True
            if pygame.sprite.spritecollideany(self, blocks) or pygame.sprite.collide_mask(self, border2):
                self.in_air = False
                self.rect.y -= self.fall_speed
        elif self.jump:
            self.jump_update_time += 1
            if self.jump_update_time == 20:
                self.jump = False
                self.jump_update_time = 0
            else:
                self.rect.y -= self.fall_speed
            self.in_air = True
            if pygame.sprite.spritecollideany(self, blocks):
                self.jump = False
                self.jump_update_time = 0
                self.rect.x = self.old_x
                self.rect.y = self.old_y
        else:
            self.in_air = False

        self.old_x = self.rect.x
        self.old_y = self.rect.y
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, coord, key):
        if coord == 'x':
            if key == pygame.K_a and not pygame.sprite.collide_mask(self, border3):
                self.rect.x -= self.speed
                self.direction = False
                if pygame.sprite.spritecollideany(self, blocks):
                    self.rect.y -= self.speed
                    if not pygame.sprite.spritecollideany(self, blocks):
                        self.rect.y += self.speed
                    else:
                        self.rect.y = self.old_y
                        self.rect.x = self.old_x
            if key == pygame.K_d and not pygame.sprite.collide_mask(self, border4):
                self.rect.x += self.speed
                self.direction = True
                if pygame.sprite.spritecollideany(self, blocks):
                    self.rect.y -= self.speed
                    if not pygame.sprite.spritecollideany(self, blocks):
                        self.rect.y += self.speed
                    else:
                        self.rect.y = self.old_y
                        self.rect.x = self.old_x


class Block(pygame.sprite.Sprite):
    image = pygame.image.load('data/block.png')

    def __init__(self, x, y):
        super().__init__(blocks)

        self.image = pygame.transform.scale(Block.image, (40, 40))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y


class Enemy_Block(pygame.sprite.Sprite):
    image = pygame.image.load('data/enemy_block.png')

    def __init__(self, x, y):
        super().__init__(enemy_blocks)

        self.image = pygame.transform.scale(Enemy_Block.image, (40, 20))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y + 20


class Coin(pygame.sprite.Sprite):
    image = pygame.image.load('data/coin.png')

    def __init__(self, x, y):
        super().__init__(coins)

        self.image = pygame.transform.scale(Coin.image, (20, 25))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y


class Portal(pygame.sprite.Sprite):
    image = pygame.image.load('')

    def __init__(self, x, y):
        super().__init__(coins)

        self.image = pygame.transform.scale(Coin.image, (20, 25))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y


def load_level(number):
    global player, spawn_coords
    if os.path.exists('levels/level_' + str(number) + '.txt'):
        file = open('levels/level_' + str(number) + '.txt')
        data = file.read()

        if len(data.split('\n')) != 21:
            return False
        else:
            for y, line in enumerate(data.split('\n')):
                if len(line) == 37:
                    for x, symbol in enumerate(line):
                        if symbol == 'x':
                            Block(x * 40, y * 40)
                        elif symbol == '@':
                            player = Player(x * 40, y * 40)
                            spawn_coords = [x * 40, y * 40]
                        elif symbol == 'o':
                            Enemy_Block(x * 40, y * 40)
                        elif symbol == '$':
                            Coin(x * 40, y * 40)


if __name__ == '__main__':
    size = width, height = 1480, 840
    screen = pygame.display.set_mode(size)
    fps = 120
    clock = pygame.time.Clock()
    pygame.font.init()
    font = pygame.font.Font(pygame.font.get_default_font(), 100)
    font2 = pygame.font.Font(pygame.font.get_default_font(), 30)

    blocks = pygame.sprite.Group()
    enemy_blocks = pygame.sprite.Group()
    coins = pygame.sprite.Group()

    border1 = Border(0, 0, width, 0)
    border2 = Border(0, height, width, height)
    border3 = Border(0, 0, 0, height)
    border4 = Border(width, 0, width, height)

    level = 1
    game_over = False
    spawn_coords = [0, 600]
    player = Player(0, 600)
    load_level(level)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.key.get_pressed()[pygame.K_a]:
            player.move('x', pygame.K_a)
        if pygame.key.get_pressed()[pygame.K_d]:
            player.move('x', pygame.K_d)
        if pygame.key.get_pressed()[pygame.K_SPACE] and not player.jump and not player.in_air:
            player.jump = True

        if not game_over:
            screen.fill((107, 102, 176))

            for i in range(5):
                if i < player.hp:
                    screen.blit(pygame.transform.scale(pygame.image.load('data/heart.png'), (50, 50)), (i * 50, 0))
                else:
                    screen.blit(pygame.transform.scale(pygame.image.load('data/empty_heart.png'), (50, 50)), (i*50, 0))

            screen.blit(pygame.transform.scale(pygame.image.load('data/coin.png'), (40, 50)), (350, 5))
            screen.blit(font2.render('x ' + str(player.collect_coins), True, pygame.Color('white')), (400, 20))

            blocks.draw(screen)
            enemy_blocks.draw(screen)
            coins.draw(screen)
            player.update()

            pygame.display.flip()

            if player.hp == 0:
                game_over = True

            clock.tick(fps)
            pygame.display.set_caption(str(int(clock.get_fps())))
        else:
            for i in range(5):
                image = pygame.transform.scale(pygame.image.load('data/empty_heart.png'), (50, 50))
                screen.blit(image, (i * 50, 0))

            text_surface = font.render('Game Over!!!', True, pygame.Color('white'))
            screen.blit(text_surface, (height // 2, height // 2))

            pygame.display.flip()

    pygame.quit()
