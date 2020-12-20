import re

with open('input2', 'r') as f:
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
    if message == '':
        return False, message

    for subrule in rule:
        matches, remainder = matches_subrule(subrule, message)
        if matches:
            return True, remainder

    return False, message


def matches_31s(remainder, n31s):
    matches_31, remainder_after_31 = matches_subrule('31', remainder)
    if matches_31:
        if remainder_after_31 == '':
            return True, n31s+1
        else:
            return matches_31s(remainder_after_31, n31s+1)
    else:
        return False, 0


def matches_42s_then_31s(remainder, n42s):
    matches_42, remainder_after_42 = matches_subrule('42', remainder)
    if matches_42:
        ends_in_31s, n31s = matches_31s(remainder_after_42, 0)
        if ends_in_31s and n31s < n42s + 1:
            return True
        else:
            return matches_42s_then_31s(remainder_after_42, n42s + 1)
    else:
        return False


def matches_rule_zero(message):
    # 0 : 8 11
    # 8 : 42 ( 42 ( 42 (...) ) )
    # 11: 42 ( 42 ( 42 (...) 31) 31) 31
    return matches_42s_then_31s(message, 0)


n_matches = 0
for message in messages:
    if matches_rule_zero(message):
        n_matches += 1

print(n_matches)