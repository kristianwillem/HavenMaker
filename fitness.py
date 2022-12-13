class Fitness:
    def __init__(self):
        self.difficulty_weight = 4
        self.size_weight = 1
        self.complexity_weight = 1
        self.theme_weight = 2
        self.clutter_weight = 2

        # there is no ideal for theme since more coherent is always better.
        self.difficulty_ideal = X
        self.size_ideal = X
        self.complexity_ideal = X
        self.clutter_ideal = X
        # last one should be a fraction

    def apply_fitness(self, dungeon):
        difficulty = self.difficulty_fitness(dungeon)
        size = self.size_fitness(dungeon)
        complexity = self.complexity_fitness(dungeon)
        theme = self.theme_fitness(dungeon)
        clutter = self.clutter_fitness(dungeon)
        total_fitness = self.difficulty_weight * difficulty + self.size_weight * size + self.complexity_weight * complexity + self.theme_weight * theme + self.clutter_weight * clutter
        return total_fitness

    def difficulty_fitness(self, dungeon):
        difficulty_number = 0
        for monster_type in dungeon.monsters:
            monster_amounts = dungeon.monsters[monster_type]
            monster_difficulty = monster_type.difficulty * (monster_amounts[0] + 2 * monster_amounts[1])
            difficulty_number += monster_difficulty
        # create difficulty_score from difficulty_number and ideal_difficulty
        # score = 0 if number-ideal = ideal, and 1 if number-ideal = 0
        difficulty_score = 1 - (abs(self.difficulty_ideal-difficulty_number)/self.difficulty_ideal)
        if difficulty_score < 0:
            difficulty_score = 0
        return difficulty_score

    def size_fitness(self, dungeon):
        size_number = 0
        for room in dungeon.rooms:
            size_number += room.hexes
        size_score = 1 - (abs(self.size_ideal-size_number)/self.size_ideal)
        if size_score < 0:
            size_score = 0
        return size_score

    def complexity_fitness(self, dungeon):
        complexity_number = len(dungeon.rules)
        complexity_score = 1 - (abs(self.complexity_ideal-complexity_number)/self.complexity_ideal)
        if complexity_score < 0:
            complexity_score = 0
        return complexity_score

    def theme_fitness(self, dungeon):
        theme_number = 0

        # get theme numbers

        # get theme score

    def clutter_fitness(self, dungeon):
        # get filled hexes from placement
        filled_hexes = 0
        for hexes in dungeon.placements.values():
            filled_hexes += len(hexes)
        # get total hexes from coordinates
        total_hexes = len(dungeon.coordinates)

        clutter_number = filled_hexes/total_hexes
        clutter_score = 1 - (abs(self.clutter_ideal-clutter_number)/self.clutter_ideal)
        if clutter_score < 0:
            clutter_score = 0
        return clutter_score




