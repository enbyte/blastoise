def map_2d(function, matrix):
    for row in matrix:
        for element in row:
            function(element)