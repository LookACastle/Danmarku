import pygame, sys
from constants import *
from gfx.loadSprite import Sprites
from gfx.loadAllSprites import load_Sprites
from entities.player import Player

pygame.init()
MONITOR_INFO = pygame.display.Info()
WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

loaded_Sprites = [[], [], []]

load_Sprites(loaded_Sprites)

test = Player(int(MONITOR_INFO.current_w/2), int(MONITOR_INFO.current_h/2), loaded_Sprites, WINDOW)
test.render_player()
test2 = None

#Input handling
def keyboard(event):
	global WINDOW
	pressed = pygame.key.get_pressed()
	global test, test2
	if pressed[pygame.K_q]: #test
		WINDOW.fill(WHITE)
	if pressed[pygame.K_p]: #test
		WINDOW.fill(PASTEL_PINK)
		test2.move(-2, -2, WINDOW)
	if pressed[pygame.K_x]: #test
		test2 = Sprites(int(MONITOR_INFO.current_w/2) + 130, int(MONITOR_INFO.current_h/2) + 130, loaded_Sprites, ENEMYSPRITESARRAY, PURPLE_CIRCLE)
		test2.render_Sprites(WINDOW)
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
	test.movement(pygame.event.get(pygame.KEYDOWN), MONITOR_INFO.current_w, MONITOR_INFO.current_h)
	if test is not None and test2 is not None:
		if pygame.sprite.collide_mask(test, test2):
			print("COLLISION")
		else:
			print("no collision :(")
	
	pygame.display.update()