import pygame
from constants import *
from gfx.loadSprite import Sprites

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, array, window):
        self.x = x
        self.y = y
        self.array = array
        self.window = window
        self.player = self.array[PLAYERSPRITESARRAY][ON_PLANE].copy()
        pygame.sprite.Sprite.__init__(self)
        self.mask = pygame.mask.from_surface(self.player)
        self.speed = 7.5
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
    def render(self, window):
        window.blit(self.player, (self.x - 64, self.y - 64))

    def getPos(self):
        return [self.x, self.y]
