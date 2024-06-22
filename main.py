import pygame
from loader import load_image
from tilemap import *

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True


grass_tile = Tile('demo_assets/grass.png', 'grass')
empty_tile = NullTile()
tmap_grass = Tilemap('map', [empty_tile, grass_tile])


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    tmap_grass.draw(screen, *pygame.mouse.get_pos())

    pygame.display.flip()