import pygame
from pygame.locals import *
from Sprite import *

max_vx = 4

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.facing_right = True
        self.is_attack = False
        self.is_death = False
        self.index_attack = 0
        self.index_walk = 0
        self.index_death = 0
        self.state = 'IDLE'
        self.image = idle_frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = 272
        self.rect.y = 328
        self.vx = 0
        self.ax = 0.35
        self.fireball_cooldown = 0
        self.is_use_fireball = False

    def move(self, keys):
        if self.is_attack or self.state == 'DEATH':
            self.vx = 0

        elif keys[pygame.K_LEFT]:
            self.facing_right = False

            if self.vx > 0 :
                self.vx -= self.ax
            else:
                if self.vx > (max_vx * -1) :
                    self.vx -= self.ax
                    if self.vx > -0.5 :
                        self.vx = -0.5
                elif self.vx < (max_vx * -1):
                    self.vx = max_vx * -1

        elif keys[pygame.K_RIGHT]:
            self.facing_right = True

            if self.vx < 0 :
                self.vx += self.ax
            else:
                if self.vx < max_vx :
                    self.vx += self.ax
                    if self.vx < 0.5 :
                        self.vx = 0.5
                elif self.vx > max_vx:
                    self.vx = max_vx
        
        else :#If no key is pressed, it slowly slides to a stop.
            if self.facing_right:
                if self.vx > 0 :
                    self.vx -= self.ax
                else:
                    self.vx = 0
            else:
                if self.vx < 0:
                    self.vx += self.ax
                else :
                    self.vx = 0

    def attack(self, keys):
        if keys[K_SPACE]:
            if self.is_attack : pass #공격하고 있으면 그냥 pass
            elif self.state != 'DEATH' :
                self.is_attack = True
                self.state = 'ATTACK'

    def magic(self, keys):
        if keys[K_UP] :
            if self.fireball_cooldown > 0 : pass
            elif self.state != 'DEATH' and self.state != 'ATTACK' :
                self.fireball_cooldown = 120
                self.is_use_fireball = True



    def update(self):
        keys = pygame.key.get_pressed()

        self.move(keys)
        self.attack(keys)
        self.magic(keys)

        if self.fireball_cooldown > 0 :
            self.fireball_cooldown -= 1

        if self.state == 'DEATH':
            if self.index_death == 120 :
                self.index_death = 0
                self.is_death = True
            
            if self.facing_right == True:
                self.image = death_frames[int(self.index_death // 10)]
                self.index_death += 1
            else :
                self.image = death_frames_flipped[int(self.index_death // 10)]
                self.index_death += 1
            
        if self.state == 'ATTACK' :
            if self.index_attack == 30 :
                self.is_attack = False
                self.index_attack = 0
                self.state = 'IDLE'

            if self.facing_right == True:
                self.image = attack_frames[self.index_attack // 5]
                self.index_attack += 1
            else :
                self.image = attack_frames_flipped[self.index_attack // 5]
                self.index_attack += 1

        elif self.state == 'IDLE':
            if self.vx != 0 and not self.is_attack :
                self.state = "WALK"

            if self.facing_right == True:
                self.image = idle_frames[0]
            else :
                self.image = idle_frames_flipped[0]

        elif self.state == 'WALK':
            if self.vx == 0 and not self.is_attack :
                self.state = 'IDLE'

            if self.facing_right == True:
                self.image = walk_frames[int((self.index_walk % 8))]
                self.index_walk+=0.5
            else :
                self.image = walk_frames_flipped[int((self.index_walk % 8))]
                self.index_walk+=0.5

        
        self.rect.x += self.vx

        if self.rect.x < 0 :
            self.rect.x = 0
        
        if self.rect.x > (600 - player_frame_width) :
            self.rect.x = (600 - player_frame_width)
        

