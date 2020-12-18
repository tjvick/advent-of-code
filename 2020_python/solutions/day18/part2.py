import re

with open('input', 'r') as f:
    expressions = [line.strip('\n') for line in f]


number_re = re.compile(r'^\d+$')
single_re = re.compile(r'^\(?\d+ [+*] \d+\)?$')
parens_re = re.compile(r'\(([\d+* ]+)\)')
addition_re = re.compile(r'\d+ \+ \d+')
multiply_re = re.compile(r'\d+ \* \d+')


def evaluate(expression):
    if number_re.match(expression):
        return expression

    if single_re.match(expression):
        return str(eval(expression))

    if parens_re.search(expression):
        return evaluate(parens_re.sub(lambda x: evaluate(x.group(1)), expression))

    if addition_re.search(expression):
        return evaluate(addition_re.sub(lambda x: evaluate(x.group()), expression))

    return evaluate(multiply_re.sub(lambda x: evaluate(x.group()), expression))


print(evaluate('1 + 2 * 3 + 4 * 5 + 6') == '231')
print(evaluate('1 + (2 * 3) + (4 * (5 + 6))') == '51')
print(evaluate('2 * 3 + (4 * 5)') == '46')
print(evaluate('5 + (8 * 3 + 9 + 3 * 4 * 3)') == '1445')
print(evaluate('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == '669060')
print(evaluate('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == '23340')
print(evaluate('4 * (4 * (4 + 8 + 9 * 7) + 5 + 9 * 6 * (4 + 4 + 8 + 7 * 9 + 3)) * 3 + (6 + 5 * 9 * 5 * (4 * 4 + 5 + 3)) + (6 * 9 * 5 * 3 * 7 + 2) * (9 * 4 * (2 * 8))') == '76301352787968')


total = sum([int(evaluate(expression)) for expression in expressions])

print(total)
