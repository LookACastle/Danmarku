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


StartBulletShower(64,19,100,16, WINDOW, loaded_Sprites, renderBullets)

test = Player(int(window_w/2), int(window_h/2), loaded_Sprites, WINDOW)
test2 = Sprites(int(window_w/2) + 130, int(window_h/2) + 130, loaded_Sprites, ENEMYSPRITESARRAY, PURPLE_CIRCLE)
test3 = Sprites(int(window_w/2), int(window_h/2), loaded_Sprites, ENEMYSPRITESARRAY, PURPLE_CIRCLE)
render_objects.append(test)
render_objects.append(test2)
render_objects.append(test3)

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
	'''if test is not None and test2 is not None:
		if pygame.sprite.collide_mask(test, test2):
			print("COLLISION")
		else:
			print("no collision :(")'''
	
	pop = 0
	i = 0
	while (i < len(renderBullets) - pop):
		renderBullets[i].move(window_w, window_h)
		renderBullets[i].render(WINDOW)
		pos = renderBullets[i].getpos()
		if (pos[1] < -128 or pos[1] > window_h + 128 or pos[0] < 0 - 128 or pos[0] > window_w + 128):
			renderBullets.pop(i)
			i = i - 1
			pop += 1
		i += 1
	render(render_objects, WINDOW)
	pygame.display.update(render_objects)
	pygame.display.update(renderBullets)