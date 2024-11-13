import pygame
from pygame.locals import *
from Sprite import *
from math import *

class Stone(pygame.sprite.Sprite):
    def __init__(self, spawn_point, y):
        super().__init__()
        self.vx = 1
        self.vy = 0
        self.is_destroy = False
        self.image = stone_image 
        self.rect = self.image.get_rect()
        self.rect.x = spawn_point * (600 - stone_height)
        self.rect.y = y
        self.right_facing = True
        self.ax = 0  # X 이동에 가속도가 붙지 않음
        self.ay = 0.05
    
    def move(self):
        # 수직 가속도 적용
        self.vy += self.ay
        self.rect.y += self.vy

        # 수평 이동 방향에 따른 위치 업데이트
        if self.right_facing:
            self.rect.x += self.vx
        else:
            self.rect.x -= self.vx

    def update(self):
        self.move()

        if self.rect.y <= 0:
            self.rect.y = 0

        # 바닥에 도달했을 때 수직 속도 반전 및 위치 조정
        if self.rect.y >= 352:
            self.rect.y = 352
            self.vy = -self.vy

        # 화면 좌우 경계에서 이동 방향 반전
        if self.rect.x <= 0:
            self.rect.x = 0  
            self.right_facing = True
        elif self.rect.x >= 544:
            self.rect.x = 544  
            self.right_facing = False
            
