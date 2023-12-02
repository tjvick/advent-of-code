from solutions import helpers
import numpy as np
import re

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'
# filename = 'test'

strings = helpers.read_each_line_as_string(filename)

game_id_sum = 0
for game_string in strings:
    m = re.match(r'Game (\d+): (.*)', game_string)
    game_id = m.group(1)
    game_description = m.group(2)
    print(game_id, game_description)
    game_rounds = game_description.split(';')
    print(game_rounds)
    game_possible = True
    for game_round in game_rounds:
        print(game_round)
        reds = re.search(r'(\d+) red', game_round)
        n_reds = int(reds.group(1)) if reds else 0
        blues = re.search(r'(\d+) blue', game_round)
        n_blues = int(blues.group(1)) if blues else 0
        greens = re.search(r'(\d+) green', game_round)
        n_greens = int(greens.group(1)) if greens else 0

        if n_reds > 12 or n_greens > 13 or n_blues > 14:
            game_possible = False

    if game_possible:
        game_id_sum += int(game_id)


print(game_id_sum)
