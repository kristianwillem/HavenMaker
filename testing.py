# This file is not part of the program, and exists only to test other parts of the project.

from dungeon import Dungeon
import load
from monster import Monster
from room import Room
from validity import check_validity
import files.test_dungeons_file
from output import output
import uf


def test_rotation():
    test_coordinates = [0, 0, 0], [-1, -1, 2], [-1, 0, 1], [-1, 1, 0], [-2, 0, 2], [-2, 1, 1], [-2, 2, 0], [-3, 1, 2], [-3, 2, 1], [-3, 3, 0], [-4, 2, 2], [-4, 3, 1], [-4, 4, 0], [-4, 5, -1], [-4, 6, -2], [-4, 7, -3], [-4, 8, -4], [-5, 3, 2], [-5, 4, 1], [-5, 5, 0], [-5, 6, -1], [-5, 7, -2], [-5, 8, -3], [-6, 5, 1], [-6, 6, 0], [-6, 7, -1], [-6, 8, -2], [-6, 9, -3]
    test_links = [0, -1, 1, 1, "exit"], [-3, 0, 3, 10, "exit"], [-7, 8, -1, 8, "exit"], [0, 1, -1, 4, "entry"], [-6, 4, 2, 9, "entry"], [-3, 7, -4, 2, "entry"], [-5, 9, -4, 5, "entry"]

    test_rooms = load.load_rooms()
    for any_room in test_rooms:
        if any_room.name == "J1" and any_room.side == "a":
            test_room = any_room
            break

    new_coordinates, new_links = test_room.rotate(1)

    mistake = False
    for coordinate in new_coordinates:
        if coordinate not in test_coordinates:
            mistake = True
            print("mistake in coordinates")
            break
    for link in new_links:
        if link not in test_links:
            mistake = True
            print("mistake in links")
            break

    if not mistake:
        print("all clear")


def test_validity():
    # dungeon 1 should be without problems, dungeon 2 should have overlap, dungeon 3 should have unreachable enemies
    all_rooms = load.load_rooms()
    all_monsters = load.load_monsters()
    test_dungeons = load_test_dungeons(all_rooms, all_monsters)
    test_1 = check_validity(test_dungeons[0])
    test_2 = check_validity(test_dungeons[1])
    test_3 = check_validity(test_dungeons[2])
    if test_1 == False:
        print("False Negative")
    if test_2 == True:
        print("False Positive: Overlap")
    if test_3 == True:
        print("False Positive: Reachability")
    if test_1 == True and test_2 == False and test_3 == False:
        print("Working as intended")


def load_test_dungeons(all_rooms, all_monsters):
    test_dungeons = []
    for specific_dungeon in files.test_dungeons_file.validity_dungeons:
        dungeon_goal = specific_dungeon["goal"]
        dungeon_rules = specific_dungeon["rules"]

        # get dungeon rooms as classes
        raw_rooms = specific_dungeon["rooms"]
        dungeon_rooms = []
        dungeon_rotations = {}
        for used_room in raw_rooms:
            room_name = used_room[0]
            room_side = used_room[1]
            room_rotation = used_room[2]
            for possible_room in all_rooms:
                if room_name == possible_room.name and room_side == possible_room.side:
                    dungeon_rooms.append(possible_room)
                    dungeon_rotations[possible_room] = room_rotation

        # change all connection names to their corresponding room classes
        dungeon_connections = specific_dungeon["connections"]
        for used_connection in dungeon_connections:
            for connected_room in dungeon_rooms:
                if used_connection[0] == connected_room.name:
                    room_a = connected_room
                if used_connection[2] == connected_room.name:
                    room_b = connected_room
            used_connection[0] = room_a
            used_connection[2] = room_b

        # get dungeon monsters
        dungeon_monsters = {}
        data_monsters = specific_dungeon["dungeon_monsters"]
        for used_monster in data_monsters:
            for possible_monster in all_monsters:
                if used_monster[0] == possible_monster.name:
                    dungeon_monsters[used_monster[0]] = [possible_monster, used_monster[1], used_monster[2]]

        dungeon_obstacles = specific_dungeon["obstacles"]
        dungeon_traps = specific_dungeon["traps"]
        dungeon_h_terrain = specific_dungeon["hazardous terrain"]
        dungeon_d_terrain = specific_dungeon["difficult terrain"]
        dungeon_chests = specific_dungeon["chests"]
        dungeon_coins = specific_dungeon["coins"]
        dungeon_theme = specific_dungeon["main theme"]
        dungeon_placements = specific_dungeon["placements"]
        dungeon_start = specific_dungeon["start"]

        test_dungeons.append(Dungeon(dungeon_goal, dungeon_rules, dungeon_rooms, dungeon_rotations, dungeon_connections, dungeon_monsters, dungeon_obstacles, dungeon_traps, dungeon_h_terrain, dungeon_d_terrain, dungeon_chests, dungeon_coins, dungeon_theme, dungeon_placements, dungeon_start))
    return test_dungeons


def test_output():
    all_rooms = load.load_rooms()
    all_monsters = load.load_monsters()
    all_dungeons = load.load_dungeon(all_rooms, all_monsters)
    output(all_dungeons[0])


def test_coordinates():
    all_rooms = load.load_rooms()
    all_monsters = load.load_monsters()
    all_dungeons = load.load_dungeon(all_rooms, all_monsters)
    black_barrow = all_dungeons[0]
    black_barrow.get_coordinates()
    coordinates = black_barrow.coordinates.copy()
    # print(coordinates)
    print(black_barrow.connection_coordinates)
    for coordinate in coordinates:
        if black_barrow.coordinates.count(coordinate) > 1:
            print(coordinate)


def test_validity_extended():
    all_rooms = load.load_rooms()
    all_monsters = load.load_monsters()
    all_dungeons = load.load_dungeon(all_rooms, all_monsters)
    validity_list = []
    for dungeon in all_dungeons:
        validity_test = check_validity(dungeon)
        validity_list.append(validity_test)
        print("one done")
    print(validity_list)


def test_rooms():
    test_rooms = load.load_rooms()
    for every_room in test_rooms:
        for every_coordinate in every_room.coordinates:
            room_sum = every_coordinate[0] + every_coordinate[1] + every_coordinate[2]
            if room_sum != 0:
                print("specific coordinate")
                print(every_room.name)
            if every_room.coordinates.count(every_coordinate) > 1:
                print("coordinate doubles")
                print(every_room.name)

# test_validity_extended()
