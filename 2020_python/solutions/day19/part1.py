import re

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

break_point = file_contents.index('')
rule_strings = file_contents[:break_point]
messages = file_contents[break_point+1:]

rules = {}
for rule_string in rule_strings:
    m = re.match(r'^(\d+): (.*)$', rule_string)
    rule_id = m.group(1)
    subrules = m.group(2).strip('"').split(" | ")
    rules[rule_id] = subrules


def matches_subrule(subrule, message):
    if subrule in 'ab':
        if message[0] == subrule:
            return True, message[1:]
        else:
            return False, message

    remainder = message
    for rule_id in subrule.split(' '):
        matches, remainder = matches_rule(rules[rule_id], remainder)
        if not matches:
            return False, message

    return True, remainder


def matches_rule(rule, message):
    for subrule in rule:
        matches, remainder = matches_subrule(subrule, message)
        if matches:
            return True, remainder

    return False, message


def matches_rule_zero(message):
    matches, remainder = matches_subrule('0', message)
    if matches and remainder == '':
        return True


n_matches = 0
for message in messages:
    if matches_rule_zero(message):
        n_matches += 1

print(n_matches)