import re

from solutions import helpers

filepath = 'input'
# filepath = 'test'

instructions = helpers.read_each_line_as_string(filepath)
single_line_instructions = ''.join(instructions)

pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

matches = pattern.findall(single_line_instructions)
total = sum(int(match[0]) * int(match[1]) for match in matches)

print(total)
