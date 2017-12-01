import pygame
from constants import *

class Player_Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, array, window):
        self.x = x
        self.y = y
        self.array = array
        self.window = window
        self.bullet = self.array[PLAYERSPRITESARRAY][PLAYER_PROJECTILE].copy()
        pygame.sprite.Sprite.__init__(self)
        self.mask = pygame.mask.from_surface(self.bullet)
        self.speed = PLAYER_PROJECTILE_SPEED
        self.rect = pygame.Rect(self.x - (64 + self.speed), self.y - (64 + self.speed), 128 + self.speed*2, 128 + self.speed*2)

    def move(self, width, height):
        if (self.y >= -128):
            self.y -= self.speed
            self.rect = pygame.Rect(self.x - (91 + self.speed*2), self.y - (91 + self.speed*2), 182 + self.speed*2, 182 + self.speed*2)
            return False
        else:
            return True

    def render(self, window):
        window.blit(self.bullet, (self.x - 64, self.y - 64))