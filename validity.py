import uf


def check_validity(dungeon, inclusion):
    overlap = overlap_check(dungeon)
    reachable = reachability_check(dungeon)
    limited = limited_check(dungeon, inclusion)
    monster_limited = monster_limit_check(dungeon)
    if not overlap:
        print("invalid: overlap")
    if not reachable:
        print("invalid: reachability (goal)")
    if not limited:
        print("invalid: too many components")
    if not monster_limited:
        print("invalid: too many monsters")
    if not overlap or not reachable or not limited or not monster_limited:
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
    dungeon.get_coordinates()
    coordinates = dungeon.coordinates.copy()
    coordinates.extend(dungeon.connection_coordinates)
    if len(dungeon.placements["obstacles"]) != 0:
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
    unvisited_nodes.remove(current_node)
    past_nodes = []
    next_nodes = []

    while True:
        clear_nodes = []
        for node in unvisited_nodes:
            if uf.is_adjacent(current_node, node):
                next_nodes.append(node)
                clear_nodes.append(node)
        for node in clear_nodes:
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


def limited_check(dungeon, inclusion):
    limited = True
    obstacle_limit = 95
    h_terrain_limit = 12
    d_terrain_limit = 40
    door_limit = 26
    trap_limit = 18

    if inclusion[1]:
        obstacle_limit += 116
        h_terrain_limit += 22
        d_terrain_limit += 54
        door_limit += 19
        trap_limit += 18

    if dungeon.coins > 40:
        limited = False
    if len(dungeon.chests) > 6:
        limited = False
    if len(dungeon.connection_coordinates) > door_limit:
        limited = False
    if dungeon.traps > trap_limit:
        limited = False

    obstacles = dungeon.obstacles
    h_terrain = dungeon.h_terrain
    d_terrain = dungeon.d_terrain

    if obstacles > obstacle_limit:
        limited = False
    if h_terrain > h_terrain_limit:
        limited = False
    if d_terrain > d_terrain_limit:
        limited = False

# this isn't quite correct anymore with Frosthaven
    if obstacles + d_terrain > 111:
        limited = False
    if obstacles + h_terrain > 100:
        limited = False
    if d_terrain + h_terrain > 48:
        limited = False
    if obstacles + d_terrain + h_terrain > 112:
        limited = False
    return limited


def monster_limit_check(dungeon):
    monster_limited = True
    total_coordinates = dungeon.placements["monsters"].copy()
    monster_coordinates = dict()

    for monster_type in dungeon.monsters:
        # get the monster coordinates
        monster_data = dungeon.monsters[monster_type]
        monster_class = monster_data[0]
        total_amount = monster_data[1] + monster_data[2]
        specific_monster_coordinates = []
        for i in range(total_amount):
            if not total_coordinates:
                pass
            location = total_coordinates.pop(0)
            specific_monster_coordinates.append(location)
        monster_coordinates[monster_type] = specific_monster_coordinates

        # test for every room how many of this monster type are there
        for room in dungeon.rooms:
            room_count = 0
            room_coordinates = dungeon.room_coordinates[room]
            for mc in monster_coordinates:
                for rc in room_coordinates:
                    if mc is rc:
                        room_count += 1
            if room_count > monster_class.max_amount:
                monster_limited = False
    return monster_limited

# this can be removed if the new monster check works
def old_monster_limit_check(dungeon):
    monster_limited = True
    for monster_type in dungeon.monsters:
        monster_count = 0
        monster_data = dungeon.monsters[monster_type]
        monster_class = monster_data[0]
        monster_count += monster_data[1]
        monster_count += monster_data[2]
        if monster_count > monster_class.max_amount:
            # print(monster_class.name + " " + str(monster_count))
            monster_limited = False
    return monster_limited
