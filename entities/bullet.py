import pygame
from math import sqrt
from gfx.loadSprite import Sprites

class bullet(pygame.sprite.Sprite):
	def __init__(self, sprite, x, y, vx, vy, array, window):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.array = array
		self.sprite = sprite
		self.window = window
		#self.max_rect = sqrt(128**2*2) - Max size of rect where 128 is sprite width & height
		self.speed = sqrt(self.vx**2 + self.vy**2)
		self.bullet = self.array[sprite].copy()
		pygame.sprite.Sprite.__init__(self)
		self.rect = self.bullet.get_rect(center=(self.x, self.y),width=(190	+self.speed*2),height=(190+self.speed*2))
		#self.rect = pygame.Rect(self.x - (91 + self.speed*2), self.y - (91 + self.speed*2), 182 + self.speed*2, 182 + self.speed*2)
		self.mask = pygame.mask.from_surface(self.bullet)

	def move(self, width, height):
		if (self.y >= -128 and self.y <= height+128 and self.x >= -128 and self.x <= width+128):
			self.y += self.vy
			self.x += self.vx
			self.rect = self.bullet.get_rect(center=(self.x, self.y),width=(190),height=(190))
			#self.mask = pygame.mask.from_surface(self.bullet)
			#self.rect = pygame.Rect(self.x - (91 + self.speed*2), self.y - (91 + self.speed*2), 182 + self.speed*2, 182 + self.speed*2)
			return False
		else:
			return True

	def render(self, window):
		window.blit(self.bullet, self.rect)

	def rotate(self, angle):
		self.bullet = pygame.transform.rotate(self.bullet, angle)
		self.rect = self.bullet.get_rect(center=(self.x, self.y),width=(190),height=(190))
		self.mask = pygame.mask.from_surface(self.bullet)