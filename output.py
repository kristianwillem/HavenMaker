from dungeon import Dungeon


def output(dungeon):
    place = dungeon.placements.copy()
    print("Goal: " + dungeon.goal)
    print("Special Rules: " + str(dungeon.rules))
    room_names = []
    for room in dungeon.rooms:
        room_name = room.name + room.side
        room_rotation = dungeon.room_rotations[room]
        room_names.append([room_name, room_rotation*60])
    print("used rooms are: " + str(room_names))
    readable_connections = []
    for connection in dungeon.connections:
        room_a = connection[0]
        room_b = connection[2]
        room_a_name = room_a.name + room_a.side
        room_b_name = room_b.name + room_b.side
        readable_connections.append([room_a_name, connection[1], room_b_name, connection[3]])
    print("rooms are connected through: " + str(readable_connections))

    print("starts are at " + str(place["start"]))
    if dungeon.obstacles > 0:
        print("place obstacles at " + str(place["obstacles"]))
    if dungeon.traps > 0:
        print("place traps at " + str(place["traps"]))
    if dungeon.h_terrain > 0:
        print("place hazardous terrain at " + str(place["hazardous terrain"]))
    if dungeon.h_terrain > 0:
        print("place difficult terrain at " + str(place["difficult terrain"]))
    if dungeon.coins > 0:
        print("place coins at " + str(place["coins"]))

    if len(dungeon.chests) > 0:
        for content in dungeon.chests:
            location = place["chests"].pop(0)
            print("place a chest containing '" + str(content) + "' at " + str(location))

    for monster_type in dungeon.monsters:
        monster_data = dungeon.monsters[monster_type]
        normal_amount = monster_data[1]
        normal_locations = []
        elite_amount = monster_data[2]
        elite_locations = []
        for i in range(normal_amount):
            location = place["monsters"].pop(0)
            normal_locations.append(location)
        for i in range(elite_amount):
            location = place["monsters"].pop(0)
            elite_locations.append(location)
        print("place normal " + str(monster_type) + " at " + str(normal_locations) + " and place elite " + str(monster_type) + " at " + str(elite_locations))




