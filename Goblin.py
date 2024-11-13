import pygame
from pygame.locals import *
from Sprite import *

Goblin_vx = 1

class Goblin(pygame.sprite.Sprite):
    def __init__(self, spawn_point): #spawn_point는 0또는 1로, 0일 경우 왼쪽에서 스폰한다. 반대의 경우에는 오른쪽에서 스폰
        self.facing_right = True
        self.is_death = False
        self.spawn_point = spawn_point
        self.is_hit = False
        self.state = 'RUN'
        self.image = Goblin_Run_frames[0]
        self.rect = self.image.get_rect()
        self.index_Run = 0
        self.index_death = 0
        self.rect.x = spawn_point * (600 - enemy_frame_width)
        self.rect.y = 334

    def move(self):
        if self.state != 'DEATH':
            if self.spawn_point == 0:
                self.rect.x += Goblin_vx
            else :
                self.facing_right = False
                self.rect.x -= Goblin_vx

    def update(self):
        self.move()

        if self.is_hit:
            self.state = 'DEATH'
            
        if self.state == 'RUN':
            if self.facing_right :
                self.image = Goblin_Run_frames[int(self.index_Run % 8)]
                self.index_Run+=.4
            else:
                self.image = Goblin_Run_frames_flipped[int(self.index_Run % 8)]
                self.index_Run+=.4
        
        elif self.state == 'DEATH':

            if self.index_death >= 32:
                self.index_death = 0
                self.is_death = True

            elif self.facing_right :
                self.image = Goblin_Death_frames[self.index_death // 8]
                self.index_death += 1
            else:
                self.image = Goblin_Death_frames_flipped[self.index_death // 8]
                self.index_death += 1