import re

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

final_map = {}
while len(final_map) < len(allergen_map):
    for allergen, ingredients in allergen_map.items():
        if len(ingredients) == 1:
            ingredient = list(ingredients)[0]
            final_map[allergen] = ingredient
            [allergen_map[a].discard(ingredient) for a in allergen_map.keys()]

print(final_map)
keylist = sorted([key for key in final_map.keys()])
print(",".join(final_map[key] for key in keylist))