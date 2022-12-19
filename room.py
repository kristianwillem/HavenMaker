class Room:

    def __init__(self, name, side, theme, coordinates, links, hexes):
        self.name = name
        self.side = side
        self.theme = theme
        self.coordinates = coordinates

        # combined entries/exits into links
        # links in the form of [coordinates (list), direction (int), type (string)]
        # for example: [[-1,0,1], 9, "exit"]
        self.links = links
        self.hexes = hexes

        # rotation in steps of 60 degrees. Base of every room is 0.
        self.rotation = 0

    def __eq__(self, other):
        return self.name == other.name

    def rotate(self, angle):
        # change the coordinates and links because of rotation.
        for step in range(angle):
            for coordinate in self.coordinates:
                oc = coordinate.copy()
                coordinate = [-oc[1], -oc[2], -oc[0]]
            for link in self.links:
                link_coordinates = link[0]
                oc = link_coordinates.copy()
                link[0] = [-oc[1], -oc[2], -oc[0]]
            self.rotation = (self.rotation+1) % 6
