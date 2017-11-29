import pygame
from time import sleep
from gfx.loadSprite import Sprites
from entities.bullet import *
import threading
from constants import *

def StartBulletShower(x, amount, spread, sprite, Window, array, render, speed):
	bulletshower = threading.Thread(group=None, target=BulletShower, name=None, args=(x, amount, spread, sprite, Window, array, render, speed))
	bulletshower.start()

def StartBulletFan(x, amount, spread, delay, sprite):
	bulletfan = threading.Thread(group=None, target=BulletFan, name=None, args=(x, y, amount, spread, delay, array, sprite, speed, Window, render))
	bulletfan.start()

def StartStraight(x, y, Tracer, px, py, array, sprite, speed, Window, render):
	bulletfan = threading.Thread(group=None, target=Straight, name=None, args=(x, y, Tracer, px, py, sprite, array, speed, Window, render))
	bulletfan.start()

def BulletShower(x, amount, spread, sprite, Window, array, render, speed):
	for n in range(amount):
		SpawnBullet(sprite,x+n*spread,-128,0,speed,Window, array, render, 0)

def BulletFan(x, y, amount, spread, delay, array, sprite, speed, Window, render):
	for n in range(amount):
		angle = (spread/amount*n-spread/2)
		vx = math.cos(angle/180*pi)*speed
		vy = math.sin(angle/180*pi)*speed
		sleep(delay/1000)
		SpawnBullet(sprite, x, y, vx, vy, Window, array, render, angle)

def Straight(x, y, Tracer, px, py, sprite, array, speed, Window, render):
	if Tracer:
		t = (((x**2-px**2)+(y**2-py**2))**(0.5))/speed
		vx = abs((px-x)/t)
		vy = abs((py-y)/t)
		SpawnBullet(sprite, x, y, vx, vy, Window, array, render, rotate)
	else:
		SpawnBullet(sprite, x, y, 0, speed, Window, array, render, 0)

def Function(funcx, funcy, x, y, sprite):
	bullet(sprite, x, y, vx, vy, 0)


def SpawnBullet(sprite, x, y, vx, vy, Window, array, render, rotate):
	obj = bullet(sprite, x, y, vx, vy, array[ENEMYSPRITESARRAY], Window)
	obj.rotate(rotate)
	render.append(obj)
	obj.render(Window)