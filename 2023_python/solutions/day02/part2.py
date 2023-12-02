from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

strings = helpers.read_each_line_as_string(filename)

power_sum = 0
for game_string in strings:
    m = re.match(r'Game (\d+): (.*)', game_string)
    game_id = m.group(1)
    game_description = m.group(2)
    print(game_id, game_description)
    game_rounds = game_description.split(';')
    print(game_rounds)
    game_possible = True
    min_reds = 0
    min_blues = 0
    min_greens = 0
    for game_round in game_rounds:
        reds = re.search(r'(\d+) red', game_round)
        n_reds = int(reds.group(1)) if reds else 0
        min_reds = max(n_reds, min_reds)
        blues = re.search(r'(\d+) blue', game_round)
        n_blues = int(blues.group(1)) if blues else 0
        min_blues = max(n_blues, min_blues)
        greens = re.search(r'(\d+) green', game_round)
        n_greens = int(greens.group(1)) if greens else 0
        min_greens = max(n_greens, min_greens)

    power = min_reds * min_blues * min_greens

    power_sum += power


print(power_sum)
