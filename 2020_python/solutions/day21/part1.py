import re
from collections import Counter

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

all_ingredients = []
allergen_map = {}
for row_contents in file_contents:
    m = re.match(r'^([^(]+) \(contains (.+)\)$', row_contents)
    ingredients = m.group(1).split(" ")
    allergens = m.group(2).split(", ")
    for allergen in allergens:
        if allergen not in allergen_map:
            allergen_map[allergen] = set(ingredients)
        else:
            allergen_map[allergen] = allergen_map[allergen].intersection(set(ingredients))

    all_ingredients += ingredients

print(allergen_map)

all_suspect_ingredients = set()
for allergen, ingredients in allergen_map.items():
    all_suspect_ingredients = all_suspect_ingredients.union(ingredients)


safe_ingredients = set(all_ingredients).difference(all_suspect_ingredients)
print(safe_ingredients)

c = dict(Counter(all_ingredients))
print(c)

safe_appearances = sum([c[safe_ingredient] for safe_ingredient in safe_ingredients])
print(safe_appearances)
