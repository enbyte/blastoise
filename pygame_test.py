# make sure module can properly be imported
import pygame

import sys

# test inits

pygame.init()
pygame.font.init()
pygame.mixer.init()


# test opening a window

screen = pygame.display.set_mode((1, 1))


# exit gracefully

sys.exit(0)
