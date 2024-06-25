import random

def map_2d(function, matrix):
    for row in matrix:
        for element in row:
            function(element)

def random_transform(l, variation):
    new_l = []
    for i in l:
        new_l.append(i + random.randint(-variation, variation))

    return new_l