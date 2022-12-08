class Room:

    def __init__(self, name, side, theme, coordinates, entries, exits, hexes):
        self.name = name
        self.side = side
        self. theme = theme
        self.coordinates = coordinates
        self.entries = entries
        self.exits = exits
        self.hexes = hexes

    def __eq__(self, other):
        return self.name == other.name
