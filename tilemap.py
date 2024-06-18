import pygame
from pygame.locals import *

pygame.init()

class Tilemap:
    def __init__(self, width, height, image):
        self.image = pygame.image.load(image).convert_alpha()
        self.width = width
        self.height = height
        self.tile_width = width / self.image.get_rect().width
        self.tile_height = height / self.image.get_rect().height


    def draw(self, surface, x, y):
        for i in range(x):
            for j in range(y):
                surface.blit(self.image, (i * self.image.get_rect().width, j * self.image.get_rect().height))

