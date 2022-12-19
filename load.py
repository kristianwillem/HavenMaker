from dungeon import Dungeon


def load_dungeon(dungeon_name):
    dungeon_data =

    goal_data = dungeon_data.iat[0, 0]
    rules_data = dungeon_data.iat[1, 0]
    rooms_data = dungeon_data.iat[2, 0]
    connections_data = dungeon_data.iat[3, 0]
    monster_data = dungeon_data.iat[4, 0]
    obstacles_data = dungeon_data.iat[5, 0]
    traps_data = dungeon_data.iat[6, 0]
    h_terrain_data = dungeon_data.iat[7, 0]
    d_terrain_data = dungeon_data.iat[8, 0]
    chest_data = dungeon_data.iat[9, 0]
    coins_data = dungeon_data.iat[10, 0]
    theme_data = dungeon_data.iat[11, 0]
    placements_data = dungeon_data.iat[12, 0]
    start_data = dungeon_data.iat[13, 0]


    new_dungeon = Dungeon(goal_data, rules_data, rooms_data, connections_data, monster_data, obstacles_data, traps_data, h_terrain_data, d_terrain_data, chest_data, coins_data, theme_data, placements_data, start_data)
    return new_dungeon
