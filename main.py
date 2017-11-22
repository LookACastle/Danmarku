import pygame, sys
from constants import *

pygame.init()
WINDOW = pygame.display.set_mode((1280,720))

#Input handling
def keyboard(event):
	global WINDOW
	if event.key == pygame.K_w: #test
		WINDOW.fill(WHITE)
	if event.key == pygame.K_p: #test
		WINDOW.fill(PASTEL_PINK)
	if event.key == pygame.K_ESCAPE:
		pygame.quit()
		sys.exit()



while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			keyboard(event)
			
	pygame.display.update()