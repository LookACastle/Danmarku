import pygame
from constants import *
from gfx.loadSprite import Sprites
from entities.player_projectile import Player_Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, array, window, objectsArray):
        self.x = x
        self.y = y
        self.t = 0
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
            if (self.t == 15 or self.t == 30 or self.t == 45 or self.t==60):
                bullet = Player_Projectile(self.x, self.y+PLAYER_PROJECTILE_SPEED, self.array, self.window)
                self.objectsArray.append(bullet)
                if (self.t == 60):
                    self.t = 0
            self.t += 1
    def render(self, window):
        window.blit(self.player, (self.x - 64, self.y - 64))

    def getPos(self):
        return [self.x, self.y]
