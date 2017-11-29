import pygame
from gfx.loadSprite import Sprites
from entities.bullet import *
import threading
from constants import *

def StartBulletShower(x, amount, spread, sprite, Window, array, moveArray, renderArray):
	bulletshower = threading.Thread(group=None, target=BulletShower, name=None, args=(x, amount, spread, sprite, Window, array, moveArray, renderArray))
	bulletshower.start()

def StartBulletFan(x, amount, spread, delay, sprite):
	bulletfan = threading.Thread(group=None, target=BulletFan, name=None, args=(x, amount, spread, delay, sprite))
	bulletfan.start()

def BulletShower(x, amount, spread, sprite, Window, array, moveArray, renderArray):
	for n in range(amount):
		SpawnBullet(sprite,x+n*spread,-128,0,5,Window, array, moveArray, renderArray)

def BulletFan(x, amount, spread, delay, sprite):
	for n in range(amount):
		SpawnBullet(sprite)
	bullet(sprite, x, y, vx, vy, 0);

def StraightDown(x,y, Tracer, sprite):
	bullet(sprite, x, y, vx, vy, 0);
	

def Function(funcx, funcy, x, y, sprite):
	bullet(sprite, x, y, vx, vy, 0);


def SpawnBullet(sprite, x, y, vx, vy, Window, array, moveArray, renderArray):
	obj = bullet(sprite, x, y, vx, vy, array[ENEMYSPRITESARRAY], Window);
	moveArray.append(obj)
	renderArray.append(obj)
	obj.render(Window)