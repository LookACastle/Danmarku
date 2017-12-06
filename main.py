import pygame, sys, time, math
from constants import *
from gfx.loadSprite import Sprites
from gfx.loadAllSprites import load_Sprites
from entities.life import Health
from entities.player import Player
from entities.playerHitbox import PlayerHitbox
from gfx.render import *
from bullets import *
from Level import *

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
renderHearts = []
load_Sprites(loaded_Sprites)
clock = pygame.time.Clock()
window_w, window_h = pygame.display.get_surface().get_size()

player = Player(3, int(window_w/2), int(window_h/2), loaded_Sprites, WINDOW, renderPlayerBullets)
render_objects.append(player)
playerHitbox = PlayerHitbox(loaded_Sprites, WINDOW, player)

#Input handling
def keyboard(event):
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_ESCAPE]:
		pygame.quit()
		sys.exit()
	else:
		pass

def PlayerUpdate(render_objects, renderPlayerBullets, keydown, window_w, window_h):
	player.movement(keydown, window_w, window_h)
	playerHitbox.movement(keydown)
	render(render_objects, WINDOW)
	for i in range((len(renderPlayerBullets)-1), -1, -1):
		renderPlayerBullets[i].render(WINDOW)
		remove = renderPlayerBullets[i].move(window_w, window_h)
		if (remove):
			renderPlayerBullets.pop(i)

def BulletUpdate(renderBullets):
	for i in range((len(renderBullets)-1),-1,-1):
		renderBullets[i].render(WINDOW)
		remove = renderBullets[i].move(window_w, window_h)
		if (remove):
			renderBullets.pop(i)

def BulletPlayerCollision(player, playerHitbox, renderHearts, renderBullets):
	global hitTimer
	if (hitTimer > 0):
		hitTimer -= 1
	else:
		for x in range(len(renderBullets)):
			if (hitTimer <= 0):
				if pygame.sprite.collide_mask(playerHitbox, renderBullets[x]):
					health = player.getHealth()
					player.setHealth(health - 1)
					renderHearts.pop(len(renderHearts) - 1)
					hitTimer = 60

def Level(loaded_Sprites, window_w, window_h, Player, WINDOW, renderBullets, level):
	if (level == 1):
		level1(loaded_Sprites, window_w, window_h, Player, WINDOW, renderBullets)

for x in range(1, int(player.getHealth() + 1)):
	health = Health(int(player.getHealth()), x * 32, 32, loaded_Sprites, WINDOW)
	renderHearts.append(health)
start_time = time.time()
framecount = 0
WINDOW.fill((66, 194, 244))
pygame.display.flip()

levelThread = threading.Thread(group=None, target=Level, name=None, args=(loaded_Sprites, window_w, window_h, Player, WINDOW, renderBullets, 1, ))
levelThread.start()
hitTimer = 0
while True:
	if (player.getHealth() == 0):
		pygame.quit()
		sys.exit()
	else:
		WINDOW.fill((66, 194, 244))
		playerUpdateThread = threading.Thread(group=None, target=PlayerUpdate, name=None, args=(render_objects, renderPlayerBullets, pygame.event.get(pygame.KEYDOWN), window_w, window_h, ))
		playerUpdateThread.start()
		BulletUpdateThread = threading.Thread(group=None, target=BulletUpdate, name=None, args=(renderBullets, ))
		BulletUpdateThread.start()
		BulletPlayerCollisionThread = threading.Thread(group=None, target=BulletPlayerCollision, name=None, args=(player, playerHitbox, renderHearts, renderBullets, ))
		BulletPlayerCollisionThread.start()
		clock.tick(MAX_FPS)
		framecount+=1
		if (time.time()-start_time >= 1):
			print("Enemy Bullets: " + str(len(renderBullets)) + " | Player Bullets: " + str(len(renderPlayerBullets)))
			print("FPS:"+ str(math.floor(framecount/(time.time()-start_time))))
			framecount = 0
			start_time = time.time()
		playerUpdateThread.join()
		BulletUpdateThread.join()
		BulletPlayerCollisionThread.join()
		print (hitTimer)
		keyboard(pygame.event.get(pygame.KEYDOWN))
		playerHitbox.render(WINDOW)
		for x in range(len(renderHearts)):
			renderHearts[x].render(WINDOW)
		pygame.display.update()