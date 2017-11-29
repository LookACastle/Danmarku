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
		self.rect = pygame.Rect(self.x - (64 + self.vx), self.y - (64 + self.vy), 128 + self.vx*2, 128 + self.vy*2)
		self.mask = pygame.mask.from_surface(self.bullet)

	def move(self, width, height):
		if (self.y >= -128 and self.y <= height+128 and self.x >= -128 and self.x <= width+128):
			self.y += self.vy
			self.x += self.vx
			self.rect = pygame.Rect(self.x - (64 + self.vx), self.y - (64 + self.vy), 128 + self.vx*2, 128 + self.vy*2)
			return False
		else:
			return True

	def render(self, window):
		window.blit(self.bullet, (self.x - 64, self.y - 64))

	def rotate(self, angle):
		self.bullet = pygame.transform.rotate(self.bullet, angle)