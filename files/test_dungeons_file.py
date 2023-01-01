dungeon_1_placement = {
    "monsters": [[3, 0, -3]],
    "obstacles": [],
    "traps": [],
    "hazardous terrain": [],
    "difficult terrain": [],
    "chests": [],
    "coins": [],
    "start": [[0, 0, 0]]
}

dungeon_1 = {
    "name": "Test 1",
    "goal": "kill all enemies",
    "rules": ["sample rule"],
    "rooms": [["A1", "a", 0]],
    "connections": [],
    "dungeon_monsters": [["Bandit Guard", 1, 0]],
    "obstacles": 0,
    "traps": 0,
    "hazardous terrain": 0,
    "difficult terrain": 0,
    "chests": [],
    "coins": 0,
    "main theme": "Dungeon",
    "placements": dungeon_1_placement,
    "start": 1
}

dungeon_2_placement = {
    "monsters": [[3, 0, -3]],
    "obstacles": [],
    "traps": [],
    "hazardous terrain": [],
    "difficult terrain": [],
    "chests": [],
    "coins": [],
    "start": [[0, 0, 0]]
}

dungeon_2 = {
    "name": "Test 1",
    "goal": "kill all enemies",
    "rules": ["sample rule"],
    "rooms": [["J1", "a", 0], ["N1", "b", 0]],
    "connections": [["J1", [4, 3, -7, 0, "entry"], "N1", [2, 7, -9, 6, "exit"]]],
    "dungeon_monsters": [["Bandit Guard", 1, 0]],
    "obstacles": 0,
    "traps": 0,
    "hazardous terrain": 0,
    "difficult terrain": 0,
    "chests": [],
    "coins": 0,
    "main theme": "Dungeon",
    "placements": dungeon_2_placement,
    "start": 1
}

dungeon_3_placement = {
    "monsters": [[3, 0, -3]],
    "obstacles": [[0, 1, -1], [1, 0, -1]],
    "traps": [],
    "hazardous terrain": [],
    "difficult terrain": [],
    "chests": [],
    "coins": [],
    "start": [[0, 0, 0]]
}

dungeon_3 = {
    "name": "Test 1",
    "goal": "kill all enemies",
    "rules": ["sample rule"],
    "rooms": [["A1", "a", 0]],
    "connections": [],
    "dungeon_monsters": [["Bandit Guard", 1, 0]],
    "obstacles": 2,
    "traps": 0,
    "hazardous terrain": 0,
    "difficult terrain": 0,
    "chests": [],
    "coins": 0,
    "main theme": "Dungeon",
    "placements": dungeon_3_placement,
    "start": 1
}

validity_dungeons = [dungeon_1, dungeon_2, dungeon_3]
