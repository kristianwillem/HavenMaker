import uf


class Dungeon:

    def __init__(self, goal, rules, rooms, rotations, connections, dungeon_monsters, obstacles, traps, h_terrain, d_terrain, chests, coins, main_theme, placements, start):
        # string
        self.goal = goal

        # set of strings
        self.rules = rules

        # list of Room objects
        self.rooms = rooms

        # dictionary (keys: room objects, values: rotations)
        self.room_rotations = rotations

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
        self.connection_coordinates = []

        self.get_coordinates()

        # dungeon fitness score
        self.score = 0

        self.specific_scores = dict()

    def get_coordinates(self):
        # add rooms through connections (alternate way)
        room_coordinates = dict()
        connection_references = dict()
        for room in self.rooms:
            room_rotation = self.room_rotations[room]
            rotated_coordinates = room.rotate(room_rotation)[0]
            room_coordinates[room] = rotated_coordinates
        for connection in self.connections:
            room_a = connection[0]
            room_b = connection[2]
            # remove this; connections are already rotated.
            # link_a = uf.link_rotate(connection[1], self.room_rotations[room_a])
            # link_b = uf.link_rotate(connection[3], self.room_rotations[room_b])
            link_a = connection[1]
            link_b = connection[3]

            connection_references[(room_a, room_b)] = [link_a, link_b]

        self.coordinates = []
        self.connection_coordinates = []
        first_room = self.rooms[0]
        used_rooms = [first_room]
        self.coordinates.extend(room_coordinates[first_room])
        unused_connections = []
        for pair in connection_references:
            unused_connections.append(pair)

        while unused_connections:
            for connection in unused_connections:
                connect = False
                room_a = connection[0]
                room_b = connection[1]
                coordinate_pair = connection_references[connection]
                a_available = room_a in used_rooms
                b_available = room_b in used_rooms
                if a_available and b_available:
                    unused_connections.remove(connection)
                elif a_available:
                    old_room = room_a
                    old_coordinates = coordinate_pair[0]
                    new_room = room_b
                    new_coordinates = coordinate_pair[1]
                    connect = True
                elif b_available:
                    old_room = room_b
                    old_coordinates = coordinate_pair[1]
                    new_room = room_a
                    new_coordinates = coordinate_pair[0]
                    connect = True

                if connect:
                    difference = uf.subtract_coordinates(old_coordinates, new_coordinates)
                    for coordinate in room_coordinates[new_room]:
                        dungeon_coordinate = uf.add_coordinates(coordinate, difference)
                        self.coordinates.append(dungeon_coordinate)
                    unused_connections.remove(connection)
                    # add connection coordinates
                    self.connection_coordinates.append(old_coordinates[0:3])

                    # add difference to all other connections that come from the new room.
                    for other_connection in unused_connections:
                        if new_room == other_connection[0]:
                            old_connection = connection_references[other_connection]
                            new_a = uf.add_coordinates(old_connection[0], difference)
                            new_connection = [new_a, old_connection[1]]
                            connection_references[other_connection] = new_connection

                        if new_room == other_connection[1]:
                            old_connection = connection_references[other_connection]
                            new_b = uf.add_coordinates(old_connection[1], difference)
                            new_connection = [old_connection[0], new_b]
                            connection_references[other_connection] = new_connection

                    used_rooms.append(new_room)

        # start with the base room (first in the list)
        # make a copy of connections called "unused_connections"
        # while unused connections isn't empty:
        # for each connection:
        # check if either roomA or roomB is already in the list of rooms
        # if they both are, remove the connection
        # if only one is, get the coordinates of the other and remove the room from the list.
        # coordinates can be calculated with: add to each coordinate (old room connection - new room connection)

    def __gt__(self, other):
        return self.score > other.score
