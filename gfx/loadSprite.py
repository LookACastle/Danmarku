import pygame
import re
from constants import *

class Sprites(pygame.sprite.Sprite):

    def __init__(self, x, y, array, imageType, image):
        self.x = x
        self.y = y
        self.object = array[imageType][image]
        self.spriteheight = self.object.get_height()
        self.spritewidth = self.object.get_width()
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(self.x, self.y, self.spritewidth, self.spriteheight)
        self.mask = pygame.mask.from_surface(self.object)
		
    def render_Sprites(self, window):
        window.blit(self.object, (self.x - self.spriteheight/2, self.y - self.spritewidth/2))