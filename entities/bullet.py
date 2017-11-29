import pygame
from constants import *
from gfx.loadSprite import Sprites

class bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy, array, window):
        self.x = x
        self.y = y
        self.array = array
        self.window = window
        self.bullet = self.array[ENEMYSPRITESARRAY][BLUE_LASER]
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(self.x, self.y, 128, 128)
        self.mask = pygame.mask.from_surface(self.player)

    def move(self, width, height):
	if (self.y < 0 OR self.y > height OR self.x < 0 OR self.x > width):
		self.y += vy
		self.x += vx
		self.bullet = self.array[ENEMYSPRITESARRAY][BLUE_LASER]
	        pygame.sprite.Sprite.__init__(self)
        	self.rect = pygame.Rect(self.x, self.y, 128, 128)
	        self.mask = pygame.mask.from_surface(self.bullet)

    def render(self, window):
        window.blit(self.player, (self.x - 64, self.y - 64))