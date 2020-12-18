import re

with open('input', 'r') as f:
    expressions = [line.strip('\n') for line in f]


parens_re = re.compile(r'\(([\d+* ]+)\)')
single_pair_re = re.compile(r'^\(?\d+ [+*] \d+\)?$')
first_pair_re = re.compile(r'^\d+ [+*] \d+')
number_re = re.compile(r'^\d+$')


def evaluate(expression):
    if number_re.match(expression):
        return expression

    if single_pair_re.match(expression):
        return str(eval(expression))

    if parens_re.search(expression):
        return evaluate(parens_re.sub(lambda x: evaluate(x.group(1)), expression))

    return evaluate(first_pair_re.sub(lambda x: evaluate(x.group()), expression))


print(evaluate('5 + (8 * 3 + 9 + 3 * 4 * 3)') == '437')


total = sum([int(evaluate(expression)) for expression in expressions])

print(total)
