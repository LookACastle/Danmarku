import pygame, sys, time, math
from constants import *
from gfx.loadSprite import Sprites
from gfx.loadAllSprites import load_Sprites
from entities.player import Player
from gfx.render import *
from bullets import *

pygame.init()
global test, test2, WINDOW
MONITOR_INFO = pygame.display.Info()
if MONITOR_INFO.current_h >= 1080 and MONITOR_INFO.current_w >= 1920:
	WINDOW = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
else:
	WINDOW = pygame.display.set_mode((MONITOR_INFO.current_w, MONITOR_INFO.current_h), pygame.FULLSCREEN)
loaded_Sprites = [[], [], []]
render_objects = []
renderBullets = []
load_Sprites(loaded_Sprites)
clock = pygame.time.Clock()
window_w, window_h = pygame.display.get_surface().get_size()

test = Player(int(window_w/2), int(window_h/2), loaded_Sprites, WINDOW)
test2 = Sprites(int(window_w/2) + 130, int(window_h/2) + 130, loaded_Sprites, ENEMYSPRITESARRAY, PURPLE_CIRCLE)
test3 = Sprites(int(window_w/2), int(window_h/2), loaded_Sprites, ENEMYSPRITESARRAY, PURPLE_CIRCLE)
render_objects.append(test)
render_objects.append(test2)
render_objects.append(test3)

StartBulletShower(0,30,50,15, WINDOW, loaded_Sprites, renderBullets)

#Input handling
def keyboard(event):
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_p]: #test
		test2.move(-2, -2, WINDOW)	
	if pressed[pygame.K_ESCAPE]:
		pygame.quit()
		sys.exit()
	else:
		pass


start_time = time.time()
framecount = 0
while True:
	clock.tick(MAX_FPS)
	framecount+=1 
	if (time.time()-start_time >= 1):
		print("FPS:"+ str(math.floor(framecount/(time.time()-start_time))))
		framecount = 0
		start_time = time.time()
	keyboard(pygame.event.get(pygame.KEYDOWN))
	test.movement(pygame.event.get(pygame.KEYDOWN), window_w, window_h)
	render(render_objects, WINDOW)
	'''if test is not None and test2 is not None:
		if pygame.sprite.collide_mask(test, test2):
			print("COLLISION")
		else:
			print("no collision :(")'''
	pygame.display.update(render_objects)
	for i in range(len(renderBullets)):
		renderBullets[i].move(window_w, window_h)
	pygame.display.update(renderBullets)