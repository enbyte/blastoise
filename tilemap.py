import pygame
from pygame.locals import *

from loader import load_image

pygame.init()

class Tilemap:
    def __init__(self, width, height, image):
        self.image = load_image(image)

        self.tile_width = width # the number of tiles there are in the width
        self.tile_height = height

        self.width = self.tile_width * self.image.get_rect().width
        self.height = self.tile_height * self.image.get_rect().height


    def draw(self, surface, x, y):
        for i in range(self.tile_width):
            for j in range(self.tile_height):
                surface.blit(self.image,
                             (x + i * self.image.get_rect().width,
                              y + j * self.image.get_rect().height))




