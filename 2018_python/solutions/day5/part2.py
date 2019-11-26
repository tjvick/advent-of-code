with open('input.txt', 'r') as f:
    for line in f:
        og_polymer = list(line.strip('\n'))
        break

print(og_polymer)
print(len(og_polymer))

polymer_lengths = []
for c in list('abcdefghijklmnopqrstuvwxyz'):
    polymer = list(''.join(og_polymer).replace(c, '').replace(c.upper(), ''))
    reactions_exist = True
    while reactions_exist:
        reactions_exist = False
        for idx in range(len(polymer)-1):
            if polymer[idx].upper() == polymer[idx+1].upper():
                if polymer[idx] != polymer[idx+1]:
                    polymer[idx] = ' '
                    polymer[idx+1] = ' '
                    reactions_exist = True

        polymer = list(''.join(polymer).replace(' ', ''))

    polymer_lengths.append(len(polymer))
    print(c)
    print(polymer)
    print(len(polymer))

print(min(polymer_lengths))
