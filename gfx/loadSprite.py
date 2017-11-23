import pygame
import re
from constants import *

class Sprites(pygame.sprite.Sprite):

    def __init__(self, x, y, path, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.image = pygame.image.load("sprites/" + path + "/" + sprite + ".png").convert_alpha()
        self.spriteheight = self.image.get_height()
        self.spritewidth = self.image.get_width()
        
    def render(self, window):
        window.blit(self.image, (self.x - self.spriteheight/2, self.y - self.spritewidth/2))