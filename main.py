import pygame
import tilemap
from loader import load_image

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True


tmap_grass = tilemap.Tilemap(10, 10, 'demo_assets/grass.png')


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    tmap_grass.draw(screen, *pygame.mouse.get_pos())

    pygame.display.flip()