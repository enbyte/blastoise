import pygame
from pygame.locals import *

from loader import load_image
from tilemap import *

from particles import ParticleSystem, ImageParticle

import math, random

pygame.init()

FPS_CAP = 60

ALERT_ON_LOW_FPS = False
FPS_ALERT_THRESHOLD = 10

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True


grass_tile = Tile('demo_assets/grass.png', 'grass')
empty_tile = NullTile()
tmap_grass = Tilemap('demo_assets/map', [empty_tile, grass_tile], (0, 0))

clock = pygame.time.Clock()

tiles_particlesystem = ParticleSystem(max_particles=1000, kill_after=100)
grass_particle = ImageParticle('demo_assets/dirt.png', (5, 5))

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            print('click')
            clicked_tile = tmap_grass.get_tile_at_point(*pygame.mouse.get_pos())
            if clicked_tile is not None:
                print("You clicked a %s!" % clicked_tile.get_name())
                for i in range(10):
                    tiles_particlesystem.add_particle(grass_particle, *util.random_transform(pygame.mouse.get_pos(), 10), random.randint(0, 360), 2)

    screen.fill((0, 0, 0))

    tmap_grass.draw(screen)
    tiles_particlesystem.draw(screen)

    pygame.display.flip()


    if ALERT_ON_LOW_FPS and math.floor(clock.get_fps()) < FPS_ALERT_THRESHOLD:
        print("FPS: %d" % math.floor(clock.get_fps()))

    clock.tick(FPS_CAP)