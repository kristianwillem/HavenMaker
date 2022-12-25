# This file is not part of the program, and exists only to test other parts of the project.

# import dungeon
# import fitness
import load
# import main
# import monster
# import mutation
# import room
# import uf
# import validity


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
