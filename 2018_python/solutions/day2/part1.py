from collections import Counter

hasTwoTotal = 0
hasThreeTotal = 0

with open('input', 'r') as f:
    for line in f:
        boxid = line.strip('\n')
        c = Counter(boxid)
        hasTwo = False
        hasThree = False
        for key, val in c.items():
            if val == 2:
                hasTwo = True
            if val == 3:
                hasThree = True

        if hasTwo:
            hasTwoTotal += 1

        if hasThree:
            hasThreeTotal += 1

print(hasTwoTotal)
print(hasThreeTotal)
print(hasTwoTotal * hasThreeTotal)
