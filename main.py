from dungeon import Dungeon
from mutation import mutate
from fitness import apply_fitness
import random
import pandas

def generate():

    # Initialize
    # This part loads all the necessary data for the program to function.

    # load rules, rooms, monsters

    #should hold dungeon files (their names at least)
    dungeons = []

    # load Dungeons
    population = []
    for name in dungeons:
        initial_dungeon = load_dungeon(name)
        fitness = apply_fitness(initial_dungeon)
        population.append([initial_dungeon, fitness])

    # initialize mutation
    # Mutation should be initialized after the Dungeons since min_size/max_size depends on it.


    # Evolutionary Loop
    # This part runs the evolutionary cycle.
    for iteration in range(100):
        parents = select_parents(population)
        new_dungeon = crossover(parents)
        new_dungeon = mutate(new_dungeon)
        new_dungeon = fix(new_dungeon)
        valid = validity(new_dungeon)
        if valid:
            fitness = apply_fitness(new_dungeon)
            population.append([new_dungeon, fitness])


def load_dungeon(dungeon_name):
    file_name = dungeon_name + ".glm"
    dungeon_data = pandas.read_csv(file_name)

    goal_data = dungeon_data.iat[0, 0]
    rules_data = dungeon_data.iat[1, 0]
    rooms_data = dungeon_data.iat[2, 0]
    connections_data = dungeon_data.iat[3, 0]
    monster_data = dungeon_data.iat[4, 0]
    obstacles_data = dungeon_data.iat[5, 0]
    traps_data = dungeon_data.iat[6, 0]
    h_terrain_data = dungeon_data.iat[7, 0]
    d_terrain_data = dungeon_data.iat[8, 0]
    chest_data = dungeon_data.iat[9, 0]
    coins_data = dungeon_data.iat[10, 0]
    theme_data = dungeon_data.iat[11, 0]
    placements_data = dungeon_data.iat[12, 0]
    start_data = dungeon_data.iat[13, 0]


    new_dungeon = Dungeon(goal_data, rules_data, rooms_data, connections_data, monster_data, obstacles_data, traps_data, h_terrain_data, d_terrain_data, chest_data, coins_data, theme_data, placements_data, start_data)
    return new_dungeon

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
    # how to get this to work (specifically; referring to a specific attribute of a class that has the same name as a variable)
    for entry in dungeon.placement.keys():
        if dungeon.placement[entry] > dungeon.entry:


def validity(dungeon):





if __name__ == '__main__':
    generate()
