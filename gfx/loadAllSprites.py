import pygame
from constants import *

def load_Sprites(loaded_Sprites):
    folders = ["Enemies", "Player", "PlayerMainScreen"]
    for x in range(len(SPRITES)):
        for y in range(len(SPRITES[x])):
            sprite = pygame.image.load("sprites/" + folders[x] + "/" + str(y) + ".png")
            loaded_Sprites[x].append(sprite)