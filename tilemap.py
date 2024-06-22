import pygame
from pygame.locals import *

from loader import load_image, load_matrix
import util

pygame.init()


class Tile:
    def __init__(self, image, name):
        self.image = load_image(image)
        self.name = name

    def draw(self, surface, x, y):
        surface.blit(self.image, (x, y))

    def get_name(self):
        return self.name
    
    def __eq__(self, other):
        return self.name == other.name
    
class NullTile(Tile):
    def __init__(self):
        self.name = 'null'
    
    def draw(self, surface, x, y):
        pass
class Tilemap:
    def __init__(self, matrix_path, tileset, tile_size=(32, 32)):

        self.matrix = load_matrix(matrix_path)

        self.tile_width = len(self.matrix[0]) # the number of tiles there are in the width
        self.tile_height = len(self.matrix)

        self.tile_size = tile_size

        self.width = self.tile_width * tile_size[0] # pixel width of the matrix
        self.height = self.tile_height * tile_size[1] # pixel height of the matrix

        # Convert each integer to a Tile object
        for row_number, row in enumerate(self.matrix):
            for tile_number, tile in enumerate(row):
                self.matrix[row_number][tile_number] = tileset[tile]

    def get_tileset_index(self, tile):
        return self.tileset.index(tile)

    def draw(self, surface, x, y):
        cached_x = x
        for row in self.matrix:
            for tile in row:
                tile.draw(surface, x, y)
                x += self.tile_size[0]
            x = cached_x
            y += self.tile_size[1]




