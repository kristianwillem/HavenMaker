from dungeon import Dungeon
from mutation import Mutation
from fitness import Fitness
from validity import check_validity
import random
import load


def generate():

    # Initialize
    # This part loads all the necessary data for the program to function.
    # load rules, rooms, monsters
    all_rules = load.load_rules()
    all_rooms = load.load_rooms()
    all_monsters = load.load_monsters()
    all_chests = load.load_chests()
    ff = Fitness()

    # should hold dungeon files (their names at least)
    dungeons = []

    # load Dungeons
    population = []
    for name in dungeons:
        initial_dungeon = load.load_dungeon(name)
        fitness = ff.apply_fitness(initial_dungeon)
        population.append([initial_dungeon, fitness])

    sizes = []
    for dungeon_set in population:
        dungeon = dungeon_set[0]
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
    for iteration in range(100):
        parents = select_parents(population)
        new_dungeon = crossover(parents)
        new_dungeon = mutation.mutate(new_dungeon)
        fix(new_dungeon)
        valid = check_validity(new_dungeon)
        if valid:
            fitness = ff.apply_fitness(new_dungeon)
            population.append([new_dungeon, fitness])


def select_parents(possible_parents):
    parent_1 = 0
    parent_2 = 0
    while parent_1 == parent_2:
        parent_1 = select_parent(possible_parents)
        parent_2 = select_parent(possible_parents)
    return [parent_1, parent_2]


def select_parent(possible_parents):
    total_score = 0
    for entry in possible_parents:
        total_score += entry.score
    chosen_score = random.randrange(0, total_score)
    for entry in possible_parents:
        chosen_score -= entry.score
        if chosen_score << 0:
            return entry


def crossover(parents):
    crossover_list = []
    for category in ["rules", "map", "monsters", "environment", "treasure"]:
        crossover_list.append(random.randint(0, 1))
    new_goal = parents[crossover_list[0]].goal
    new_rules = parents[crossover_list[0]].rules
    new_rooms = parents[crossover_list[1]].rooms
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

    new_dungeon = Dungeon(new_goal, new_rules, new_rooms, new_connections, new_monsters, new_obstacles, new_traps, new_h_terrain, new_d_terrain, new_coins, new_chests, new_theme, new_placements, new_start)
    return new_dungeon


def fix(dungeon):
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

    for entry in dungeon.placements:
        component_count = components[entry]
        placement_count = len(dungeon.placements[entry])
        if component_count < placement_count:
            new_entry = random.choices(dungeon.placements[entry], k=component_count)
            dungeon.placements[entry] = new_entry

        # consider changing this to use difference instead of a while loop.
        while component_count > placement_count:
            # get all coordinates
            available_coordinates = dungeon.coordinates
            # remove filled coordinates
            for placement_type in dungeon.placements:
                for filled_coordinate in dungeon.placements[placement_type]:
                    available_coordinates.remove(filled_coordinate)
            # add a random empty coordinate
            new_entry = dungeon.placements[entry].copy()
            new_entry.append(random.choice(available_coordinates))
            dungeon.placements[entry] = new_entry
            placement_count = len(dungeon.placements[entry])


if __name__ == '__main__':
    generate()
