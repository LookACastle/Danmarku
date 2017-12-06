import pygame
from constants import *
from gfx.loadSprite import Sprites

class Health(pygame.sprite.Sprite):
    def __init__(self, health, x, y, array, window):
        self.x = x
        self.y = y
        self.array = array
        self.window = window
        self.object = self.array[PLAYERSPRITESARRAY][HEART].copy()
        pygame.sprite.Sprite.__init__(self)
    
    def render(self, window):
        window.blit(self.object, (self.x - 16, self.y - 16))