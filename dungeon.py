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

    def get_coordinates:
        # add rooms through connections




