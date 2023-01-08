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

    def __eq__(self, other):
        return self.name == other.name

    def rotate(self, angle):
        # change the coordinates and links because of rotation.
        # rotation in steps of 60 degrees. Base of every room is 0.
        rotated_coordinates = self.coordinates.copy()
        rotated_links = self.links.copy()
        for step in range(angle):
            for i in range(len(rotated_coordinates)):
                oc = rotated_coordinates[i]
                coordinate = [-oc[1], -oc[2], -oc[0]]
                rotated_coordinates[i] = coordinate
            for i in range(len(rotated_links)):
                link = rotated_links[i]
                oc = link[0:3]
                link_direction = (link[3]+2) % 12
                link_type = link[4]
                rotated_links[i] = [-oc[1], -oc[2], -oc[0], link_direction, link_type]
        return rotated_coordinates, rotated_links

    def __hash__(self):
        return id(self)
