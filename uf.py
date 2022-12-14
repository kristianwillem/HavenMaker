# file title stands for "useful functions", but that felt like too long of a title to reference.

def add_coordinates(coordinate_a, coordinate_b):
    new_coordinate = [0, 0, 0]
    for i in range(3):
        new_coordinate[i] = coordinate_a[i] + coordinate_b[i]
    return new_coordinate


def subtract_coordinates(coordinate_a, coordinate_b):
    new_coordinate = [0, 0, 0]
    for i in range(3):
        new_coordinate[i] = coordinate_a[i] - coordinate_b[i]
    return new_coordinate
