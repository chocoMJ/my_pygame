import pygame
from pygame.locals import *
from Sprite import *
from math import *

flying_eye_vx = .7

class Flying_eye(pygame.sprite.Sprite):
    def __init__(self, spawn_point): #spawn_point는 0또는 1로, 0일 경우 왼쪽에서 스폰한다. 반대의 경우에는 오른쪽에서 스폰
        self.facing_right = True
        self.is_death = False
        self.spawn_point = spawn_point
        self.is_hit = False
        self.state = 'FLIGHT'
        self.image = Flying_eye_Flight_frames[0]
        self.rect = self.image.get_rect()
        self.index_flight = 0
        self.index_death = 0
        self.rect.x = spawn_point * (600 - enemy_frame_width)
        self.rect.y = 234
        self.amplitude = 100  # 코사인 파동의 진폭
        self.frequency = 0.05  # 파동의 빈도 (주기 조절)
        self.time = 0
        self.x = self.rect.x
        self.y = self.rect.y #소수점 문제 해결을 위해.

    def move(self):
        if self.state != 'DEATH':
            self.y = 234 + self.amplitude * cos(self.frequency * self.time)
            self.time+=1

            if self.spawn_point == 0:
                self.x += flying_eye_vx
            else :
                self.facing_right = False
                self.x -= flying_eye_vx

    def update(self):
        self.move()
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        if self.is_hit:
            self.state = 'DEATH'

        if self.state == 'FLIGHT':
            if self.facing_right :
                self.image = Flying_eye_Flight_frames[int(self.index_flight % 8)]
                self.index_flight+=.5
            else:
                self.image = Flying_eye_Flight_frames_flipped[int(self.index_flight % 8)]
                self.index_flight+=.5
        
        elif self.state == 'DEATH':

            if self.index_death >= 60:
                self.index_death = 0
                self.is_death = True

            elif self.facing_right :
                self.image = Flying_eye_Death_frames[self.index_death // 15]
                self.index_death += 1
            else:
                self.image = Flying_eye_Death_frames_flipped[self.index_death // 15]
                self.index_death += 1