import numpy as np
import math
import re
import collections

with open('input', 'r') as f:
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

print(rules)


def matches_subrule(subrule, message):
    print('subrule', subrule)
    print('message', message)
    if subrule == '"a"':
        print("test a")
        if message[0] == 'a':
            print("matches a")
            return True, message[1:]
        else:
            return False, message

    if subrule == '"b"':
        print("test b")
        if message[0] == 'b':
            print("matches b")
            return True, message[1:]
        else:
            return False, message

    remainder = message
    for ruleref in subrule.split(' '):
        matches, remainder = matches_rule(rules[ruleref], remainder)
        if not matches:
            return False, message

        print('matches', matches)
        print('remainder', remainder)

    return True, remainder


def matches_rule(rule, message):
    print('rule', rule)
    print('message', message)
    for subrule in rule:
        print("subrule", subrule, "of rule", rule)
        matches, remainder = matches_subrule(subrule, message)
        print("matches", matches)
        print("remainder", remainder)
        if matches:
            return True, remainder

    return False, message


def matches_rule_zero(message):
    matches, remainder = matches_rule(rules['0'], message)
    if matches and remainder == '':
        return True


n_matches = 0
for message in messages:
    if matches_rule_zero(message):
        n_matches += 1

print(n_matches)