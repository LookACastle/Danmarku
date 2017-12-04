import pygame
from constants import *
from gfx.loadSprite import Sprites
from entities.player_projectile import Player_Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, array, window, objectsArray):
        self.x = x
        self.y = y
        self.cd = 0
        self.shooting = False
        self.array = array
        self.window = window
        self.objectsArray = objectsArray
        self.player = self.array[PLAYERSPRITESARRAY][ON_PLANE].copy()
        pygame.sprite.Sprite.__init__(self)
        self.mask = pygame.mask.from_surface(self.player)
        self.speed = PLAYER_SPEED
        self.rect = pygame.Rect(self.x - (64 + self.speed), self.y - (64 + self.speed), 128 + self.speed*2, 128 + self.speed*2)
		
    def movement(self, event, width, height):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            if (self.y >= 64):
                self.y -= self.speed
                self.rect = pygame.Rect(self.x - (64 + self.speed), self.y - (64 + self.speed), 128 + self.speed*2, 128 + self.speed*2)
        if pressed[pygame.K_s]:
            if (self.y <= height - 64):
                self.y += self.speed
                self.rect = pygame.Rect(self.x - (64 + self.speed), self.y - (64 + self.speed), 128 + self.speed*2, 128 + self.speed*2)
        if pressed[pygame.K_a]:
            if (self.x >= 64):
                self.x -= self.speed
                self.rect = pygame.Rect(self.x - (64 + self.speed), self.y - (64 + self.speed), 128 + self.speed*2, 128 + self.speed*2)
        if pressed[pygame.K_d]:
            if (self.x <= width - 64):
                self.x += self.speed
                self.rect = pygame.Rect(self.x - (64 + self.speed), self.y - (64 + self.speed), 128 + self.speed*2, 128 + self.speed*2)
        if pressed[pygame.K_SPACE]:
            if (self.cd <= 0):
                self.shooting = True
                self.cd = 15
                bullet = Player_Projectile(self.x, self.y+PLAYER_PROJECTILE_SPEED, self.array, self.window)
                self.objectsArray.append(bullet)
                
            '''if (self.t == 1 or self.t == 16 or self.t == 31 or self.t == 46):
                self.player = self.array[PLAYERSPRITESARRAY][ON_PLANE_SHOOT1].copy()
            if (self.t == 2 or self.t == 17 or self.t == 32 or self.t == 47):
                self.player = self.array[PLAYERSPRITESARRAY][ON_PLANE_SHOOT2].copy()
            if (self.t == 4 or self.t == 19 or self.t == 34 or self.t == 49):
                self.player = self.array[PLAYERSPRITESARRAY][ON_PLANE_SHOOT3].copy()
            if (self.t == 6 or self.t == 21 or self.t == 36 or self.t == 51):
                self.player = self.array[PLAYERSPRITESARRAY][ON_PLANE_SHOOT4].copy()
            if (self.t == 8 or self.t == 23 or self.t == 38 or self.t == 53):
                self.player = self.array[PLAYERSPRITESARRAY][ON_PLANE].copy()
            if (self.t == 60):
                self.t = 0'''
        if (self.cd > 0):
            self.cd -= 1
        if (self.shooting == True):
            if (self.cd == 15):
                self.player = self.array[PLAYERSPRITESARRAY][ON_PLANE_SHOOT1].copy()
            if (self.cd == 13):
                self.player = self.array[PLAYERSPRITESARRAY][ON_PLANE_SHOOT2].copy()
            if (self.cd == 11):
                self.player = self.array[PLAYERSPRITESARRAY][ON_PLANE_SHOOT3].copy()
            if (self.cd == 9):
                self.player = self.array[PLAYERSPRITESARRAY][ON_PLANE_SHOOT4].copy()
            if (self.cd == 7):
                self.player = self.array[PLAYERSPRITESARRAY][ON_PLANE].copy()
                self.shooting = False
    def render(self, window):
        window.blit(self.player, (self.x - 64, self.y - 64))

    def getPos(self):
        return [self.x, self.y]
