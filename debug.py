import pygame as pg
from random import randint as ri
import time

# constants
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# classes
class Shape(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface([40, 40])
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.centerx, self.rect.centery = pg.mouse.get_pos()
    
class Player1(Shape):
    def __init__(self):
        super().__init__()
        self.image.fill(WHITE)

    def hit_enemy(self, sprite):
        return self.rect.colliderect(sprite.rect)

class Enemy(Shape):
    def __init__(self):
        super().__init__()
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(640//2, 640//2))

    def update(self, hit=False, direction=None):
        if hit:
            self.rect.centerx, self.rect.centery = pg.mouse.get_pos()
        else:
            self.rect.centerx, self.rect.centery = self.rect.centerx + direction[0], self.rect.centery + direction[1]

    def hit_wall(self):
        return True if not all([0 < i < 640 for i in [self.rect.left, self.rect.right, self.rect.top, self.rect.bottom]]) else False

pg.init()

p1 = Player1()
enemy = Enemy()
screen = pg.display.set_mode((640, 640))
all_sprites = pg.sprite.Group()
all_sprites.add([p1, enemy])
clock = pg.time.Clock()
score = 0
run = True
direction = (ri(-1, 1), ri(-1, 1))
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and p1.hit_enemy(enemy):
            score += 1
            enemy.update(hit=(ri(20, 620), ri(20, 620)))
            direction = (ri(-3, 3), ri(-3, 3))
    
    if enemy.hit_wall():
        print(score)
        break
    enemy.update(direction=direction)
    screen.fill(BLACK)
    p1.update()
    all_sprites.draw(screen)
    pg.display.flip()
    clock.tick(60)

pg.quit()