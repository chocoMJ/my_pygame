import pygame
import Player
from pygame.locals import *
from Sprite import *

class Fireball(pygame.sprite.Sprite) :
    def __init__(self, x, y):
        self.state = 'FIRE'
        self.image = fireball_frames[0]
        self.rect = self.image.get_rect(center = (x,y))
        self.is_destroy = False
        self.index_FIRE = 0
        self.index_BOOM = 0
        self.radius = 32 #실제 image의 크기보다는 radius를 다소 작게 설정
        self.vy = 4

    def move(self):
        if self.state == 'FIRE':
            self.rect.y -= self.vy

    def update(self):
        self.move()

        if self.rect.y <= 0 :
            self.state = 'BOOM'

        if self.state == 'FIRE' :
            self.image = fireball_frames[self.index_FIRE % 5]
            self.index_FIRE += 1

        else :
            if self.index_BOOM >= 30 :
                self.is_destroy = True
            else :
                self.image = fireball_boom_frames[int(self.index_BOOM // 10)]
                self.index_BOOM += 1

