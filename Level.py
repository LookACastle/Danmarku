import pygame, math, time
from bullets import *
from constants import *

SBF = StartBulletFan #x, y, amount, spread, delay, array, sprite, speed, Window, render
SBS = StartBulletShower #x, amount, spread, delay, sprite, Window, array, render, speed
SS = StartStraight #x, y, Tracer, px, py, array, sprite, speed, Window, render

def level1(Sprites ,WindowWidth, WindowHeight, player, Window, render):
	time.sleep(10)
	SBF(WindowWidth/5,   0, 20, 90, 1000, Sprites, 14, 6, Window, render)
	SBF(WindowWidth/2,   0, 20, 90, 1000, Sprites, 14, 6, Window, render)
	SBF(WindowWidth/5*4, 0, 20, 90, 1000, Sprites, 14, 6, Window, render)

	time.sleep(25)
	SBS(0, 21, WindowWidth/20, 0, 11, Window, Sprites, render, 6)
	SBF(WindowWidth/2, 0, 20, 90, 0, Sprites, 14, 6, Window, render)
	time.sleep(5)
	SBF(WindowWidth/10,   0, 30, 120, 300, Sprites, 14, 6, Window, render)
	SBF(WindowWidth/2,    0, 30, 120, 300, Sprites, 14, 6, Window, render)
	SBF(WindowWidth/10*9, 0, 30, 120, 300, Sprites, 14, 6, Window, render)
	time.sleep(10)
	SBS(0, 31, WindowWidth/30, 250, 11, Window, Sprites, render, 6)
	SBS(WindowWidth, 30, -WindowWidth/31, 250, 11, Window, Sprites, render, 6)
	SBF(WindowWidth/2, 0, 31, 150, 250, Sprites, 14, 6, Window, render)
	sleep(10)
	SBS(0, 26, WindowWidth/25, 0, 11, Window, Sprites, render, 6)
	SBF(0          , 0, 40,  180, 150, Sprites, 14, 6, Window, render)
	SBF(WindowWidth, 0, 40, -180, 150, Sprites, 14, 6, Window, render)
	