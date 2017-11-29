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
        self.rect = pygame.Rect(self.x-65, self.y-65, 130, 130)
        self.mask = pygame.mask.from_surface(self.player)

    def movement(self, event, width, height):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            if (self.y >= 64):
                self.y -= 1
                self.rect = pygame.Rect(self.x-65, self.y-65, 130, 130)
        if pressed[pygame.K_s]:
            if (self.y <= height - 64):
                self.y += 1
                self.rect = pygame.Rect(self.x-65, self.y-65, 130, 130)
        if pressed[pygame.K_a]:
            if (self.x >= 64):
                self.x -= 1
                self.rect = pygame.Rect(self.x-65, self.y-65, 130, 130)
        if pressed[pygame.K_d]:
            if (self.x <= width - 64):
                self.x += 1
                self.rect = pygame.Rect(self.x-65, self.y-65, 130, 130)
    
    def render(self, window):
        window.blit(self.player, (self.x - 64, self.y - 64))
