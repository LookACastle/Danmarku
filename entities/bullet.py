import pygame
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
		self.bullet = self.array[sprite].copy()
		pygame.sprite.Sprite.__init__(self)
		self.rect = pygame.Rect(self.x, self.y, 128, 128)
		self.mask = pygame.mask.from_surface(self.bullet)

	def move(self, width, height):
		if (self.y < 0 or self.y > height or self.x < 0 or self.x > width):
			self.y += self.vy
			self.x += self.vx
			self.bullet = self.array[self.sprite]
			pygame.sprite.Sprite.__init__(self)
			self.rect = pygame.Rect(self.x, self.y, 128, 128)
			self.mask = pygame.mask.from_surface(self.bullet)

	def render(self, window):
		window.blit(self.bullet, (self.x - 64, self.y - 64))