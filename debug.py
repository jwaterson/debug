import pygame as pg
from random import randint as ri
import time

# constants
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# classes
class Shape(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface([40, 40])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.centerx, self.rect.centery = pg.mouse.get_pos()
    
class Player1(Shape):
    def __init__(self):
        super().__init__()

    def hit_enemy(self, sprite):
        return self.rect.colliderect(sprite.rect)

class Enemy(Shape):
    def __init__(self):
        super().__init__()

    def update(self):
        self.rect.centerx, self.rect.centery = (ri(20, 620), ri(20, 620))

pg.init()

p1 = Player1()
enemy = Enemy()
screen = pg.display.set_mode((640, 640))
all_sprites = pg.sprite.Group()
all_sprites.add([p1, enemy])
clock = pg.time.Clock()
score = 0
run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and p1.hit_enemy(enemy):
            score += 1
            print(score)

    screen.fill(BLACK)
    p1.update()
    all_sprites.update()
    all_sprites.draw(screen)
    pg.display.flip()
    clock.tick(60)

pg.quit()