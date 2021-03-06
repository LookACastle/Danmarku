import pygame, math, time
from bullets import *
from constants import *
from random import randint
from random import uniform

SBF = StartBulletFan #x, y, amount, spread, delay, array, sprite, speed, Window, render
SBS = StartBulletShower #x, amount, spread, delay, sprite, Window, array, render, speed
SS = StartStraight #x, y, Tracer, px, py, array, sprite, speed, Window, render
SB = StartBeam #x, Tracer, px, WindowHeight, array, Window, renderbeam, renderprebeam

def level1(Sprites ,WindowWidth, WindowHeight, player, Window, render):
	time.sleep(5)
	SBF(WindowWidth/5,   -128, 20, 90, 1000, Sprites, 14, 6, Window, render)
	SBF(WindowWidth/2,   -128, 20, 90, 1000, Sprites, 14, 6, Window, render)
	SBF(WindowWidth/5*4, -128, 20, 90, 1000, Sprites, 14, 6, Window, render)

	time.sleep(22)
	SBS(0, 21, WindowWidth/20, 0, 11, Window, Sprites, render, 6)
	SBF(WindowWidth/2, 0, 20, 90, 0, Sprites, 14, 6, Window, render)
	time.sleep(5)
	SBF(WindowWidth/10,   -128, 30, 120, 300, Sprites, 14, 6, Window, render)
	SBF(WindowWidth/2,    -128, 30, 120, 300, Sprites, 14, 6, Window, render)
	SBF(WindowWidth/10*9, -128, 30, 120, 300, Sprites, 14, 6, Window, render)
	time.sleep(10)
	SBS(0, 31, WindowWidth/30, 250, 11, Window, Sprites, render, 6)
	SBS(WindowWidth, 30, -WindowWidth/31, 250, 11, Window, Sprites, render, 6)
	SBF(WindowWidth/2, -128, 31, 150, 250, Sprites, 14, 6, Window, render)
	sleep(10)
	SBS(0, 26, WindowWidth/25, 0, 11, Window, Sprites, render, 6)
	SBF(0          , -128, 40,  180, 150, Sprites, 14, 6, Window, render)
	SBF(WindowWidth, -128, 40, -180, 150, Sprites, 14, 6, Window, render)

def level2(Sprites ,WindowWidth, WindowHeight, player, Window, render):
	time.sleep(5)
	SS(WindowWidth/2,  -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/12, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/17, -128, False, 0, 0, Sprites, 11, 6, Window, render)

	SBF(0          , -128, 40,  180, 150, Sprites, 14, 6, Window, render)
	SBF(WindowWidth, -128, 40, -180, 150, Sprites, 14, 6, Window, render)

	time.sleep(3)
	SBS(0, 31, WindowWidth/30, 0, 11, Window, Sprites, render, 6)
	SBF(0          , -128, 40,  180, 150, Sprites, 14, 6, Window, render)
	SBF(WindowWidth, -128, 40, -180, 150, Sprites, 14, 6, Window, render)
	time.sleep(2)
	SBS(0, 31, WindowWidth/30, 0, 11, Window, Sprites, render, 6)

	time.sleep(1)
	SS(WindowWidth/15,    -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/11,    -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/76*52, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/2,     -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/4,     -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/3,     -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/4*3,   -128, False, 0, 0, Sprites, 11, 6, Window, render)
	time.sleep(2)

	SBF(WindowWidth/4  , -128, 40,  180, 150, Sprites, 14, 6, Window, render)
	SBF(WindowWidth/4*3, -128, 40, -180, 150, Sprites, 14, 6, Window, render)

	playerpos = player.getPos()
	SS(WindowWidth/7*0, -128, True, playerpos[0], playerpos[1], Sprites, 18, 6, Window, render)
	time.sleep(0.25)
	playerpos = player.getPos()
	SS(WindowWidth/7*1, -128, True, playerpos[0], playerpos[1], Sprites, 18, 6, Window, render)
	time.sleep(1)
	playerpos = player.getPos()
	SS(WindowWidth/27*14, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/12*3, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/2, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/17*9, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/7*2, -128, True, playerpos[0], playerpos[1], Sprites, 18, 6, Window, render)
	time.sleep(1)
	playerpos = player.getPos()
	SS(WindowWidth/7*3, -128, True, playerpos[0], playerpos[1], Sprites, 18, 6, Window, render)
	SS(WindowWidth/43*15, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/3, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/2, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/12, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	time.sleep(1)
	playerpos = player.getPos()
	SS(WindowWidth/7*4, -128, True, playerpos[0], playerpos[1], Sprites, 18, 6, Window, render)
	SS(WindowWidth/17, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/3, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/24*19, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/21*13, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/7, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/9*2, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/15, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	time.sleep(1)
	playerpos = player.getPos()
	SS(WindowWidth/7*5, -128, True, playerpos[0], playerpos[1], Sprites, 18, 6, Window, render)
	SS(WindowWidth/11, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/76*52, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/2, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/4, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/3, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/4*3, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/27*14, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/12*3, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	time.sleep(1)
	playerpos = player.getPos()
	SS(WindowWidth/7*6, -128, True, playerpos[0], playerpos[1], Sprites, 18, 6, Window, render)
	SS(WindowWidth/2, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/17*9, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/43*15, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/3, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/2, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/12, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/17, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/3, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	time.sleep(1)
	playerpos = player.getPos()
	SS(WindowWidth/7*7, -128, True, playerpos[0], playerpos[1], Sprites, 18, 6, Window, render)
	SS(WindowWidth/24*19, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/21*13, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/7, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/9*2, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/15, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/11, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/76*52, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/2, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/4, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/3, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/4*3, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/27*14, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/12*3, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/2, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/17*9, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/43*15, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	SS(WindowWidth/3, -128, False, 0, 0, Sprites, 11, 6, Window, render)
	time.sleep(1)	
	SBF(WindowWidth/11   , -128, 10, 180, 150, Sprites, 14, 6, Window, render)
	SBF(WindowWidth/11*2 , -128, 10, 180, 150, Sprites, 14, 6, Window, render)
	SBF(WindowWidth/11*3 , -128, 10, 180, 150, Sprites, 14, 6, Window, render)
	SBF(WindowWidth/11*4 , -128, 10, 180, 150, Sprites, 14, 6, Window, render)
	SBF(WindowWidth/11*5 , -128, 10, 180, 150, Sprites, 14, 6, Window, render)
	SBF(WindowWidth/11*6 , -128, 10, 180, 150, Sprites, 14, 6, Window, render)
	SBF(WindowWidth/11*7 , -128, 10, 180, 150, Sprites, 14, 6, Window, render)
	SBF(WindowWidth/11*8 , -128, 10, 180, 150, Sprites, 14, 6, Window, render)
	SBF(WindowWidth/11*9 , -128, 10, 180, 150, Sprites, 14, 6, Window, render)
	SBF(WindowWidth/11*10, -128, 10, 180, 150, Sprites, 14, 6, Window, render)

def level3(Sprites ,WindowWidth, WindowHeight, player, Window, render, renderbeam, renderprebeam):
	while True:
		playerpos = player.getPos()
		spawn = randint(1, 100)
		if (spawn < 101 and spawn > 90):
			SBF(randint(128, WindowWidth-128), -128, randint(1,15), randint(45,180), randint(0,1000), Sprites, 14, randint(4,6), Window, render)
		if (spawn == 90):
			SB(randint(128, WindowWidth-128), randint(0,1), playerpos[0], WindowHeight, Sprites, Window, renderbeam, renderprebeam)
		if (spawn < 90 and spawn > 75):
			SS(randint(128, WindowWidth-128), -128, True, playerpos[0], playerpos[1], Sprites, 17, randint(6,8), Window, render)
		if (spawn < 76):
			SS(randint(128, WindowWidth-128), -128, False, playerpos[0], playerpos[1], Sprites, 11, randint(6,8), Window, render)
		time.sleep(uniform(0,0.2))