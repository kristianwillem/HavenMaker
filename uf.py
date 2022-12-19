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


def is_adjacent(coordinate_a, coordinate_b):
    adjacent_check = [coordinate_a[0]-coordinate_b[0], coordinate_a[1]-coordinate_b[1], coordinate_a[2]-coordinate_b[2]]
    if -1 in adjacent_check and 0 in adjacent_check and 1 in adjacent_check:
        return True
    else:
        return False
