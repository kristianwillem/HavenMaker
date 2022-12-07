class Dungeon:

    def __init__(self, goal, rules, rooms, connections, dungeon_monsters, obstacles, traps, h_terrain, d_terrain, chests, coins, main_theme, placements, start):
        # string
        self.goal = goal

        # string
        self.rules = rules

        # dictionary (keys: room names, values: side (string), theme (sting))
        # making rooms into objects, and thus this into a list of objects, may work better.
        self.rooms = rooms

        # list of lists (roomA name, roomA coordinates, roomB name, roomB coordinates)
        self.connections = connections

        # dictionary (keys: monster names, values: normal amount, elite amount)
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



