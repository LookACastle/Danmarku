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
        self.rect = self.bullet.get_rect(center=(self.x, self.y-8),width=(128),height=(30+self.speed*2))

    def move(self, width, height):
        if (self.y >= -128):
            self.y -= self.speed
            self.rect = self.bullet.get_rect(center=(self.x, self.y-8),width=(128),height=(30+self.speed*2))
            return False
        else:
            return True

    def render(self, window):
        window.blit(self.bullet, self.rect)