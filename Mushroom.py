import pygame
from pygame.locals import *
from Sprite import *


mushroom_vx = .4

class Mushroom(pygame.sprite.Sprite):
    def __init__(self, spawn_point): #spawn_point는 0또는 1로, 0일 경우 왼쪽에서 스폰한다. 반대의 경우에는 오른쪽에서 스폰
        self.facing_right = True
        self.is_death = False
        self.is_hit = False
        self.spawn_point = spawn_point
        self.state = 'WALK'
        self.image = mushroom_walk_frames[0]
        self.rect = self.image.get_rect()
        self.index_walk = 0
        self.index_death = 0
        self.rect.x = spawn_point * (600 - enemy_frame_width)
        self.rect.y = 334
        self.x = self.rect.x
        self.y = self.rect.y

    def move(self):
        if self.state != 'DEATH':
            if self.spawn_point == 0:
                self.x += mushroom_vx
            else :
                self.facing_right = False
                self.x -= mushroom_vx

    def update(self):
        self.move()
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        if self.is_hit:
            self.state = 'DEATH'

        if self.state == 'WALK':
            if self.facing_right :
                self.image = mushroom_walk_frames[int(self.index_walk % 8)]
                self.index_walk+=.2
            else:
                self.image = mushroom_walk_frames_flipped[int(self.index_walk % 8)]
                self.index_walk+=.2
        
        elif self.state == 'DEATH':

            if self.index_death >= 60:
                self.index_death = 0
                self.is_death = True

            elif self.facing_right :
                self.image = mushroom_death_frames[self.index_death // 15]
                self.index_death += 1
            else:
                self.image = mushroom_death_frames_flipped[self.index_death // 15]
                self.index_death += 1
