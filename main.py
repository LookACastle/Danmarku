import pygame, sys
from constants import *

pygame.init()

window = pygame.display.set_mode((1920,1080))

window.fill((PASTEL_PINK))

pygame.display.update()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()