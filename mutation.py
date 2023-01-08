import random
import uf
import validity


class Mutation:

    def __init__(self, all_rules, all_rooms, all_monsters, all_chests, min_size, max_size):
        self.all_rules = all_rules
        self.all_rooms = all_rooms
        self.all_monsters = all_monsters
        self.all_chests = all_chests
        self.min_size = min_size
        self.max_size = max_size

        self.rule_chance_base = 0.8
        self.chest_chance_base = 0.8
        self.monster_theme_bias = 2
        self.room_theme_bias = 4

        # probably at 0.5 or so
        self.mutation_chance = 0.75
        self.ensure_proper_map = True

    def mutate(self, dungeon):
        # randomly mutate, each mutation has a 25% chance to apply.
        random_mutations = []
        for i in range(5):
            if random.random() < self.mutation_chance:
                random_mutations.append(True)
            else:
                random_mutations.append(False)

        if random_mutations[0]:
            self.mutate_rules(dungeon)
        if random_mutations[1]:
            self.mutate_monsters(dungeon)
        if random_mutations[2]:
            self.mutate_environment(dungeon)
        if random_mutations[3]:
            self.mutate_treasure(dungeon)

        # While it is usually at another place, I've moved the map mutation to the bottom since it also mutates the
        # "Placement" attribute, which depends on all other attributes.
        if random_mutations[4]:
            self.mutate_map(dungeon)

        if self.ensure_proper_map:
            proper_map = validity.overlap_check(dungeon)
            while not proper_map:
                self.mutate_map(dungeon)
                proper_map = validity.overlap_check(dungeon)

    # for a more advanced (non-MVP) version:
    # gaussian distribution with the ideal as mean and a (variable) standard deviation.
    # every step, test the current value against the ideal value.

    def mutate_rules(self, dungeon):
        rule_chance = self.rule_chance_base
        dungeon.rules = set(())
        mutate_loop = True
        while mutate_loop:
            rule_test = random.random()
            if rule_test < rule_chance:
                new_rule = random.choice(self.all_rules)
                dungeon.rules.add(new_rule)
                rule_chance /= 2
            else:
                mutate_loop = False

    def mutate_monsters(self, dungeon):
        # get monster_difficulty (total difficulty of all monsters) and monster_number (number of different monsters)
        # remove old dictionary
        # choose new (biased) monster_difficulty and monster_number. (difficulty should not change too much)
        # (min monster_number to 2)
        # choose a new monster (randomly)
        # choose a number of new monsters with bias to first monster's type.
        # divide the difficulty to choose new monsters
        # rebuild the dungeon.monster dictionary

        monster_difficulty = 0
        for monster_type in dungeon.monsters:
            monster_data = dungeon.monsters[monster_type]
            monster_class = monster_data[0]
            monster_amounts = [monster_data[1], monster_data[2]]
            monster_difficulty += monster_class.difficulty * (monster_amounts[0] + 2 * monster_amounts[1])
        monster_number = len(dungeon.monsters)

        dungeon.monsters = dict()

        # randomize difficulty
        mu = monster_difficulty
        sigma = monster_difficulty / 8
        new_difficulty = round(random.normalvariate(mu, sigma))
        if new_difficulty < 10:
            new_difficulty = 10

        # randomize numbers
        mu = monster_number
        sigma = monster_number / 4
        new_number = round(random.normalvariate(mu, sigma))
        if new_number < 2:
            new_number = 2

        # grab new monsters, add one normal of each.
        current_difficulty = 0
        new_dungeon_monsters = []
        monster_type_list = []
        for i in range(new_number):
            if i == 0:
                # choose first monster
                new_monster_type = random.choice(self.all_monsters)
                dungeon_monster_theme = new_monster_type.theme
            else:
                # choose additional monsters
                theme_weight = []
                for entry in self.all_monsters:
                    if entry.theme == dungeon_monster_theme:
                        theme_weight.append(self.monster_theme_bias)
                    else:
                        theme_weight.append(1)
                new_monster_type = 0
                while new_monster_type in monster_type_list or new_monster_type == 0:
                    new_monster_type = random.choices(self.all_monsters, theme_weight)[0]
            # do the basics
            current_difficulty += new_monster_type.difficulty
            new_monster = [new_monster_type, 1, 0]
            monster_type_list.append(new_monster_type)
            new_dungeon_monsters.append(new_monster)

        while current_difficulty < new_difficulty:
            # choose a random monster
            # 50/50 chance of; adding a normal or changing a normal into an elite (if any normal are present)
            added_monster = random.choice(new_dungeon_monsters)
            add_elite = random.randint(0, 1)
            if add_elite == 1 and added_monster[1] > 0:
                added_monster[1] = added_monster[1] - 1
                added_monster[2] = added_monster[2] + 1
            else:
                added_monster[1] = added_monster[1] + 1
            current_difficulty += added_monster[0].difficulty

        for monster_entry in new_dungeon_monsters:
            monster_class = monster_entry[0]
            monster_name = monster_class.name
            dungeon.monsters[monster_name] = monster_entry

    def mutate_environment(self, dungeon):
        # using gaussian to create a 95% chance that the new number will be between 0.5 and 1.5 times the original.
        environment_list = [dungeon.obstacles, dungeon.traps, dungeon.h_terrain, dungeon.d_terrain]
        for i in range(len(environment_list)):
            mu = environment_list[i]
            if mu == 0:
                sigma = 1
            else:
                sigma = mu/4
            new_entry = round(random.normalvariate(mu, sigma))
            environment_list[i] = abs(new_entry)
        dungeon.obstacles = environment_list[0]
        dungeon.traps = environment_list[1]
        dungeon.h_terrain = environment_list[2]
        dungeon.d_terrain = environment_list[3]

    def mutate_treasure(self, dungeon):
        # new amount of coins, similar to environment
        coin_amount = dungeon.coins
        mu = coin_amount
        if mu == 0:
            sigma = 1
        else:
            sigma = coin_amount/4
        new_coins = round(random.normalvariate(mu, sigma))
        dungeon.coins = abs(new_coins)

        # new treaure, similar to rules
        chest_chance = self.chest_chance_base
        dungeon.chests = []
        mutate_loop = True
        while mutate_loop:
            chest_test = random.random()
            if chest_test < chest_chance:
                new_chest = random.choice(self.all_chests)
                dungeon.chests.append(new_chest)
                chest_chance /= 2
            else:
                mutate_loop = False

    def mutate_map(self, dungeon):
        # room & connection randomization
        dungeon.rooms = []
        dungeon.theme = "None"
        dungeon.room_rotations.clear()
        dungeon.connections = []
        open_links = dict()
        size = 0
        mutate_loop = True
        while mutate_loop:
            # select random room
            theme_weight = []
            for entry in self.all_rooms:
                if entry.theme == dungeon.theme:
                    theme_weight.append(self.room_theme_bias)
                else:
                    theme_weight.append(1)
            new_room = random.choices(self.all_rooms, theme_weight)[0]
            valid_room = True

            if not dungeon.rooms:
                dungeon.theme = new_room.theme
                new_connection = []
                new_rotation = 0
            else:
                # check if the room is available
                for other_room in dungeon.rooms:
                    if other_room == new_room:
                        valid_room = False

                # connect new room (all possible connections)
                chosen_connection = self.connect(open_links, new_room)
                if chosen_connection:
                    old_room = chosen_connection[0]
                    old_link = chosen_connection[1]
                    new_link = chosen_connection[2]
                    link_rotation = (old_link[3] - new_link[3] + 6)/2
                    link_rotation = link_rotation % 6
                    if link_rotation < 0:
                        link_rotation += 6
                    new_rotation = int(link_rotation)
                    new_link = uf.link_rotate(new_link, new_rotation)
                    new_connection = [old_room, old_link, new_room, new_link]
                else:
                    valid_room = False

            if valid_room:
                size += new_room.hexes
                dungeon.rooms.append(new_room)
                # add the room rotation
                dungeon.room_rotations[new_room] = new_rotation
                # add and rotate new links
                new_links = new_room.links.copy()
                rotated_links = []
                for link in new_links:
                    rotated_link = uf.link_rotate(link, new_rotation)
                    rotated_links.append(rotated_link)
                open_links[new_room] = rotated_links

                if new_connection:
                    # remove connector link of the old room
                    dungeon.connections.append(new_connection)
                    old_room_links = open_links[new_connection[0]]
                    old_room_links.remove(new_connection[1])
                    open_links[new_connection[0]] = old_room_links

                    # remove connector link of the new room
                    new_room_links = open_links[new_room]
                    new_room_links.remove(new_link)
                    open_links[new_room] = new_room_links

                # choose whether to continue
                if size > self.max_size:
                    mutate_loop = False
                elif size > self.min_size:
                    if random.random() > 0.5:
                        mutate_loop = False

                if not open_links.values():
                    mutate_loop = False

        # placement randomization
        self.mutate_placement(dungeon)

    def connect(self, open_links, new_room):
        possible_connections = []
        # check possible connections:
        # for each room, check for all its links with this room's links whether they can connect.
        for old_room in open_links:
            for old_link in open_links[old_room]:
                for new_link in new_room.links:
                    if (old_link[3] % 2 == new_link[3] % 2) and (old_link[4] != new_link[4]):
                        # add this as a possible connection.
                        possible_connections.append([old_room, old_link, new_link])
        if not possible_connections:
            return 0
        else:
            chosen_connection = random.choice(possible_connections)
            return chosen_connection

    def mutate_placement(self, dungeon):
        dungeon.placements = dict()
        dungeon.get_coordinates()
        possible_coordinates = dungeon.coordinates.copy()

        dungeon.start = 4
        looking_for_start = True
        while looking_for_start:
            other_starts = []
            random_start = random.choice(possible_coordinates)
            for other in possible_coordinates:
                if uf.is_adjacent(random_start, other):
                    other_starts.append(other)
            if len(other_starts) < 6:
                looking_for_start = False

        certain_starts = [random_start]

        # while we don't have enough start locations, get more.
        while len(other_starts) + len(certain_starts) < dungeon.start:
            extra_start = random.choice(other_starts)
            other_starts.remove(extra_start)
            certain_starts.append(extra_start)
            for other in possible_coordinates:
                if uf.is_adjacent(extra_start, other) and other not in other_starts and other not in certain_starts:
                    other_starts.append(other)

        all_starts = certain_starts
        for i in range(dungeon.start - len(certain_starts)):
            extra_start = random.choice(other_starts)
            other_starts.remove(extra_start)
            all_starts.append(extra_start)
        dungeon.placements["start"] = all_starts

        # remove the starts from the possible coordinates
        for used_coordinate in all_starts:
            possible_coordinates.remove(used_coordinate)

        # create a "component" dictionary that basically copies the placement dictionary, except for start.
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

        entry_list = ["monsters", "obstacles", "traps", "hazardous terrain", "difficult terrain", "chests", "coins"]
        for entry in entry_list:
            component_count = components[entry]
            # get a number of random available coordinates equal to the component count
            # then remove them from the available list
            # new_coordinates = random.choices(possible_coordinates, k=component_count)
            new_coordinates = []
            for i in range(component_count):
                chosen_coordinate = random.choice(possible_coordinates)
                possible_coordinates.remove(chosen_coordinate)
                new_coordinates.append(chosen_coordinate)
            dungeon.placements[entry] = new_coordinates
