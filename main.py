import pygame, sys
from constants import *
from gfx.loadSprite import Sprites
from gfx.loadAllSprites import load_Sprites

pygame.init()
MONITOR_INFO = pygame.display.Info()
WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
keyboard_event = False

loaded_Sprites = [[], [], []]

load_Sprites(loaded_Sprites)

test = None
test2 = None

#Input handling
def keyboard(event):
	global WINDOW
	global test, test2
	if event.key == pygame.K_w: #test
		WINDOW.fill(WHITE)
	if event.key == pygame.K_p: #test
		WINDOW.fill(PASTEL_PINK)
		test.move(2, 2, WINDOW)
		test2.move(-2, -2, WINDOW)
	if event.key == pygame.K_x: #test
		test = Sprites(int(MONITOR_INFO.current_w/2), int(MONITOR_INFO.current_h/2), loaded_Sprites, PLAYERSPRITESARRAY, ON_PLANE)
		test.render_Sprites(WINDOW)
		test2 = Sprites(int(MONITOR_INFO.current_w/2) + 130, int(MONITOR_INFO.current_h/2) + 130, loaded_Sprites, ENEMYSPRITESARRAY, PURPLE_CIRCLE)
		test2.render_Sprites(WINDOW)
		#pygame.draw.circle(WINDOW,PASTEL_PINK,(int(MONITOR_INFO.current_w/2), int(MONITOR_INFO.current_h/2)), 100, 9)
	if event.key == pygame.K_z:
		test2 = Sprites(int(MONITOR_INFO.current_w/2), int(MONITOR_INFO.current_h/2), loaded_Sprites, ENEMYSPRITESARRAY, PURPLE_CIRCLE)
		test2.render_Sprites(WINDOW)
	if event.key == pygame.K_ESCAPE:
		pygame.quit()
		sys.exit()



while True:
	if pygame.KEYDOWN:
		keyboard_event = True
	elif pygame.KEYUP:
		keyboard_event = False
		

	for event in pygame.event.get():
		if keyboard_event:
			keyboard(event)
	
	if test is not None and test2 is not None:
		if pygame.sprite.collide_mask(test, test2):
			print("COLLISION")
		else:
			print("no collision :(")
	
	pygame.display.update()