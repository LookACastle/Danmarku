import pygame, sys
from constants import *
from gfx.loadSprite import Sprites
from gfx.loadAllSprites import load_Sprites

pygame.init()
MONITOR_INFO = pygame.display.Info()
WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

loaded_Sprites = [[], [], []]

load_Sprites(loaded_Sprites)

test = None
test2 = None

#Input handling
def keyboard(event):
	global WINDOW
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_w]: #test
		WINDOW.fill(WHITE)
	if pressed[pygame.K_p]: #test
		WINDOW.fill(PASTEL_PINK)
	if pressed[pygame.K_x]: #test
		global test, test2
		test = Sprites(int(MONITOR_INFO.current_w/2), int(MONITOR_INFO.current_h/2), loaded_Sprites, PLAYERSPRITESARRAY, ON_PLANE)
		test.render_Sprites(WINDOW)
		test2 = Sprites(int(MONITOR_INFO.current_w/2) + 130, int(MONITOR_INFO.current_h/2) + 130, loaded_Sprites, ENEMYSPRITESARRAY, PURPLE_CIRCLE)
		test2.render_Sprites(WINDOW)
		#pygame.draw.circle(WINDOW,PASTEL_PINK,(int(MONITOR_INFO.current_w/2), int(MONITOR_INFO.current_h/2)), 100, 9)
	if pressed[pygame.K_z]:
		test2 = Sprites(int(MONITOR_INFO.current_w/2), int(MONITOR_INFO.current_h/2), loaded_Sprites, ENEMYSPRITESARRAY, PURPLE_CIRCLE)
		test2.render_Sprites(WINDOW)
	if pressed[pygame.K_ESCAPE]:
		pygame.quit()
		sys.exit()
	else:
		pass



while True:
	keyboard(pygame.event.get(pygame.KEYDOWN))
	
	if test is not None and test2 is not None:
		if pygame.sprite.collide_mask(test, test2):
			print("COLLISION")
		else:
			print("no collision :(")
	
	pygame.display.update()