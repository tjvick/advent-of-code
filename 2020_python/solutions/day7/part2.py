import re

with open('input.txt', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

all_pairs = []
pair_dict = {}

rule_re = re.compile(r'^([\w\s]+) bags contain (\d+ .* bags?[,.])+$')
empty_rule_re = re.compile(r'^([\w\s]+) bags contain no other bags.$')
for rule in file_contents:
    m = rule_re.match(rule)
    if m:
        outer_color = m.group(1)
        inner_colors = re.findall(r'(\d+) ([\w\s]+) bags?', m.group(2))
        pair_dict[outer_color] = inner_colors

        for inner_color in inner_colors:
            all_pairs.append((outer_color, inner_color))
    else:
        n = empty_rule_re.match(rule)
        outer_color = n.group(1)

print(pair_dict)

converted = pair_dict['shiny gold']
conversion_dict = {}
for countstr, color in converted:
    if color not in conversion_dict:
        conversion_dict[color] = int(countstr)
    else:
        conversion_dict[color] += int(countstr)


def do_it(conversion_dict, total_conversion_dict):
    new_conversion_dict = {}
    for outer_color, outer_count in conversion_dict.items():
        if outer_color in pair_dict.keys():
            things_to_replace_this_with = pair_dict[outer_color]
            for countstr, inner_color in things_to_replace_this_with:
                if inner_color not in new_conversion_dict:
                    new_conversion_dict[inner_color] = int(countstr) * outer_count
                else:
                    new_conversion_dict[inner_color] += int(countstr) * outer_count

                if inner_color not in total_conversion_dict:
                    total_conversion_dict[inner_color] = int(countstr) * outer_count
                else:
                    total_conversion_dict[inner_color] += int(countstr) * outer_count

    remainder = new_conversion_dict.copy()

    return remainder, total_conversion_dict


print(conversion_dict)

total_conversion_dict = conversion_dict.copy()
remainder, total_conversion_dict = do_it(conversion_dict, total_conversion_dict)
print(total_conversion_dict)
print(remainder)
while remainder != {}:
    remainder, total_conversion_dict = do_it(remainder.copy(), total_conversion_dict.copy())
    print(total_conversion_dict)
    print(remainder)

print(total_conversion_dict)

bags_inside = sum([count for _, count in total_conversion_dict.items()])
print(bags_inside)
