import pygame

def load_image(path, convert_alpha=True):
    img = pygame.image.load(path)

    return img if not convert_alpha else img.convert_alpha()