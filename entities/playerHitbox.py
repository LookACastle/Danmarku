import pygame
from constants import *
from gfx.loadSprite import Sprites

class PlayerHitbox(pygame.sprite.Sprite):
    def __init__(self, array, window, player):
        self.array = array
        self.position = player.getPos()
        self.x = self.position[0]
        self.y = self.position[1]
        self.window = window
        self.player = player
        self.t = False
        self.hitbox = self.array[PLAYERSPRITESARRAY][PLAYER_HITBOX].copy()
        pygame.sprite.Sprite.__init__(self)
        self.mask = pygame.mask.from_surface(self.hitbox)
        self.speed = PLAYER_SPEED
        self.rect = self.hitbox.get_rect(center=(self.x, self.y),width=(20+self.speed*2),height=(20+self.speed*2))
        #self.rect = pygame.Rect(self.x - (64 + self.speed), self.y - (64 + self.speed), 128 + self.speed*2, 128 + self.speed*2)
		
    def movement(self, event):
        pressed = pygame.key.get_pressed()
        self.position = self.player.getPos()
        self.x = self.position[0]
        self.y = self.position[1]
        self.rect = self.hitbox.get_rect(center=(self.x, self.y),width=(20+self.speed*2),height=(20+self.speed*2))
        #self.rect = pygame.Rect(self.x - (64 + self.speed), self.y - (64 + self.speed), 128 + self.speed*2, 128 + self.speed*2)
        if pressed[pygame.K_LSHIFT]:
            self.t = True
        else:
            self.t = False

    def render(self, window):
        if (self.t):
            window.blit(self.hitbox, (self.x - 64, self.y - 64))