import pygame, sys, time, math
from constants import *
from gfx.loadSprite import Sprites
from gfx.loadAllSprites import load_Sprites
from entities.player import Player
from entities.playerHitbox import PlayerHitbox
from gfx.render import *
from bullets import *

pygame.init()
global player, WINDOW
MONITOR_INFO = pygame.display.Info()
if MONITOR_INFO.current_h >= 1080 and MONITOR_INFO.current_w >= 1920:
	WINDOW = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
else:
	WINDOW = pygame.display.set_mode((MONITOR_INFO.current_w, MONITOR_INFO.current_h), pygame.FULLSCREEN)
loaded_Sprites = [[], [], []]
render_objects = []
renderBullets = []
renderPlayerBullets = []
load_Sprites(loaded_Sprites)
clock = pygame.time.Clock()
window_w, window_h = pygame.display.get_surface().get_size()

player = Player(int(window_w/2), int(window_h/2), loaded_Sprites, WINDOW, renderPlayerBullets)
render_objects.append(player)
playerHitbox = PlayerHitbox(loaded_Sprites, WINDOW, player)

#Input handling
def keyboard(event):
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_b]:
		playerpos = player.getPos()
		StartBulletFan(980, 0, 20, 160, 50,loaded_Sprites, 14, 3, WINDOW, renderBullets)
		#StartStraight(980, 540, True, playerpos[0], playerpos[1], loaded_Sprites, 14, 6, WINDOW, renderBullets)
	if pressed[pygame.K_ESCAPE]:
		pygame.quit()
		sys.exit()
	else:
		pass


start_time = time.time()
framecount = 0
WINDOW.fill((66, 194, 244))
pygame.display.flip()
StartBulletFan(980, 0, 20, 160, 50,loaded_Sprites, 14, 3, WINDOW, renderBullets)
while True:
	clock.tick(MAX_FPS)
	framecount+=1 
	if (time.time()-start_time >= 1):
		print("Enemy Bullets: " + str(len(renderBullets)) + " | Player Bullets: " + str(len(renderPlayerBullets)))
		print("FPS:"+ str(math.floor(framecount/(time.time()-start_time))))
		framecount = 0
		start_time = time.time()
	keyboard(pygame.event.get(pygame.KEYDOWN))
	player.movement(pygame.event.get(pygame.KEYDOWN), window_w, window_h)
	playerHitbox.movement(pygame.event.get(pygame.KEYDOWN))
	'''if player is not None and playerHitbox is not None:
		if pygame.sprite.collide_mask(player, playerHitbox):
			print("COLLISION")
		else:
			print("no collision :(")'''
	WINDOW.fill((66, 194, 244))
	for i in range((len(renderPlayerBullets)-1), -1, -1):
		renderPlayerBullets[i].render(WINDOW)
		remove = renderPlayerBullets[i].move(window_w, window_h)
		if (remove):
			renderPlayerBullets.pop(i)
	for i in range((len(renderBullets)-1),-1,-1):
		renderBullets[i].render(WINDOW)
		remove = renderBullets[i].move(window_w, window_h)
		if (remove):
			renderBullets.pop(i)
	render(render_objects, WINDOW)
	playerHitbox.render(WINDOW)
	pygame.display.update(render_objects)
	pygame.display.update(renderPlayerBullets)
	pygame.display.update(renderBullets)
	pygame.display.update(playerHitbox)