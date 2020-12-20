import re

with open('input2', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

break_point = file_contents.index('')
rule_strings = file_contents[:break_point]
messages = file_contents[break_point+1:]

rules = {}
for rule_string in rule_strings:
    m = re.match(r'^(\d+): (.*)$', rule_string)
    id = m.group(1)
    subrules = m.group(2).split(" | ")
    rules[id] = subrules

# print(rules)


def matches_subrule(subrule, message):
    # print('message', message)
    if subrule == '"a"':
        if message[0] == 'a':
            return True, message[1:]
        else:
            return False, message

    if subrule == '"b"':
        if message[0] == 'b':
            return True, message[1:]
        else:
            return False, message

    remainder = message
    for ruleref in subrule.split(' '):
        # print('ruleref', ruleref, "of subrule", subrule)
        matches, remainder = matches_rule(rules[ruleref], remainder)
        if not matches:
            return False, message

    return True, remainder


def matches_rule(rule, message):
    # print('rule', rule)
    # print('message', message)
    if message == '':
        return False, message

    for subrule in rule:
        # print("subrule", subrule, "of rule", rule)
        matches, remainder = matches_subrule(subrule, message)
        # print("matches", matches)
        # print("remainder", remainder)
        if matches:
            return True, remainder

    return False, message


def matches_31s(remainder, n31s):
    matches_31, remainder_after_31 = matches_rule(rules['31'], remainder)
    if matches_31:
        if remainder_after_31 == '':
            return True, n31s+1
        else:
            return matches_31s(remainder_after_31, n31s+1)
    else:
        return False, 0


def match_the_damn_thing(remainder, n42s):
    print(remainder)
    matches_42, remainder_after_42 = matches_rule(rules['42'], remainder)
    print('matches_42', matches_42)
    print('remainder_after_42', remainder_after_42)
    if matches_42:
        rest_31s, n31s = matches_31s(remainder_after_42, 0)
        print('n31s:', n31s, 'n42s:', n42s)
        if rest_31s and n31s <= n42s:
            return True
        else:
            return match_the_damn_thing(remainder_after_42, n42s+1)
    else:
        return False


def matches_rule_zero(message):
    return match_the_damn_thing(message, 0)


n_matches = 0
for message in messages:
    if matches_rule_zero(message):
        n_matches += 1

print(n_matches)

# 337 too high
# 327 too high