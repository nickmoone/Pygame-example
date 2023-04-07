import pygame
import random

from settings import *

class PlatformBar(pygame.sprite.Sprite):
    def __init__(self, image, xpos=0, ypos=0):
        super().__init__()

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = xpos
        self.rect.y = ypos