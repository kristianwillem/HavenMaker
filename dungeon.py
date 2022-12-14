import uf


class Dungeon:

    def __init__(self, goal, rules, rooms, connections, dungeon_monsters, obstacles, traps, h_terrain, d_terrain, chests, coins, main_theme, placements, start):
        # string
        self.goal = goal

        # set of strings
        self.rules = rules

        # list of Room objects
        # Something to keep in mind, these rooms are already rotated.
        # in reading the dungeon, it should copy the room classes and rotate the new ones.
        self.rooms = rooms

        # list of lists (roomA object, roomA coordinates, roomB object, roomB coordinates)
        self.connections = connections

        # dictionary (keys: monster names, values: [monster object, normal amount, elite amount])
        self.monsters = dungeon_monsters

        # int (amount)
        self.obstacles = obstacles

        # int (amount)
        self.traps = traps

        # int (amount)
        self.h_terrain = h_terrain

        # int (amount)
        self.d_terrain = d_terrain

        # list of strings
        self.chests = chests

        # int (amount)
        self.coins = coins

        # string
        self.theme = main_theme

        # dictionary (keys: names, values: coordinates (list of three ints))
        self.placements = placements

        # int
        self.start = start

        # list of coordinates
        self.coordinates = []
        self.get_coordinates()

    def get_coordinates(self):
        # add rooms through connections
        first_room = self.rooms[0]
        used_rooms = [first_room]
        self.coordinates = first_room.coordinates
        unused_connections = self.connections.copy
        while unused_connections:
            for connection in unused_connections:
                connect = False
                room_a = connection[0]
                room_b = connection[2]
                a_available = room_a in used_rooms
                b_available = room_b in used_rooms
                if a_available and b_available:
                    unused_connections.remove(connection)
                elif a_available:
                    old_room = room_a
                    old_coordinates = connection[1]
                    new_room = room_b
                    new_coordinates = connection[3]
                    connect = True
                elif b_available:
                    old_room = room_b
                    old_coordinates = connection[3]
                    new_room = room_a
                    new_coordinates = connection[1]
                    connect = True

                if connect:
                    difference = uf.subtract_coordinates(old_coordinates, new_coordinates)
                    for coordinate in new_room.coordinates:
                        dungeon_coordinate = uf.add_coordinates(coordinate, difference)
                        self.coordinates.append(dungeon_coordinate)
                    unused_connections.remove(connection)

                    # add difference to all other connections that come from the new room.
                    for other_connection in unused_connections:
                        if new_room == other_connection[0]:
                            other_connection[1] = uf.add_coordinates(other_connection[1], difference)
                        if new_room == other_connection[2]:
                            other_connection[3] = uf.add_coordinates(other_connection[3], difference)

        # start with the base room (first in the list)
        # make a copy of connections called "unused_connections"
        # while unused connections isn't empty:
        # for each connection:
        # check if either roomA or roomB is already in the list of rooms
        # if they both are, remove the connection
        # if only one is, get the coordinates of the other and remove the room from the list.
        # coordinates can be calculated with: add to each coordinate (old room connection - new room connection)



