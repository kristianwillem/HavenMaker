from dungeon import Dungeon
from room import Room
from monster import Monster

import files.chests_file, files.dungeons_file, files.monsters_file, files.rooms_file, files.rules_file

def load_rules():
    all_rules = files.rules_file.rules
    return all_rules


def load_chests():
    all_chests = files.chests_file.chests
    return all_chests


def load_rooms():


def load_monsters():
    all_monsters = []
    for monster_type in files.monsters_file.available_monsters:
        monster_name = monster_type["name"]
        monster_max = monster_type["max"]
        monster_difficulty = monster_type["difficulty"]
        monster_theme = monster_type["theme"]
        all_monsters.append(Monster(monster_name, monster_max, monster_difficulty, monster_theme))
    return all_monsters

def load_dungeon(dungeon_name):
    dungeon_data =

    goal_data = dungeon_data[0]
    rules_data = dungeon_data[1]
    rooms_data = dungeon_data[2]
    connections_data = dungeon_data[3]
    monster_data = dungeon_data[4]
    obstacles_data = dungeon_data[5]
    traps_data = dungeon_data[6]
    h_terrain_data = dungeon_data[7]
    d_terrain_data = dungeon_data[8]
    chest_data = dungeon_data[9]
    coins_data = dungeon_data[10]
    theme_data = dungeon_data[11]
    placements_data = dungeon_data[12]
    start_data = dungeon_data[13]

    new_dungeon = Dungeon(goal_data, rules_data, rooms_data, connections_data, monster_data, obstacles_data, traps_data, h_terrain_data, d_terrain_data, chest_data, coins_data, theme_data, placements_data, start_data)
    return new_dungeon
