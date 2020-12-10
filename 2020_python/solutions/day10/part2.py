with open('input', 'r') as f:
    joltages = [int(line.strip('\n')) for line in f]

sorted_joltages = sorted(joltages)
device_joltage = max(joltages) + 3
sorted_joltages.append(device_joltage)
sorted_joltages.insert(0, 0)

print(sorted_joltages)

multiplier = 1
ix = 0
l = len(sorted_joltages)
while ix < l - 1:
    joltage = sorted_joltages[ix]

    # jump of 3
    if sorted_joltages[ix+1] - joltage == 3:
        multiplier = multiplier
        ix += 1

    # jumps of 1
    # 5 in a row - pray there aren't any of these
    elif ix+5 < l and (sorted_joltages[ix+5] - joltage == 5):
        print("jump of 5")
        ix += 5

    # 4 in a row
    # (0), 1, 2, 3, 4, (7)
    # (0), 1, 2, 4, (7)
    # (0), 1, 3, 4, (7)
    # (0), 2, 3, 4, (7)
    # (0), 1, 4, (7)
    # (0), 2, 4, (7)
    # (0), 3, 4, (7)
    elif ix+4 < l and (sorted_joltages[ix+4] - joltage == 4):
        multiplier *= 7
        ix += 4

    # 3 in a row
    # (0), 1, 2, 3, (6)
    # (0), 1, 3, (6)
    # (0), 2, 3, (6)
    # (0), 3, (6)
    elif ix+3 < l and (sorted_joltages[ix+3] - joltage == 3):
        multiplier *= 4
        ix += 3

    # 2 in a row
    # (0), 1, 2, (5)
    # (0), 2, (5)
    elif ix+2 < l and sorted_joltages[ix+2] - joltage == 2:
        multiplier *= 2
        ix += 2

    # 1 in a row
    # (0), 1, (4)
    elif sorted_joltages[ix+1] - joltage == 1:
        multiplier = multiplier
        ix += 1

print(multiplier)


