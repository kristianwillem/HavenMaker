import random

def mutate(dungeon):
    # use random(choices) to randomize this
    mutate_rules(dungeon)
    mutate_map(dungeon)
    mutate_monsters(dungeon)
    mutate_environment(dungeon)
    mutate_treasure(dungeon)

# for a more advanced (non-MVP) version:
# gaussian distribution with the ideal as mean and a (variable) standard deviation.
# every step, test the current value against the ideal value.

def mutate_rules(dungeon):
    rulechance = 0.8
    dungeon.rules = []
    mutate_loop = True
    while mutate_loop:
        ruletest = random.random()
        if ruletest < rulechance:
            # step to get random rule from rule list
            dungeon.rules.append(new_rule)
            rulechance /= 2
        else:
            mutate_loop = False

def mutate_map(dungeon):
    # room randomization
    dungeon.rooms = []
    dungeon.theme = ''
    size_range = [X,Y]
    size = 0
    mutate_loop = True
    while mutate_loop:
        # select random room
        new_room = random.choice(rooms)
        size += new_room.size
        dungeon.rooms.append(new_room)
        if dungeon.theme == '':
            dungeon.theme = new_room.theme

        # choose whether to continue
        if size > size_range[1]:
            mutate_loop = False
        elif size > size_range[0]:
            if random.random() > 0.5:
                mutate_loop = False

    # connection randomization

    # placement randomization

def mutate_monsters(dungeon):
    for monster_type in dungeon.monsters:
        # select random monster from same monster.theme

def mutate_environment(dungeon):


def mutate_treasure(dungeon):
