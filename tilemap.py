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
    def __init__(self, matrix_path, tileset, position, tile_size=(32, 32)):

        self.matrix = load_matrix(matrix_path)

        self.x, self.y = position

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

    def draw(self, surface):
        x, y = self.x, self.y
        for row in self.matrix:
            for tile in row:
                tile.draw(surface, x, y)
                x += self.tile_size[0]
            x = self.x
            y += self.tile_size[1]

    def get_tile_coordinates_at_point(self, worldspace_x, worldspace_y):
        offset_x, offset_y = worldspace_x - self.x, self.y - worldspace_y

        if offset_x >= self.width or offset_y >= self.height:
            return None

        tile_offset_x, tile_offset_y = offset_x // self.tile_size[0], offset_y // self.tile_size[1]
        
        return tile_offset_x, tile_offset_y
    

    def get_tile_at_point(self, worldspace_x, worldspace_y):
        # return the tile at the given point

        tile_offset = self.get_tile_coordinates_at_point(worldspace_x, worldspace_y)
        return (self.matrix[tile_offset[1]][tile_offset[0]] if tile_offset is not None else None)
    
    




