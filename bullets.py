import pygame
from gfx.loadSprite import Sprites
from entities.bullet import *
import threading
from constants import *

def StartBulletShower(x, amount, spread, sprite, Window, array, render):
	bulletshower = threading.Thread(group=None, target=BulletShower, name=None, args=(x, amount, spread, sprite, Window, array, render))
	bulletshower.start()

def StartBulletFan(x, amount, spread, delay, sprite):
	bulletfan = threading.Thread(group=None, target=BulletFan, name=None, args=(x, amount, spread, delay, sprite))
	bulletfan.start()

def StartStraight(x, y, Tracer, px, py, sprite, array, speed, Window, render):
	bulletfan = threading.Thread(group=None, target=Straight, name=None, args=(x, y, Tracer, px, py, sprite, array, speed, Window, render))
	bulletfan.start()

def BulletShower(x, amount, spread, sprite, Window, array, render, speed):
	for n in range(amount):
		SpawnBullet(sprite,x+n*spread,-128,0,speed,Window, array, render)

def BulletFan(x, amount, spread, delay, sprite):
	for n in range(amount):
		SpawnBullet(sprite)

def Straight(x, y, Tracer, px, py, sprite, array, speed, Window, render):
	if Tracer:
		t = (((x**2-px**2)+(y**2-py**2))**(0.5))/speed
		vx = (px-x)/t
		vy = (py-y)/t
		SpawnBullet(sprite, x, y, vx, vy, Window, array, render)
	else:
		SpawnBullet(sprite, x, y, 0, speed, Window, array, render)

def Function(funcx, funcy, x, y, sprite):
	bullet(sprite, x, y, vx, vy, 0)


def SpawnBullet(sprite, x, y, vx, vy, Window, array, render):
	obj = bullet(sprite, x, y, vx, vy, array[ENEMYSPRITESARRAY], Window)
	render.append(obj)
	obj.render(Window)