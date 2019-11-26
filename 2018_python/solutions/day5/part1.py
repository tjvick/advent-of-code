with open('input.txt', 'r') as f:
    for line in f:
        polymer = list(line.strip('\n'))
        break

print(polymer)
print(len(polymer))

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


print(polymer)
print(len(polymer))
