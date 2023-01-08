# These first two entries are not used and are intended as a sample template for adding more dungeons.

sample_dungeon_placement = {
    "monsters": [[0, 0, 0]],
    "obstacles": [[0, 0, 0]],
    "traps": [[0, 0, 0]],
    "hazardous terrain": [[0, 0, 0]],
    "difficult terrain": [[0, 0, 0]],
    "chests": [[0, 0, 0]],
    "coins": [[0, 0, 0]],
    "start": [[0, 0, 0]]
}

sample_dungeon = {
    "name": "Sample Name",
    "goal": "kill all enemies",
    "rules": ["sample rule"],
    "rooms": [["A1", "a", 0]],
    "connections": [["A1", [-1, 0, 1, 9, "exit"], "A2", [1, 0, -1, 3, "entry"]]],
    "dungeon_monsters": [["Bandit Guard", 1, 1]],
    "obstacles": 1,
    "traps": 1,
    "hazardous terrain": 1,
    "difficult terrain": 1,
    "chests": ["5 gold"],
    "coins": 1,
    "main theme": "Sample Theme",
    "placements": sample_dungeon_placement,
    "start": 4
}

black_barrow_placement = {
    "monsters": [[1, -2, 1], [2, -4, 2], [4, -2, -2], [5, -4, -1], [1, -3, 2], [10, -10, 0], [9, -10, 1], [9, -3, -6], [9, -8, -1], [8, -8, 0]],
    "obstacles": [[6, -7, 1], [7, -7, 0], [9, -7, -2], [10, -7, -3]],
    "hazardous terrain": [],
    "difficult terrain": [],
    "traps": [[6, -4, -2], [7, -4, -3]],
    "chests": [[7, -10, 3]],
    "coins": [[7, -9, 2], [6, -8, 2], [12, -10, -2], [11, -8, -3], [11, -9, -2]],
    "start": [[-3, -1, 4], [-3, -2, 5], [-2, -2, 4], [-2, -3, 5], [-1, -4, 5], [-2, -4, 6], [-1, -5, 6]]
}

black_barrow = {
    "name": "Black Barrow",
    "goal": "kill all enemies",
    "rules": [],
    "rooms": [["L1", "a", 3], ["G1", "b", 0], ["I1", "a", 3]],
    "connections": [["L1", [2, -3, 1, 3, "exit"], "G1", [-1, 1, 0, 9, "entry"]], ["G1", [4, -1, -3, 0, "exit"], "I1", [-3, 1, 2, 6, "entry"]]],
    "dungeon_monsters": [["Bandit Guard", 4, 1], ["Bandit Archer", 2, 1], ["Living Bones", 0, 2]],
    "obstacles": 4,
    "traps": 2,
    "hazardous terrain": 0,
    "difficult terrain": 0,
    "chests": ["replace"],
    "coins": 5,
    "main theme": "Dungeon",
    "placements": black_barrow_placement,
    "start": 7
}

crypt_of_the_damned_placement = {
    "monsters": [[-1, -1, 2], [-1, -2, 3], [-2, -1, 3], [-1, 2, -1], [-2, 4, -2], [-3, 3, 0], [1, 3, -4], [-2, 8, -6], [-8, 9, -1], [0, 8, -8], [-4, 10, -6]],
    "obstacles": [[0, 7, -7], [-1, 10, -9], [-3, 9, -6]],
    "traps": [[0, 0, 0], [-1, -3, 4], [-6, 6, 0], [-1, 7, -6], [-3, 11, -8]],
    "hazardous terrain": [],
    "difficult terrain": [],
    "chests": [[0, 9, -9], [-9, 8, 1]],
    "coins": [[0, 10, -10], [-1, 11, -10], [-2, 12, -10]],
    "start": [[1, -2, 1], [2, -3, 1], [1, -3, 2], [2, -4, 2], [1, -4, 3]]
}

crypt_of_the_damned = {
    "name": "Crypt of the Damned",
    "goal": "kill all enemies",
    "rules": [],
    "rooms": [["E1", "a", 3], ["G1", "b", 0], ["C1", "a", 0], ["M1", "a", 0]],
    "connections": [["E1", [-3, 1, 2, 6, "entry"], "G1", [2, -1, -1, 0, "exit"]], ["G1", [-1, 3, -2, 6, "entry"], "C1", [1, -1, 0, 0, "exit"]], ["G1", [5, 3, -8, 6, "entry"], "M1", [2, -1, -1, 0, "exit"]]],
    "dungeon_monsters": [["Living Bones", 1, 1], ["Bandit Archer", 3, 0], ["Cultist", 3, 0], ["Earth Demon", 0, 1], ["Wind Demon", 2, 0]],
    "obstacles": 3,
    "traps": 5,
    "hazardous terrain": 0,
    "difficult terrain": 0,
    "chests": ["replace", "replace"],
    "coins": 3,
    "main theme": "Dungeon",
    "placements": crypt_of_the_damned_placement,
    "start": 5
}

ruinous_crypt_placement = {
    "monsters": [[2, 2, -4], [1, 4, -5], [7, -6, -1], [-2, 12, -10], [-1, 5, -4], [1, 1, -2], [2, -4, 2], [3, -5, 2], [-5, 10, -5], [-5, 11, -6]],
    "obstacles": [[1, 3, -4]],
    "traps": [[-2, 6, -4], [-1, 6, -5], [1, 0, -1], [2, 0, -2]],
    "hazardous terrain": [],
    "difficult terrain": [[-3, 9, -6], [-4, 9, -5], [-6, 11, -5], [4, -3, -1], [3, -4, 1], [1, -4, 3]],
    "chests": [[-8, 12, -4], [1, -6, 5]],
    "coins": [[8, -7, -1], [7, -7, 0], [8, -6, -2], [-2, 13, -11], [-3, 13, -10], [-1, 12, -11]],
    "start": [[-3, 5, -2], [-3, 4, -1], [-2, 3, -1], [-2, 2, 0], [-1, 1, 0]]
}

ruinous_crypt = {
    "name": "Ruinous Crypt",
    "goal": "kill all enemies",
    "rules": ["All characters start with DISARM as a scenario effect"],
    "rooms": [["M1", "a", 0], ["K1", "a", 3], ["K2", "b", 0]],
    "connections": [["M1", [2, -1, -1, 0, "exit"], "K1", [-2, 1, 1, 6, "entry"]], ["M1", [-2, 7, -5, 6, "exit"], "K2", [2, -1, -1, 0, "entry"]]],
    "dungeon_monsters": [["Cultist", 2, 0], ["Living Bones", 0, 2], ["Night Demon", 2, 0], ["Flame Demon", 2, 0], ["Frost Demon", 2, 0]],
    "obstacles": 1,
    "traps": 4,
    "hazardous terrain": 0,
    "difficult terrain": 6,
    "chests": ["15 gold", "15 gold"],
    "coins": 6,
    "main theme": "Dungeon",
    "placements": ruinous_crypt_placement,
    "start": 5
}

temple_of_the_seer_placement = {
    "monsters": [[2, 3, -5], [2, 1, -3], [0, 5, -5], [5, 6, -11], [6, 0, -6], [8, 0, -8], [7, 1, -8], [8, 6, -14], [9, 3, -12]],
    "obstacles": [[6, 1, -7], [8, 1, -9], [10, 1, -11], [4, 5, -9], [6, 5, -11], [8, 5, -13], [10, 3, -13]],
    "traps": [[5, 1, -6], [6, 3, -9], [9, 4, -13]],
    "hazardous terrain": [],
    "difficult terrain": [],
    "chests": [[12, 0, -12]],
    "coins": [[10, 4, -14], [9, 5, -14], [9, 6, -15]],
    "start": [[-1, 1, 0], [-2, 2, 0], [-2, 3, -1], [-3, 4, -1], [-3, 5, -2]]
}

temple_of_the_seer = {
    "name": "Temple of the Seer",
    "goal": "kill all enemies",
    "rules": [],
    "rooms": [["M1", "a", 0], ["N1", "a", 3]],
    "connections": [["M1", [3, 3, -6, 3, "entry"], "N1", [-6, -3, 9, 9, "exit"]]],
    "dungeon_monsters": [["Stone Golem", 3, 0], ["Cave Bear", 0, 1], ["Living Spirit", 3, 0], ["Spitting Drake", 1, 1]],
    "obstacles": 7,
    "traps": 3,
    "hazardous terrain": 0,
    "difficult terrain": 0,
    "chests": ["10 experience"],
    "coins": 3,
    "main theme": "Dungeon",
    "placements": temple_of_the_seer_placement,
    "start": 5
}

frozen_hollow_placement = {
    "monsters": [[-2, 0, 2], [-3, 0, 3], [0, -1, 1], [-1, -1, 2], [10, -1, -9], [12, -8, -4], [8, 0, -8], [10, 0, -10], [3, -4, 1], [9, -9, 0], [10, -8, -2], [12, -7, -5], [9, 0, -9]],
    "obstacles": [[10, -9, -1], [9, -8, -1], [13, -6, -7], [13, -7, -6], [-1, -2, 3], [3, -3, 0], [8, -1, -7], [7, 1, -8], [8, -3, -5], [13, -3, -10], [11, -1, -10], [10, 1, -11]],
    "traps": [[7, 0, -7], [11, 0, -11]],
    "hazardous terrain": [],
    "difficult terrain": [],
    "chests": [[11, 1, -12]],
    "coins": [],
    "start": [[-1, -5, 6], [-2, -5, 7], [-3, -4, 7], [-2, -4, 6], [-3, -3, 6]]
}

frozen_hollow = {
    "name": "Frozen Hollow",
    "goal": "kill all enemies",
    "rules": ["Add three -1 cards to each character's attack modifier deck as a scenario effect"],
    "rooms": [["K1", "b", 3], ["K2", "a", 0], ["I2", "a", 3]],
    "connections": [["K1", [5, -5, 0, 2, "entry"], "K2", [-5, 5, 0, 8, "exit"]], ["K2", [1, 6, -7, 6, "entry"], "I2", [0, -5, 5, 0, "exit"]]],
    "dungeon_monsters": [["Hound", 5, 0], ["Living Spirit", 3, 1], ["Frost Demon", 3, 1]],
    "obstacles": 12,
    "traps": 2,
    "hazardous terrain": 0,
    "difficult terrain": 0,
    "chests": ["20 gold"],
    "coins": 0,
    "main theme": "Cave",
    "placements": frozen_hollow_placement,
    "start": 5
}

abandoned_sewers_placement = {
    "monsters": [[-1, 0, 1], [-1, -3, 4], [-9, 0, 9], [0, -1, 1], [-2, -2, 4], [-8, 0, 8], [-11, 0, 11], [-12, 0, 12], [-3, -14, 17], [-1, -14, 15], [-5, 0, 5], [-2, -14, 16], [-6, -6, 12], [-3, -10, 13], [-5, -12, 17], [-7, -6, 13], [-7, -10, 17]],
    "obstacles": [],
    "traps": [[-5, -13, 18]],
    "hazardous terrain": [],
    "difficult terrain": [[-2, 0, 2], [-1, -1, 2], [-1, -2, 3], [0, -3, 3], [0, -4, 4], [1, -5, 4], [-4, -1, 5], [-5, -1, 6], [-6, -1, 7], [-7, -1, 8], [-8, -1, 9], [-9, -1, 10], [-10, -1, 11], [-11, -1, 12], [-12, -1, 13], [-4, -8, 12], [-4, -9, 13], [-5, -9, 14], [-4, -10, 14], [-5, -10, 15], [-5, -11, 16], [-4, -12, 16], [-4, -11, 15], [-3, -11, 14]],
    "chests": [[-3, -12, 15]],
    "coins": [],
    "start": [[0, -6, 6], [1, -6, 5], [0, -5, 5], [-1, -5, 6], [-1, -4, 5]]
}

abandoned_sewers = {
    "name": "Abandoned Sewers",
    "goal": "kill all enemies",
    "rules": [],
    "rooms": [["H1", "b", 3], ["H3", "b", 3], ["M1", "a", 3]],
    "connections": [["H1", [-6, 0, 6, 9, "entry"], "H3", [1, 0, -1, 3, "exit"]], ["H3", [1, -7, 6, 0, "entry"], "M1", [-2, 1, 1, 6, "exit"]]],
    "dungeon_monsters": [["Giant Viper", 3, 3], ["Ooze", 4, 2], ["Vermling Scout", 3, 2]],
    "obstacles": 0,
    "traps": 1,
    "hazardous terrain": 0,
    "difficult terrain": 24,
    "chests": ["replace"],
    "coins": 0,
    "main theme": "Dungeon",
    "placements": abandoned_sewers_placement,
    "start": 5
}

magma_pit_placement = {
    "monsters": [[-3, 0, 3], [0, -2, 2], [-2, -1, 3], [-3, -2, 5], [-1, -8, 9], [3, -14, 11], [-2, -4, 6], [1, -8, 7], [-2, -5, 7], [2, -9, 7], [2, -14, 12], [1, -11, 10], [5, -16, 11]],
    "obstacles": [],
    "traps": [],
    "hazardous terrain": [[0, -8, 8], [1, -9, 8], [2, -10, 8], [1, -10, 9], [0, -9, 9], [-1, -9, 10], [5, -14, 9], [4, -14, 10], [4, -15, 11], [4, -16, 12], [3, -16, 13]],
    "difficult terrain": [],
    "chests": [[6, -17, 11]],
    "coins": [[4, -17, 13], [5, -17, 12], [5, -16, 11], [5, -15, 10]],
    "start": [[3, -3, 0], [4, -4, 0], [3, -4, 1], [4, -5, 1], [3, -5, 2]]
}

magma_pit = {
    "name": "Magma Pit",
    "goal": "kill all enemies",
    "rules": ["All characters start with WOUND as a scenario effect"],
    "rooms": [["K1", "b", 3], ["I2", "a", 0], ["D2", "b", 3]],
    "connections": [["K1", [-1, -6, 7, 0, "entry"], "I2", [0, 5, -5, 6, "exit"]], ["I2", [3, -1, -2, 0, "entry"], "D2", [-2, 1, 1, 6, "exit"]]],
    "dungeon_monsters": [["Vermling Scout", 4, 0], ["Inox Guard", 2, 2], ["Inox Archer", 3, 0], ["Fire Demon", 1, 1]],
    "obstacles": 0,
    "traps": 0,
    "hazardous terrain": 11,
    "difficult terrain": 0,
    "chests": ["replace"],
    "coins": 4,
    "main theme": "Cave",
    "placements": magma_pit_placement,
    "start": 5
}

underwater_lagoon_placement = {
    "monsters": [[-2, -1, 3], [2, -3, 1], [1, 3, -4], [2, 2, -4], [8, 0, -8], [1, -1, 0], [-1, 0, 1], [4, 4, -8], [4, 5, -9], [7, -3, -4], [0, 0, 0], [9, -7, -2], [11, -3, -8], [11, -8, -3], [10, -8, -2]],
    "obstacles": [],
    "traps": [[0, -2, 2], [-1, -1, 2], [1, -2, 1]],
    "hazardous terrain": [],
    "difficult terrain": [[1, 5, -6], [2, 4, -6], [3, 3, -6], [4, 3, -7], [5, 2, -7], [12, -4, -8], [11, -4, -7], [10, -4, -6], [9, -4, -5], [12, -5, -7], [11, -5, -6], [10, -5, -5], [9, -5, -4], [10, -6, -4], [11, -6, -5], [11, -7, -4], [12, -7, -5]],
    "chests": [[13, -7, -6]],
    "coins": [[12, -7, -5], [13, -8, -5]],
    "start": [[0, -3, 3], [0, -4, 4], [1, -4, 3], [-1, -3, 4]]
}

underwater_lagoon = {
    "name": "Underwater Lagoon",
    "goal": "kill all enemies",
    "rules": [],
    "rooms": [["D2", "b", 3], ["K1", "b", 3], ["M1", "b", 0]],
    "connections": [["D2", [1, 0, -1, 4, "entry"], "K1", [-3, -5, 8, 10, "exit"]], ["K1", [4, -6, 2, 0, "entry"], "M1", [-2, 7, -5, 6, "exit"]]],
    "dungeon_monsters": [["Ooze", 4, 1], ["Forest Imp", 5, 2], ["Rending Drake", 3, 0]],
    "obstacles": 0,
    "traps": 3,
    "hazardous terrain": 0,
    "difficult terrain": 17,
    "chests": ["replace"],
    "coins": 2,
    "main theme": "Cave",
    "placements": underwater_lagoon_placement,
    "start": 4
}

sunken_vessel_placement = {
    "monsters": [[2, -7, 5], [7, -10, 3], [10, -9, -1], [2, -4, 2], [9, -12, 3], [9, -3, -6], [10, -5, -5], [7, -3, -4], [13, -4, -9]],
    "obstacles": [[4, -9, 5], [6, -9, 3], [8, -11, 3], [7, -11, 4], [8, -12, 4], [10, -12, 2], [9, -10, 1], [11, -10, -1], [8, -4, -4], [7, -4, -3]],
    "traps": [[7, -5, -2], [7, -2, -5], [10, -4, -6]],
    "hazardous terrain": [[2, -3, 1], [2, -6, 4]],
    "difficult terrain": [[0, 0, 0], [0, -1, 1], [0, -2, 2], [0, -3, 3], [0, -4, 4], [0, -5, 5], [0, -6, 6], [0, -7, 7], [6, -6, 0], [6, -5, -1], [5, -4, -1], [5, -3, -2], [4, -2, -2]],
    "chests": [[14, -4, -10]],
    "coins": [[13, -3, -10], [12, -2, -10], [13, -2, -11], [14, -5, -9], [13, -5, -8], [12, -5, -7]],
    "start": [[0, -1, 1], [0, -2, 2], [0, -3, 3], [0, -4, 4], [0, -5, 5], [0, -6, 6]]
}

sunken_vessel = {
    "name": "Sunken Vessel",
    "goal": "kill all enemies",
    "rules": ["All characters start with IMMOBILIZE as a scenario effect"],
    "rooms": [["G1", "a", 4], ["K2", "a", 0], ["I1", "a", 3], ["B3", "a", 3]],
    "connections": [["G1", [3, -8, 5, 2, "entry"], "K2", [-5, 5, 0, 8, "exit"]], ["K2", [1, 6, -7, 6, "entry"], "I1", [0, -5, 5, 0, "exit"]], ["I1", [1, -1, 0, 3, "entry"], "B3", [-3, -1, 4, 9, "exit"]]],
    "dungeon_monsters": [["Lurker", 3, 1], ["Frost Demon", 2, 0], ["Living Spirit", 2, 1]],
    "obstacles": 10,
    "traps": 3,
    "hazardous terrain": 2,
    "difficult terrain": 13,
    "chests": ["replace"],
    "coins": 6,
    "main theme": "Cave",
    "placements": sunken_vessel_placement,
    "start": 6
}

available_dungeons = [black_barrow, crypt_of_the_damned, ruinous_crypt, temple_of_the_seer, frozen_hollow, abandoned_sewers, magma_pit, underwater_lagoon, sunken_vessel]
