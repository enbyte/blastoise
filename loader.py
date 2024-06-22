import pygame, csv

def load_image(path, convert_alpha=True):
    img = pygame.image.load(path)

    return img if not convert_alpha else img.convert_alpha()


def load_matrix(path, squelch_invalid=False):
    matrix = []
    with open(path, 'r') as file:
        for line in file.readlines():
            try:
                matrix.append(list(map(int, line.strip().split(','))))
            except ValueError:
                if squelch_invalid:
                    continue
                else:
                    raise ValueError("Invalid row (non-integer value found, row %d) in file %s" % (len(matrix) + 1, path))

    return matrix