import math

class Fitness:
    def __init__(self):
        self.difficulty_weight = 4
        self.size_weight = 1
        self.complexity_weight = 1
        self.theme_weight = 2
        self.clutter_weight = 2

        # there is no ideal for theme since more coherent is always better.
        # difficulty between 30 and 36 according to Isaac Childres
        # That value is halved for 2 players, but doubled for the difficulty system used.
        # value is set to 28 since the first dungeon only has a difficulty of 24.
        self.difficulty_ideal = 28
        self.size_ideal = 90
        self.complexity_ideal = 1
        self.clutter_ideal = 0.344
        # last one should be a number between 0 and 1

    def apply_fitness(self, dungeon):
        difficulty = self.difficulty_fitness(dungeon)
        size = self.size_fitness(dungeon)
        complexity = self.complexity_fitness(dungeon)
        theme = self.theme_fitness(dungeon)
        clutter = self.clutter_fitness(dungeon)
        total_fitness = self.difficulty_weight * difficulty + self.size_weight * size + self.complexity_weight * complexity + self.theme_weight * theme + self.clutter_weight * clutter
        all_scores = {
            "difficulty": difficulty,
            "size": size,
            "complexity": complexity,
            "theme" : theme,
            "clutter": clutter,
            "total score": total_fitness
        }
        return all_scores

    def difficulty_fitness(self, dungeon):
        difficulty_number = 0
        for monster_type in dungeon.monsters:
            monster_data = dungeon.monsters[monster_type]
            monster_class = monster_data[0]
            monster_amounts = [monster_data[1], monster_data[2]]
            monster_difficulty = monster_class.difficulty * (monster_amounts[0] + 2 * monster_amounts[1])
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
        # monsters
        # go through list of monsters, add themes to set
        monster_themes = set()
        for monster in dungeon.monsters:
            monster_class = dungeon.monsters[monster][0]
            monster_themes.add(monster_class.theme)
        # rooms
        # go through list of rooms, add themes to set
        room_themes = set()
        for room in dungeon.rooms:
            room_themes.add(room.theme)
        # get theme score
        # factorial is used to ensure that more deviancy from a single theme returns a significantly lower score.
        theme_number = math.factorial(len(monster_themes)) + math.factorial(len(room_themes)) - 2
        if theme_number > 20:
            theme_score = 0
        else:
            theme_score = 1 - (theme_number/20)
        return theme_score

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




