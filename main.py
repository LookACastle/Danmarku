import pygame, sys
from constants import *

pygame.init()
MONITOR_INFO = pygame.display.Info()
WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#Input handling
def keyboard(event):
	global WINDOW
	if event.key == pygame.K_w: #test
		WINDOW.fill(WHITE)
	if event.key == pygame.K_p: #test
		WINDOW.fill(PASTEL_PINK)
	if event.key == pygame.K_x: #test
		pygame.draw.circle(WINDOW,PASTEL_PINK,(int(MONITOR_INFO.current_w/2), int(MONITOR_INFO.current_h/2)), 100, 9)
	if event.key == pygame.K_ESCAPE:
		pygame.quit()
		sys.exit()



while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			keyboard(event)
			
	pygame.display.update()