
def check_validity(dungeon):
    overlap = overlap_check(dungeon)
    reachable = reachability_check(dungeon)
    if not overlap or not reachable:
        return False
    else:
        return True


def overlap_check(dungeon):
    overlap_valid = True
    for coordinate in dungeon.coordinates:
        if dungeon.coordinates.count(coordinate) > 1:
            overlap_valid = False
    return overlap_valid


def reachability_check(dungeon):
    reachability_valid = True
    start_locations = dungeon.placements["start"]
    monster_locations = dungeon.placements["monsters"]
    main_start = start_locations[0]
    coordinates = dungeon.coordinates
    for obstacle_hex in dungeon.placements["obstacles"]:
        coordinates.remove(obstacle_hex)
    # do the actual search
    for start in start_locations:
        path = search(coordinates, main_start, start)
        if not path:
            reachability_valid = False
    for monster in monster_locations:
        path = search(coordinates, main_start, monster)
        if not path:
            reachability_valid = False
    return reachability_valid


def search(coordinates, start, finish):
    # search algorithm (DFS)
    if start == finish:
        return True
    current_node = start
    unvisited_nodes = coordinates.copy()
    past_nodes = []
    next_nodes = []

    while next_nodes != [] or current_node == start:
        for node in unvisited_nodes:
            if is_adjacent(current_node, node):
                next_nodes.append(node)
                unvisited_nodes.remove(node)
        if finish in next_nodes:
            return True
        if not next_nodes:
            return False
        past_nodes.append(current_node)
        current_node = next_nodes.pop()

    # search for neighboring nodes to current_node that are not in past_nodes or next_nodes
    # append those nodes
    # if the finish node is in next_nodes, return true
    # when done, put the current node in past_nodes, then pop the next_nodes to current_node
    # if next_nodes is empty, return false.


def is_adjacent(coordinate_a, coordinate_b):
    adjacent_check = [coordinate_a[0]-coordinate_b[0], coordinate_a[1]-coordinate_b[1], coordinate_a[2]-coordinate_b[2]]
    if -1 in adjacent_check and 0 in adjacent_check and 1 in adjacent_check:
        return True
    else:
        return False
