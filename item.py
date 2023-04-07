import pygame
import random

from settings import *

class Item(pygame.sprite.Sprite):
    def __init__(self, image, xpos=0, ypos=0):
        super().__init__()

        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (16*5, 16*5))
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(0, HEIGHT)