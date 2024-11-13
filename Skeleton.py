import pygame
from pygame.locals import *
from Sprite import *

skeleton_vx = .2

class Skeleton(pygame.sprite.Sprite):
    def __init__(self, spawn_point): #spawn_point는 0또는 1로, 0일 경우 왼쪽에서 스폰한다. 반대의 경우에는 오른쪽에서 스폰
        self.facing_right = True
        self.is_death = False
        self.is_use_shield = False
        self.spawn_point = spawn_point
        self.is_hit = False
        self.state = 'WALK'
        self.image = skeleton_walk_frames[0]
        self.rect = self.image.get_rect()
        self.index_walk = 0
        self.index_death = 0
        self.time_shield = 0
        self.rect.x = spawn_point * (600 - enemy_frame_width)
        self.rect.y = 334
        self.x = self.rect.x
        self.y = self.rect.y

    def move(self):
        if self.state != 'DEATH' and self.state != 'SHIELD':
            if self.spawn_point == 0:
                self.x += skeleton_vx
            else :
                self.facing_right = False
                self.x -= skeleton_vx

    def update(self):
        self.move()
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        if self.is_hit == True:
            if not self.is_use_shield :
                self.state = 'SHIELD'
            else :
                self.state = 'DEATH'


        if self.state == 'WALK':
            if self.facing_right :
                self.image = skeleton_walk_frames[int(self.index_walk % 4)]
                self.index_walk+=.05
            else:
                self.image = skeleton_walk_frames_flipped[int(self.index_walk % 4)]
                self.index_walk+=.05
        
        elif self.state == 'DEATH':

            if self.index_death >= 60:
                self.index_death = 0
                self.is_death = True

            elif self.facing_right :
                self.image = skeleton_death_frames[self.index_death // 15]
                self.index_death += 1
            else:
                self.image = skeleton_death_frames_flipped[self.index_death // 15]
                self.index_death += 1

        elif self.state == "SHIELD" :
            if self.time_shield >= 120 :
                self.is_hit = False
                self.is_use_shield = True
                self.state = 'WALK'
            
            elif self.facing_right :
                self.image = skeleton_shield_frames[0]
            else:
                self.image = skeleton_shield_frames_flipped[0]
            self.time_shield += 1