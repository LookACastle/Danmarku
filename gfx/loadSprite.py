import pygame
import re
from constants import *

class Sprites(pygame.sprite.Sprite):

    def __init__(self, x, y, array, imageType, image):
        self.x = x
        self.y = y
        self.imageType = imageType
        self.image = image
        self.object = array[self.imageType][self.image]
        self.spriteheight = self.object.get_height()
        self.spritewidth = self.object.get_width()
            
    def render_Sprites(self, window):
        window.blit(self.object, (self.x - self.spriteheight/2, self.y - self.spritewidth/2))