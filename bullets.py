import pygame
import math
from time import sleep
from gfx.loadSprite import Sprites
from entities.bullet import *
import threading
from constants import *

def StartBulletShower(x, amount, spread, delay, sprite, Window, array, render, speed):
	bulletshower = threading.Thread(group=None, target=BulletShower, name=None, args=(x, amount, spread, delay, sprite, Window, array, render, speed))
	bulletshower.start()

def StartBulletFan(x, y, amount, spread, delay, array, sprite, speed, Window, render):
	bulletfan = threading.Thread(group=None, target=BulletFan, name=None, args=(x, y, amount, spread, delay, array, sprite, speed, Window, render))
	bulletfan.start()

def StartStraight(x, y, Tracer, px, py, array, sprite, speed, Window, render):
	bulletfan = threading.Thread(group=None, target=Straight, name=None, args=(x, y, Tracer, px, py, sprite, array, speed, Window, render))
	bulletfan.start()

def StartBeam(x, Tracer, px, windowHeight, array, Window, render, preBeamRender):
	bulletfan = threading.Thread(group=None, target=Beam, name=None, args=(x, Tracer, windowHeight, px, array, Window, render, preBeamRender))
	bulletfan.start()

def BulletShower(x, amount, spread, delay, sprite, Window, array, render, speed):
	for n in range(amount):
		SpawnBullet(sprite,x+n*spread,-128,0,speed,Window, array, render, 0)
		sleep(delay/1000)

def BulletFan(x, y, amount, spread, delay, array, sprite, speed, Window, render):
	for n in range(amount):
		angle = (spread/amount*n-spread/2)+90
		vx = math.cos(angle/180*math.pi)*speed
		vy = math.sin(angle/180*math.pi)*speed
		sleep(delay/1000)
		rotate = -1*(math.degrees(math.acos(vx/speed))+90)
		SpawnBullet(sprite, x, y, vx, vy, Window, array, render, rotate)

def Straight(x, y, Tracer, px, py, sprite, array, speed, Window, render):
	if Tracer:
		t = (((x-px)**2+(y-py)**2)**(0.5))/speed
		vx = abs((px-x)/t)
		vy = abs((py-y)/t)
		if (y>py):
			vy = vy*(-1)
		if (x>px):
			vx = vx*(-1)
		rotate = math.degrees(math.atan2(px-x, py-y))
		SpawnBullet(sprite, x, y, vx, vy, Window, array, render, rotate)
	else:
		SpawnBullet(sprite, x, y, 0, speed, Window, array, render, 0)

def Beam(x, Tracer, windowHeight, px, array, Window, render, preBeamRender):
	amount = math.ceil(windowHeight/128) + 1
	if Tracer:
		x = px
	for i in range(amount):
		preBeam(x, 128*i, Window, array, preBeamRender)
	sleep(2)
	removePreBeam(amount, preBeamRender)
	for i in range(amount):
		SpawnBullet(27, x, 128*i, 0, 0, Window, array, render, 0)
	sleep(4)
	removeBeam(amount, render)

def removeBeam(amount, render):
	for x in range(amount-1, -1, -1):
		render.pop(x)

def preBeam(x, y, Window, array, preBeamRender):
	obj = bullet(31, x, y, 0, 0, array[ENEMYSPRITESARRAY], Window)
	preBeamRender.append(obj)
	obj.render(Window)

def removePreBeam(amount, PreBeamRender):
	for x in range(amount-1, -1, -1):
		PreBeamRender.pop(x)

def Function(funcx, funcy, x, y, sprite):
	bullet(sprite, x, y, vx, vy, 0)

def SpawnBullet(sprite, x, y, vx, vy, Window, array, render, rotate):
	obj = bullet(sprite, x, y, vx, vy, array[ENEMYSPRITESARRAY], Window)
	obj.rotate(rotate)
	render.append(obj)
	obj.render(Window)