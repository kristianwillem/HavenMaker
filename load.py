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
    all_rooms = []
    for room in files.rooms_file.available_rooms:
        room_name = room["name"]
        room_side = room["side"]
        room_theme = room["theme"]
        room_coordinates = room["coordinates"]
        room_links = room ["links"]
        room_hexes = len(room_coordinates)
        all_rooms.append(Room(room_name, room_side, room_theme, room_coordinates, room_links, room_hexes))
    return all_rooms


def load_monsters():
    all_monsters = []
    for monster_type in files.monsters_file.available_monsters:
        monster_name = monster_type["name"]
        monster_max = monster_type["max"]
        monster_difficulty = monster_type["difficulty"]
        monster_theme = monster_type["theme"]
        all_monsters.append(Monster(monster_name, monster_max, monster_difficulty, monster_theme))
    return all_monsters


def load_dungeon(all_rooms, all_monsters):
    all_dungeons = []
    for specific_dungeon in files.dungeons_file.available_dungeons:
        dungeon_name = specific_dungeon["name"]
        dungeon_goal = specific_dungeon["goal"]
        dungeon_rules = specific_dungeon["rules"]

        # get dungeon rooms as classes
        raw_rooms = specific_dungeon["rooms"]
        dungeon_rooms = []
        for used_room in raw_rooms:
            room_name = used_room[0]
            room_side = used_room[1]
            for possible_room in all_rooms:
                if room_name == possible_room.name and room_side == possible_room.side:
                    dungeon_rooms.append(possible_room.copy())
                    # unsure whether this works. If not, change this to work similar to connection/monsters
                    dungeon_rooms[-1] = dungeon_rooms[-1].rotate[used_room[3]]

        # change all connection names to their corresponding room classes
        dungeon_connections = specific_dungeon["connections"]
        for used_connection in dungeon_connections:
            for connected_room in dungeon_rooms:
                if used_connection[0] == connected_room.name:
                    used_connection[0] = connected_room
                if used_connection[2] == connected_room.name:
                    used_connection[2] = connected_room

        # get dungeon monsters
        dungeon_monsters = specific_dungeon["dungeon_monsters"]
        for used_monster in dungeon_monsters:
            for possible_monster in all_monsters:
                if used_monster[0] == possible_monster.name:
                    used_monster[0] = possible_monster

        dungeon_obstacles = specific_dungeon["obstacles"]
        dungeon_traps = specific_dungeon["traps"]
        dungeon_h_terrain = specific_dungeon["hazardous terrain"]
        dungeon_d_terrain = specific_dungeon["difficult terrain"]
        dungeon_chests = specific_dungeon["chests"]
        dungeon_coins = specific_dungeon["coins"]
        dungeon_theme = specific_dungeon["main theme"]
        dungeon_placements = specific_dungeon["placements"]
        dungeon_start = specific_dungeon["start"]

        all_dungeons.append(Dungeon(dungeon_goal, dungeon_rules, dungeon_rooms, dungeon_connections, dungeon_monsters, dungeon_obstacles, dungeon_traps, dungeon_h_terrain, dungeon_d_terrain, dungeon_chests, dungeon_coins, dungeon_theme, dungeon_placements, dungeon_start))
    return all_dungeons
