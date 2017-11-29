import pygame
import re
from constants import *

class Sprites(pygame.sprite.Sprite):

    def __init__(self, x, y, array, imageType, image):
        self.x = x
        self.y = y
        self.array = array
        self.imageType = imageType
        self.image = image
        self.object = self.array[self.imageType][self.image].copy()
        self.spriteheight = self.object.get_height()
        self.spritewidth = self.object.get_width()
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(self.x-self.spritewidth/2-1, self.y-self.spriteheight/2-1, self.spritewidth+2, self.spriteheight+2)
        self.mask = pygame.mask.from_surface(self.object)
		
    def render(self, window):
        window.blit(self.object, (self.x - self.spriteheight/2, self.y - self.spritewidth/2))

    def move(self, vx, vy, window):
        self.x += vx
        self.y += vy
        self.rect = pygame.Rect(self.x-self.spritewidth/2-1, self.y-self.spriteheight/2-1, self.spritewidth+2, self.spriteheight+2)