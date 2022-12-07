from dungeon import Dungeon
from mutation import mutate
from fitness import apply_fitness
import random
import pandas

def generate():

    # Initialize
    # This part loads all the necessary data for the program to function.

    #should hold dungeon files (their names at least)
    dungeons = []

    # load Dungeons

    population = []
    for name in dungeons:
        initial_dungeon = load_dungeon(name)
        fitness = apply_fitness(initial_dungeon)
        population.append([initial_dungeon, fitness])


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
