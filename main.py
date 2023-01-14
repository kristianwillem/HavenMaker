from dungeon import Dungeon
from mutation import Mutation
from fitness import Fitness
from validity import check_validity
import random
import load
from output import output


def generate():
    cycles = 20
    output_test_dungeons = True
    # Initialize
    # This part loads all the necessary data for the program to function.
    # load rules, rooms, monsters, and chests
    all_rules = load.load_rules()
    all_rooms = load.load_rooms()
    all_monsters = load.load_monsters()
    all_chests = load.load_chests()
    ff = Fitness()

    # load Dungeons
    population = []
    initial_dungeons = load.load_dungeon(all_rooms, all_monsters)
    for specific_dungeon in initial_dungeons:
        fitness_scores = ff.apply_fitness(specific_dungeon)
        specific_dungeon.specific_scores = fitness_scores
        specific_dungeon.score = fitness_scores["total score"]
        population.append(specific_dungeon)

    sizes = []
    for dungeon in population:
        dungeon_size = len(dungeon.connections)
        for room in dungeon.rooms:
            dungeon_size += room.hexes
        sizes.append(dungeon_size)

    min_size = min(sizes)
    max_size = max(sizes)

    # initialize mutation
    # Mutation should be initialized after the Dungeons since min_size/max_size depends on it.
    mutation = Mutation(all_rules, all_rooms, all_monsters, all_chests, min_size, max_size)

    # Evolutionary Loop
    # This part runs the evolutionary cycle.
    for iteration in range(cycles):
        parents = select_parents(population)
        new_dungeon = crossover(parents)
        mutation.mutate(new_dungeon)
        fix(new_dungeon, all_chests)
        valid = check_validity(new_dungeon)
        if valid:
            fitness_scores = ff.apply_fitness(new_dungeon)
            new_dungeon.specific_scores = fitness_scores
            new_dungeon.score = fitness_scores["total score"]
            population.append(new_dungeon)

    for initial in initial_dungeons:
        population.remove(initial)

    if output_test_dungeons:
        # in outputting test dungeons, the highest dungeon should be the output, and the different scores for the
        # dungeon, (as well as their total score), should be output as well.
        population.sort()
        best_dungeon = population[-1]
        output(best_dungeon)
        print("\n")
        print(best_dungeon.specific_scores)

    else:
        # sort the list and output the top three dungeons (in ascending order)
        population.sort()
        print("\n")
        output(population[-3])
        print("\n")
        output(population[-2])
        print("\n")
        output(population[-1])

        print("\n")
        print(population[0].score)
        print(population[-1].score)


def select_parents(possible_parents):
    parent_1 = 0
    parent_2 = 0
    while parent_1 == parent_2:
        parent_1 = select_parent(possible_parents)
        parent_2 = select_parent(possible_parents)
    return [parent_1, parent_2]


def select_parent(possible_parents):
    # number between 0 and 1 to offset the minimum fitness score.
    selection_bias = 0.5
    total_score = 0
    # determine lowest score
    lowest_score = 100
    for dungeon in possible_parents:
        if dungeon.score < lowest_score:
            lowest_score = dungeon.score

    for dungeon in possible_parents:
        # this is a quick and dirty solution. It might be better to improve this at some time.
        # possible cleaner solution uses "random.uniform" (the float variant of randrange)
        total_score += (dungeon.score - lowest_score * selection_bias)
    chosen_score = random.uniform(0, total_score)
    for dungeon in possible_parents:
        chosen_score -= (dungeon.score - lowest_score * selection_bias)
        if chosen_score < 0:
            return dungeon


def crossover(parents):
    crossover_list = []
    for category in ["rules", "map", "monsters", "environment", "treasure"]:
        crossover_list.append(random.randint(0, 1))
    new_goal = parents[crossover_list[0]].goal
    new_rules = parents[crossover_list[0]].rules
    new_rooms = parents[crossover_list[1]].rooms
    new_rotations = parents[crossover_list[1]].room_rotations.copy()
    new_connections = parents[crossover_list[1]].connections
    new_theme = parents[crossover_list[1]].theme
    new_placements = parents[crossover_list[1]].placements
    new_start = parents[crossover_list[1]].start
    new_monsters = parents[crossover_list[2]].monsters
    new_obstacles = parents[crossover_list[3]].obstacles
    new_traps = parents[crossover_list[3]].traps
    new_h_terrain = parents[crossover_list[3]].h_terrain
    new_d_terrain = parents[crossover_list[3]].d_terrain
    new_chests = parents[crossover_list[4]].chests
    new_coins = parents[crossover_list[4]].coins

    new_dungeon = Dungeon(new_goal, new_rules, new_rooms, new_rotations, new_connections, new_monsters, new_obstacles, new_traps, new_h_terrain, new_d_terrain, new_chests, new_coins, new_theme, new_placements, new_start)
    return new_dungeon


def fix(dungeon, all_chests):
    # create a "component" dictionary that basically copies the placement dictionary.
    components = dict()
    monster_count = 0
    for monster_type in dungeon.monsters:
        type_values = dungeon.monsters[monster_type]
        monster_count += type_values[1]
        monster_count += type_values[2]
    components["monsters"] = monster_count
    components["obstacles"] = dungeon.obstacles
    components["traps"] = dungeon.traps
    components["hazardous terrain"] = dungeon.h_terrain
    components["difficult terrain"] = dungeon.d_terrain
    components["chests"] = len(dungeon.chests)
    components["coins"] = dungeon.coins
    components["start"] = dungeon.start
    dungeon.get_coordinates()

    old_placement = dungeon.placements.copy()
    dungeon.placements = dict()

    entry_list = ["start", "monsters", "obstacles", "traps", "hazardous terrain", "difficult terrain", "chests", "coins"]
    for entry in entry_list:
        component_count = components[entry]
        placement_count = len(old_placement[entry])
        if component_count < placement_count:
            original_entry = old_placement[entry].copy()
            new_entry = []
            for i in range(component_count):
                random_entry = random.choice(original_entry)
                new_entry.append(random_entry)
                original_entry.remove(random_entry)

        elif component_count > placement_count:
            placement_add = component_count - placement_count
            # get all coordinates
            available_coordinates = dungeon.coordinates.copy()
            # remove filled coordinates
            for placement_type in old_placement:
                for filled_coordinate in old_placement[placement_type]:
                    if filled_coordinate in available_coordinates:
                        available_coordinates.remove(filled_coordinate)
            added_coordinates = []
            for i in range(placement_add):
                # add a random empty coordinate
                new_coordinate = random.choice(available_coordinates)
                added_coordinates.append(new_coordinate)
                available_coordinates.remove(new_coordinate)
            new_entry = old_placement[entry]
            new_entry.extend(added_coordinates)

        else:
            new_entry = old_placement[entry].copy()

        dungeon.placements[entry] = new_entry

    new_chests = []
    for chest in dungeon.chests:
        if chest == "replace":
            new_chests.append(random.choice(all_chests))
        else:
            new_chests.append(chest)
    dungeon.chests = new_chests


if __name__ == '__main__':
    generate()
