import pygame, sys
from constants import *

pygame.init()
window = pygame.display.set_mode((1280,720))

#Input handling
def keyboard(event):
	global window
	if event.key == pygame.K_w: #test
		window.fill(WHITE)
	if event.key == pygame.K_p: #test
		window.fill(PASTEL_PINK)
	if event.key == pygame.K_ESCAPE:
		pygame.quit()
		sys.exit()



while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			keyboard(event)
			
	pygame.display.update()