from solutions import helpers
import numpy as np

filename = 'input'

int_sequences = helpers.read_each_line_as_delimited_int_sequence(filename, delimiter=",")

start = int_sequences[0]

n_days = 256

cycle_tracker = {k: {'ready': 0, 'waiting': 0} for k in range(7)}

print(cycle_tracker)

for fish in start:
    cycle_tracker[fish]['ready'] += 1

for day in range(n_days):
    mod = day % 7
    birthing = cycle_tracker[mod]['ready']
    cycle_tracker[(day+2) % 7]['waiting'] += birthing
    cycle_tracker[mod]['ready'] += cycle_tracker[mod]['waiting']
    cycle_tracker[mod]['waiting'] = 0

    n_fishes = sum(sum(v.values()) for v in cycle_tracker.values())
    print(n_fishes)

